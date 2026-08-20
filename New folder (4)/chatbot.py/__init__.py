"""chatbot - installable package wrapper around chatbot_modules/.

`import chatbot` (or any `chatbot.<subpackage>.<module>`) loads the flat,
numbered files in chatbot_modules/ - unchanged, still the single source of
truth and still Pydroid-3-ready - as real, individually importable
modules. See _bootstrap.py for how and why.

Common classes are re-exported here for convenience:

    from chatbot import ChatBot, IntentEngine, TypoCorrector, ChatDatabase

Anything else can be reached via its real dotted path, e.g.:

    from chatbot.creative.creative_writing import PoemWriter, StoryTeller
"""
from chatbot._bootstrap import load_all as _load_all

_ns = _load_all()

# Best-effort convenience re-exports - if a name isn't present (e.g. an
# optional dependency like PyTorch is missing, so a class was never
# defined), skip it rather than raising ImportError for a piece nobody
# asked for.
_CONVENIENCE_NAMES = [
    "ChatBot",
    "Database",
    "IntentEngine",
    "TypoCorrector",
    "PoemWriter",
    "StoryTeller",
    "MemoryStore",
    "NeuralIntentClassifier",
    "SentimentClassifier",
]
for _name in _CONVENIENCE_NAMES:
    if _name in _ns:
        globals()[_name] = _ns[_name]

__all__ = [name for name in _CONVENIENCE_NAMES if name in _ns]

del _name, _ns
