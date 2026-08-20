"""Tests for TypoCorrector and IntentEngine (chatbot_modules/12_intent_engine.py).

Highest-value test target per the code review (§8, priority #1):
pure functions/classes, deterministic, no I/O, already had the closest
thing to tests (the accuracy harness) of anything in the codebase.
"""
import pytest

from chatbot.nlp.intent_engine import IntentEngine, TypoCorrector


@pytest.fixture()
def typo_corrector():
    return TypoCorrector()


@pytest.fixture()
def engine():
    return IntentEngine()


class TestTypoCorrector:
    def test_known_common_typo_is_corrected(self, typo_corrector):
        # "tge" -> "the" is in COMMON_TYPOS - a stable, hand-written
        # mapping, so this should never silently change.
        assert typo_corrector.correct_text("tge") == "the"

    def test_correctly_spelled_word_is_left_alone(self, typo_corrector):
        assert typo_corrector.correct_text("hello") == "hello"

    def test_correction_applies_within_a_sentence(self, typo_corrector):
        result = typo_corrector.correct_text("i think teh answer is here")
        assert "the answer" in result

    def test_unknown_word_far_from_any_known_word_is_untouched(self, typo_corrector):
        # A name or made-up word shouldn't get mangled by the edit-distance
        # fallback - only words within distance 1 of exactly one known
        # word should ever be touched.
        result = typo_corrector.correct_text("Xyzzyplonk")
        assert result == "Xyzzyplonk"


class TestIntentEngine:
    def test_register_and_handle_dispatches_on_pattern_match(self, engine):
        calls = []

        def handler(text, m):
            calls.append((text, m.group(0) if m else None))
            return "handled"

        engine.register("greeting_test", [r"^\s*hi there\s*$"], handler)
        result = engine.handle("hi there", bot=None)

        assert result == "handled"
        assert calls == [("hi there", "hi there")]

    def test_handle_returns_none_when_nothing_matches(self, engine):
        engine.register("greeting_test", [r"^\s*hi there\s*$"], lambda t, m: "handled")
        assert engine.handle("this matches nothing registered", bot=None) is None

    def test_first_registered_matching_pattern_wins(self, engine):
        engine.register("first", [r"^\s*ping\s*$"], lambda t, m: "first")
        engine.register("second", [r"^\s*ping\s*$"], lambda t, m: "second")
        assert engine.handle("ping", bot=None) == "first"

    def test_multiple_patterns_for_one_intent_all_dispatch_to_it(self, engine):
        engine.register("greet", [r"^\s*hi\s*$", r"^\s*hello\s*$"], lambda t, m: "greeted")
        assert engine.handle("hi", bot=None) == "greeted"
        assert engine.handle("hello", bot=None) == "greeted"

    def test_last_matched_intent_tracks_successful_match(self, engine):
        engine.register("greet", [r"^\s*hi\s*$"], lambda t, m: "greeted")
        engine.handle("hi", bot=None)
        assert engine.last_matched_intent == "greet"
