import pytest
from unittest.mock import patch 
from middletest import read_file, count_words, count_sentences, count_sentence_endings, count_punctuation_marks, analyze_text
from io import StringIO

# Фікстура для підготовки тексту
@pytest.fixture
def sample_text():
    return "Привіт! Це тестовий текст. Він має кілька слів, речень і розділювальних знаків."

# count_punctuation_marks
@pytest.mark.parametrize("text, expected", [
    ("Привіт! Це тестовий текст.", 2),
    ("Тест, який має кілька слів.", 2),
    ("", 0)
])
def test_count_punctuation_marks(text, expected):
    assert count_punctuation_marks(text) == expected

# count_words
@pytest.mark.parametrize("text, expected", [
    ("Привіт світ", 2),
    ("Тест, який має кілька слів.", 5),
    ("", 0)
])
def test_count_words(text, expected):
    assert count_words(text) == expected
    
# count_sentences
@pytest.mark.parametrize("text, expected", [
    ("Привіт! Це тестовий текст.", 2),
    ("", 0),
    ("Тест.", 1)
])
def test_count_sentences(text, expected):
    assert count_sentences(text) == expected

# count_sentence_endings
@pytest.mark.parametrize("text, expected", [
    ("Привіт! Це тестовий текст.", 2),
    ("", 0),
    ("Тест.", 1)
])
def test_count_sentence_endings(text, expected):
    assert count_sentence_endings(text) == expected

def test_analyze_text():
    with patch('builtins.input', return_value='example.txt'):
        analyze_text()

# read_file
def test_read_file(sample_text):
    with patch("builtins.open", return_value=StringIO(sample_text)):
        assert read_file("fake_path.txt") == sample_text