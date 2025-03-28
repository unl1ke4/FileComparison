import pytest
from unittest.mock import patch
from middletest import read_file, count_words, count_sentences, count_sentence_endings, count_punctuation_marks, analyze_text
import os

@pytest.fixture(scope="module")
def setup_file():
    file_path = 'example.txt'
    if not os.path.exists(file_path):
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write('Привіт! Це тестовий текст.')
    return file_path

# count_punctuation_marks
@pytest.mark.parametrize("text, expected", [
    ("Привіт! Це тестовий текст.", 2),
    ("Тест, який має кілька слів.", 2),
    ("", 0)
])
def test_count_punctuation_marks(text, expected):
    assert count_punctuation_marks(text) == expected

def test_analyze_text(setup_file):
    with patch('builtins.input', return_value=setup_file):
        analyze_text()
