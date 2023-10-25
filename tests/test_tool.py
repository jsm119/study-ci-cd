import pytest

from app import tool


def test_sub():
    assert tool.sub(3, 4) == -1
    assert tool.sub(4.5, 4) == 0
    assert tool.sub(3.9, 4) == -1
    assert tool.sub(4.2, 3.8) == 0


def test_word_count():
    assert tool.word_count("arm pod race", "pod") == 1
    assert tool.word_count("arm pod race", "lap") == 0
    assert tool.word_count("arm arm arm", "arm") == 3
