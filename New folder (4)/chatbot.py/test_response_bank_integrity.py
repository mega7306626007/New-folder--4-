"""Response-bank data integrity tests (priority #4 per the code review,
§8): every bank should have all three language keys (en/sw/fr) with
non-empty lists. Would have caught the stale
13_response_banks_loader.py drift (§1) and will catch a future bank
that's missing a language.
"""
import pytest

REQUIRED_LANGUAGES = {"en", "sw", "fr"}


def _all_response_banks(chatbot_ns):
    """Every module-level dict whose name ends in _RESPONSES, collected
    from the fully-loaded shared namespace - this covers every response
    bank file (33-52) at once rather than importing each individually."""
    return {
        name: value
        for name, value in chatbot_ns.items()
        if name.endswith("_RESPONSES") and isinstance(value, dict)
    }


def test_at_least_one_response_bank_was_found(chatbot_ns):
    banks = _all_response_banks(chatbot_ns)
    assert len(banks) > 10, (
        "Expected many *_RESPONSES banks from files 33-52; found "
        f"{len(banks)} - did the response-bank files fail to load?"
    )


def test_every_response_bank_has_all_three_languages(chatbot_ns):
    banks = _all_response_banks(chatbot_ns)
    missing = {
        name: REQUIRED_LANGUAGES - set(bank.keys())
        for name, bank in banks.items()
        if not REQUIRED_LANGUAGES.issubset(bank.keys())
    }
    assert not missing, f"Response banks missing language keys: {missing}"


def test_every_language_variant_is_a_nonempty_list(chatbot_ns):
    banks = _all_response_banks(chatbot_ns)
    empty = []
    for name, bank in banks.items():
        for lang in REQUIRED_LANGUAGES:
            variants = bank.get(lang)
            if not variants:
                empty.append(f"{name}[{lang!r}]")
    assert not empty, f"Response bank language variants with no entries: {empty}"


def test_every_response_variant_is_a_nonempty_string(chatbot_ns):
    banks = _all_response_banks(chatbot_ns)
    bad = []
    for name, bank in banks.items():
        for lang, variants in bank.items():
            if lang not in REQUIRED_LANGUAGES or not isinstance(variants, list):
                continue
            for i, variant in enumerate(variants):
                if not isinstance(variant, str) or not variant.strip():
                    bad.append(f"{name}[{lang!r}][{i}]")
    assert not bad, f"Response bank entries that are empty/non-string: {bad}"
