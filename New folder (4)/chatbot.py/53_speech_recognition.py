"""Section 12: OFFLINE SPEECH RECOGNITION (optional, opt-in)
Auto-split addition - see main.py for load order.

Adds optional voice input, entirely offline: Vosk does
speech-to-text from a small, locally-downloaded language model (no
cloud API, no API key, no internet needed at runtime) - matching the
app's offline-first design the same way the LLM bridge (11_llm_hybrid.py)
stays opt-in rather than required.

WHY VOSK: it's pure-offline (unlike SpeechRecognition's free backend,
which calls Google's cloud API and would quietly break the "offline"
promise), works from a single downloadable model directory, and has
pip wheels for both desktop and Android/Pydroid.

RECORDING BACKEND: two independent, optional backends, tried in order:
  1. `sounddevice` (desktop Windows/Mac/Linux - needs PortAudio)
  2. `plyer`'s audio facade (Android via Pydroid, and other platforms
     plyer supports) - records to a file instead of a live stream, so
     transcription happens after recording finishes rather than live.
If neither is available, or the Vosk model isn't downloaded, speech
input simply isn't offered - same "fails closed, explains why" pattern
as the unavailable-speech message in the calling application.

SETUP (see README): `pip install .[speech]`, then download a Vosk
model (e.g. vosk-model-small-en-us-0.15 from https://alphacephei.com/vosk/models)
and extract it into chatbot_modules/vosk_model/ - a plain folder, not
a file, so this is a directory check rather than a specific filename.
"""
import io
import json
import logging
import os
import tempfile
import wave

logger = logging.getLogger("chatbot.speech_recognition")

# ---- optional dependency guards (same pattern as the ML/vision guards
# in 01_config_and_db.py: probe once, remember the result, never crash
# the rest of the app if something's missing) ------------------------
try:
    import vosk
    VOSK_AVAILABLE = True
except ImportError:
    VOSK_AVAILABLE = False

try:
    import sounddevice as sd
    import numpy as np
    SOUNDDEVICE_AVAILABLE = True
except (ImportError, OSError):
    # OSError too: sounddevice imports fine even without a working
    # PortAudio install on some platforms, but raises OSError the
    # moment you actually touch the audio system - catch both here so
    # is_available() below reflects reality, not just "importable".
    SOUNDDEVICE_AVAILABLE = False

try:
    from plyer import audio as plyer_audio
    PLYER_AUDIO_AVAILABLE = True
except ImportError:
    PLYER_AUDIO_AVAILABLE = False

VOSK_MODEL_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "vosk_model")
VOSK_SAMPLE_RATE = 16000  # Vosk's small models expect 16kHz mono audio.


class OfflineSpeechRecognizer:
    """Voice input helper. Loads the Vosk model
    lazily (only on first actual use, not at import time) - eagerly
    loading an ML model at startup is exactly the mistake already
    found and avoided elsewhere in this app (see the code review's
    startup-cost notes and 01_config_and_db.py's ML backend guards).
    """

    def __init__(self, model_dir: str = VOSK_MODEL_DIR) -> None:
        self.model_dir = model_dir
        self._model = None  # lazily loaded vosk.Model
        self._load_error = None

    def is_available(self) -> bool:
        """True only if every piece needed to actually record and
        transcribe speech is present: the vosk package, a downloaded
        model directory, and at least one working recording backend.
        """
        if not VOSK_AVAILABLE:
            return False
        if not os.path.isdir(self.model_dir):
            return False
        return SOUNDDEVICE_AVAILABLE or PLYER_AUDIO_AVAILABLE

    def unavailable_reason(self) -> str:
        """A plain-language explanation for why is_available() is
        False, for the calling application to show instead of hiding the mic
        button silently - same "fail closed with a plain-language
        message" philosophy the code review praised elsewhere."""
        if not VOSK_AVAILABLE:
            return "Voice input needs the 'vosk' package (pip install .[speech])."
        if not os.path.isdir(self.model_dir):
            return (
                "Voice input needs a Vosk model. Download one from "
                "https://alphacephei.com/vosk/models (e.g. "
                "vosk-model-small-en-us-0.15) and extract it into "
                f"{self.model_dir}"
            )
        if not (SOUNDDEVICE_AVAILABLE or PLYER_AUDIO_AVAILABLE):
            return (
                "Voice input needs a microphone backend: 'sounddevice' "
                "on desktop, or the device's own recorder on Android."
            )
        return ""

    def _ensure_model_loaded(self) -> "vosk.Model | None":
        if self._model is not None:
            return self._model
        if self._load_error is not None:
            return None
        try:
            vosk.SetLogLevel(-1)  # vosk logs to stderr by default; quiet it
            self._model = vosk.Model(self.model_dir)
        except Exception as e:  # noqa: BLE001 - genuinely any failure here
            # means "no usable model", which the caller should treat the
            # same way regardless of the underlying exception type.
            logger.warning("Could not load Vosk model from %s: %s", self.model_dir, e)
            self._load_error = e
            return None
        return self._model

    def transcribe_wav_bytes(self, wav_bytes: bytes) -> "str | None":
        """Transcribes a complete, already-recorded WAV file (16kHz,
        16-bit mono, as both recording backends below produce). Returns
        None on any failure rather than raising - the GUI just shows
        "didn't catch that" and lets the user try again or type.
        """
        model = self._ensure_model_loaded()
        if model is None:
            return None
        try:
            with wave.open(io.BytesIO(wav_bytes), "rb") as wf:
                if wf.getnchannels() != 1 or wf.getsampwidth() != 2:
                    logger.warning(
                        "Unexpected WAV format (channels=%s, sampwidth=%s) - "
                        "Vosk expects 16-bit mono.",
                        wf.getnchannels(), wf.getsampwidth(),
                    )
                    return None
                recognizer = vosk.KaldiRecognizer(model, wf.getframerate())
                recognizer.SetWords(False)
                while True:
                    data = wf.readframes(4000)
                    if not data:
                        break
                    recognizer.AcceptWaveform(data)
                result = json.loads(recognizer.FinalResult())
                text = result.get("text", "").strip()
                return text or None
        except Exception as e:  # noqa: BLE001
            logger.warning("Speech transcription failed: %s", e)
            return None

    def _record_with_sounddevice(self, duration: float) -> "bytes | None":
        try:
            frames = sd.rec(
                int(duration * VOSK_SAMPLE_RATE),
                samplerate=VOSK_SAMPLE_RATE, channels=1, dtype="int16",
            )
            sd.wait()
        except Exception as e:  # noqa: BLE001 - PortAudio errors vary by OS
            logger.warning("Microphone recording (sounddevice) failed: %s", e)
            return None
        buf = io.BytesIO()
        with wave.open(buf, "wb") as wf:
            wf.setnchannels(1)
            wf.setsampwidth(2)
            wf.setframerate(VOSK_SAMPLE_RATE)
            wf.writeframes(frames.tobytes())
        return buf.getvalue()

    def _record_with_plyer(self, duration: float) -> "bytes | None":
        """plyer's audio facade records to a FILE (not a live buffer),
        so this starts recording, waits out the duration, stops, then
        reads the file back - a real (if small) blocking sleep, always
        called from a background thread by the calling application."""
        import time as _time

        tmp_path = os.path.join(tempfile.gettempdir(), "chatbot_voice_input.wav")
        try:
            plyer_audio.file_path = tmp_path
            plyer_audio.start()
            _time.sleep(duration)
            plyer_audio.stop()
        except Exception as e:  # noqa: BLE001 - platform audio APIs vary widely
            logger.warning("Microphone recording (plyer) failed: %s", e)
            return None
        try:
            with open(tmp_path, "rb") as f:
                return f.read()
        except OSError as e:
            logger.warning("Could not read recorded audio file %s: %s", tmp_path, e)
            return None
        finally:
            try:
                os.remove(tmp_path)
            except OSError:
                pass

    def listen_and_transcribe(self, duration: float = 5.0) -> "str | None":
        """Records `duration` seconds from whichever backend is
        available and transcribes it. Safe to call from a background
        thread (does real blocking I/O - recording and model
        inference). Returns None (never raises) if anything
        along the way fails, so the caller can show one consistent
        "didn't catch that, try again or just type" message.
        """
        if not self.is_available():
            return None
        wav_bytes = None
        if SOUNDDEVICE_AVAILABLE:
            wav_bytes = self._record_with_sounddevice(duration)
        if wav_bytes is None and PLYER_AUDIO_AVAILABLE:
            wav_bytes = self._record_with_plyer(duration)
        if wav_bytes is None:
            return None
        return self.transcribe_wav_bytes(wav_bytes)
