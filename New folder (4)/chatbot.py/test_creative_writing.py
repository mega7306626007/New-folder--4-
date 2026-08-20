"""Tests for PoemWriter and StoryTeller (chatbot_modules/04_creative_writing.py).

Priority #3 per the code review (§8): pure, deterministic-given-seed,
easy to assert against - and exactly the class of bug (a missing
`return` making `rhyming_couplets()` silently return None on every
call) that a two-line test would have caught the day it was introduced.
"""
import random

import pytest

from chatbot.creative.creative_writing import PoemWriter, StoryTeller


@pytest.fixture()
def poem_writer():
    return PoemWriter()


@pytest.fixture()
def story_teller():
    return StoryTeller()


class TestPoemWriter:
    @pytest.mark.parametrize("lang", ["en", "sw", "fr"])
    def test_haiku_returns_three_nonempty_lines(self, poem_writer, lang):
        haiku = poem_writer.haiku(lang=lang)
        assert haiku is not None
        lines = haiku.split("\n")
        assert len(lines) == 3
        assert all(line.strip() for line in lines)

    def test_acrostic_has_one_line_per_letter(self, poem_writer):
        result = poem_writer.acrostic("CAT")
        lines = result.split("\n")
        assert len(lines) == 3
        assert [line[0] for line in lines] == ["C", "A", "T"]

    def test_acrostic_strips_non_letters(self, poem_writer):
        result = poem_writer.acrostic("C-A-T!")
        assert len(result.split("\n")) == 3

    def test_acrostic_falls_back_on_empty_input(self, poem_writer):
        # No letters at all -> falls back to "HELLO" rather than
        # returning an empty poem.
        result = poem_writer.acrostic("123")
        assert len(result.split("\n")) == len("HELLO")

    @pytest.mark.parametrize("lang", ["en", "sw", "fr"])
    def test_rhyming_couplets_is_not_none(self, poem_writer, lang):
        # This is the exact bug the code review flagged (§2): a missing
        # `return` silently made this always return None. Guard against
        # a regression directly.
        result = poem_writer.rhyming_couplets(lang=lang)
        assert result is not None
        assert isinstance(result, str)
        assert result.strip() != ""

    def test_rhyming_couplets_respects_num_couplets(self, poem_writer):
        result = poem_writer.rhyming_couplets(num_couplets=2)
        # Each couplet contributes 2 lines.
        assert len([l for l in result.split("\n") if l.strip()]) >= 2

    def test_rhyming_couplets_unknown_theme_falls_back_to_general(self, poem_writer):
        # Should not raise for a theme that isn't in THEME_WORDS.
        result = poem_writer.rhyming_couplets(theme="not_a_real_theme")
        assert result is not None

    def test_full_page_poem_is_nonempty(self, poem_writer):
        result = poem_writer.full_page_poem(num_stanzas=2)
        assert result is not None
        assert result.strip() != ""


class TestStoryTeller:
    def test_categories_returns_nonempty_list(self, story_teller):
        categories = story_teller.categories()
        assert isinstance(categories, list)
        assert len(categories) > 0

    def test_random_story_returns_title_and_text(self, story_teller):
        result = story_teller.random_story()
        assert result is not None
        title, text = result
        assert isinstance(title, str) and title
        assert isinstance(text, str) and text

    def test_random_story_from_specific_category(self, story_teller):
        category = story_teller.categories()[0]
        result = story_teller.random_story(category=category)
        assert result is not None

    def test_personalize_story_text_substitutes_name(self, story_teller):
        # Tests the actual substitution logic directly rather than
        # relying on a random story happening to include {name} -
        # avoids test flakiness from random.choice picking a template
        # without a name placeholder.
        result = story_teller._personalize_story_text(
            "{name} walked into the room.", user_name="Jordan", lang="en"
        )
        assert result == "Jordan walked into the room."

    def test_personalize_story_text_capitalizes_default_name(self, story_teller):
        result = story_teller._personalize_story_text(
            "{name} walked into the room.", user_name=None, lang="en"
        )
        assert result[0].isupper()

    @pytest.mark.parametrize("lang", ["en", "sw", "fr"])
    def test_random_story_works_in_all_three_languages(self, story_teller, lang):
        result = story_teller.random_story(lang=lang)
        assert result is not None
