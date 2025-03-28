import pytest
import re
from io import StringIO

from middletest import read_file, count_words, count_sentences, count_sentence_endings, count_punctuation_marks

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
    
# count_sentence_endings
@pytest.mark.parametrize("text, expected", [
    ("Привіт! Це тестовий текст.", 2),
    ("", 0),
    ("Тест.", 1)
])
def test_count_sentence_endings(text, expected):
    assert count_sentence_endings(text) == expected