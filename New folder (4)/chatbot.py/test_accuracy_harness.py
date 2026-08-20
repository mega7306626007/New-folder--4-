"""Turns the existing accuracy harness (chatbot_modules/21_main_and_tests.py,
ACCURACY_TEST_CASES + run_accuracy_test) into a real, CI-runnable
red/green signal (code review §8/§13) instead of a manual, printed
pass/fail count with no assert anywhere.

Deliberately a *floor*, not a pin to the exact current number: it should
fail if accuracy regresses meaningfully, not force a code change every
time one new phrasing test case is added.
"""
import pytest

from chatbot.app.main_and_tests import ACCURACY_TEST_CASES, run_accuracy_test
from chatbot.core.chatbot_core import ChatBot

# Current measured hit rate is 80% (28/35) - see the code review. A
# small buffer below that catches real regressions without being
# flaky over minor wording/threshold changes.
MINIMUM_ACCEPTABLE_HIT_RATE = 0.75


@pytest.fixture(scope="module")
def bot():
    return ChatBot()


def test_accuracy_harness_has_test_cases():
    assert len(ACCURACY_TEST_CASES) > 0


def test_intent_accuracy_meets_minimum_bar(bot):
    result = run_accuracy_test(bot, verbose=False)
    assert result["hit_rate"] >= MINIMUM_ACCEPTABLE_HIT_RATE, (
        f"Intent-recognition accuracy dropped to {result['hit_rate']:.0%} "
        f"({result['hits']}/{result['total']}), below the "
        f"{MINIMUM_ACCEPTABLE_HIT_RATE:.0%} floor. Misses: {result['misses']}"
    )


def test_no_crash_on_any_accuracy_test_case(bot):
    """Every (input, expected_intent) pair should at least get a
    response without raising - a crash here is worse than a wrong
    intent match."""
    for message, _expected_intent in ACCURACY_TEST_CASES:
        try:
            bot.respond(message)
        except Exception as e:  # noqa: BLE001 - intentionally broad, this
            # is a smoke test that anything can be asked without a crash
            pytest.fail(f"bot.respond({message!r}) raised {type(e).__name__}: {e}")
