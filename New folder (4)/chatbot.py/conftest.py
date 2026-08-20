"""Shared fixtures. Loading the chatbot package is not free (it execs
every numbered file in chatbot_modules/ into real modules - see
src/chatbot/_bootstrap.py) so we do it once per test session rather
than once per test.
"""
import pytest


@pytest.fixture(scope="session")
def chatbot_ns():
    """Full, fully-loaded shared namespace - use when a test needs
    something not worth a dedicated import (e.g. a response-bank dict)."""
    from chatbot._bootstrap import load_all
    return load_all()
