"""Tests for Database (chatbot_modules/01_config_and_db.py).

Priority #2 per the code review (§8): SQL correctness is exactly the
kind of thing that silently rots, and sqlite3.connect(":memory:") makes
this fast and fully isolated to test.
"""
import pytest

from chatbot.persistence.config_and_db import Database


@pytest.fixture()
def db():
    database = Database(":memory:")
    yield database
    database.close()


class TestFacts:
    def test_set_and_get_fact(self, db):
        db.set_fact("favorite_color", "blue")
        assert db.get_fact("favorite_color") == "blue"

    def test_get_missing_fact_returns_none(self, db):
        assert db.get_fact("never_set") is None

    def test_set_fact_overwrites_previous_value(self, db):
        db.set_fact("favorite_color", "blue")
        db.set_fact("favorite_color", "green")
        assert db.get_fact("favorite_color") == "green"

    def test_delete_fact(self, db):
        db.set_fact("temp", "value")
        assert db.delete_fact("temp") is True
        assert db.get_fact("temp") is None

    def test_delete_missing_fact_returns_false(self, db):
        assert db.delete_fact("never_existed") is False

    def test_get_all_facts(self, db):
        db.set_fact("a", "1")
        db.set_fact("b", "2")
        assert db.get_all_facts() == {"a": "1", "b": "2"}

    def test_clear_facts(self, db):
        db.set_fact("a", "1")
        db.clear_facts()
        assert db.get_all_facts() == {}


class TestTodos:
    def test_add_and_list_todo(self, db):
        row_id = db.add_todo_row("buy milk")
        rows = db.list_todo_rows()
        assert any(r["id"] == row_id for r in rows)

    def test_mark_todo_done(self, db):
        row_id = db.add_todo_row("water the plants")
        assert db.mark_todo_row_done(row_id) is True

    def test_remove_todo(self, db):
        row_id = db.add_todo_row("temporary")
        assert db.remove_todo_row(row_id) is True
        assert not any(r["id"] == row_id for r in db.list_todo_rows())

    def test_clear_todo_rows(self, db):
        db.add_todo_row("one")
        db.add_todo_row("two")
        db.clear_todo_rows()
        assert db.list_todo_rows() == []


class TestImportantDates:
    def test_set_and_get_important_date(self, db):
        db.set_important_date("birthday", 6, 15, 1995)
        result = db.get_important_date("birthday")
        assert result["month"] == 6
        assert result["day"] == 15
        assert result["year"] == 1995

    def test_delete_important_date(self, db):
        db.set_important_date("anniversary", 3, 1)
        assert db.delete_important_date("anniversary") is True
        assert db.get_important_date("anniversary") is None


class TestMisc:
    def test_is_empty_true_for_fresh_db(self, db):
        assert db.is_empty() is True

    def test_is_empty_false_after_writing(self, db):
        db.set_fact("x", "y")
        assert db.is_empty() is False

    def test_table_counts_reflects_writes(self, db):
        db.set_fact("x", "y")
        db.add_todo_row("something")
        counts = db.table_counts()
        assert counts["facts"] == 1
        assert counts["todos"] == 1

    def test_table_counts_covers_all_expected_tables(self, db):
        counts = db.table_counts()
        for table in ("facts", "todos", "conversation_log", "corrections"):
            assert table in counts
