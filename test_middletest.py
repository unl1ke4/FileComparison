import pytest
from unittest.mock import patch, mock_open
from middletest import (
    read_file, count_words, count_sentences,
    count_sentence_endings, count_punctuation_marks, analyze_text
)


@pytest.fixture
def sample_text():
    return (
        "Привіт! Це тестовий текст. "
        "Він має кілька слів, речень і розділювальних знаків."
    )


@pytest.mark.parametrize(
    "text, expected",
    [
        ("Привіт! Це тестовий текст.", 2),
        ("Тест, який має кілька слів.", 2),
        ("", 0)
    ]
)
def test_count_punctuation_marks(text, expected):
    assert count_punctuation_marks(text) == expected


@pytest.mark.parametrize(
    "text, expected",
    [
        ("Привіт світ", 2),
        ("Тест, який має кілька слів.", 5),
        ("", 0)
    ]
)
def test_count_words(text, expected):
    assert count_words(text) == expected


@pytest.mark.parametrize(
    "text, expected",
    [
        ("Привіт! Це тестовий текст.", 2),
        ("", 0),
        ("Тест.", 1)
    ]
)
def test_count_sentences(text, expected):
    assert count_sentences(text) == expected


@pytest.mark.parametrize(
    "text, expected",
    [
        ("Привіт! Це тестовий текст.", 2),
        ("", 0),
        ("Тест.", 1)
    ]
)
def test_count_sentence_endings(text, expected):
    assert count_sentence_endings(text) == expected


def test_analyze_text(sample_text):
    with patch("builtins.open", mock_open(read_data=sample_text)):
        analyze_text(file_path="example.txt")


def test_read_file(sample_text):
    with patch("builtins.open", mock_open(read_data=sample_text)):
        assert read_file("example.txt") == sample_text
