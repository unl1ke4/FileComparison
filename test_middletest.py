import pytest
from unittest.mock import patch 
from middletest import read_file, count_words, count_sentences, count_sentence_endings, count_punctuation_marks

# count_punctuation_marks
@pytest.mark.parametrize("text, expected", [
    ("Привіт! Це тестовий текст.", 2),
    ("Тест, який має кілька слів.", 2),
    ("", 0)
])
def test_count_punctuation_marks(text, expected):
    assert count_punctuation_marks(text) == expected

def test_analyze_text():
    with patch('builtins.input', return_value='example.txt'):
        analyze_text()