import re

def read_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print("Файл не знайдено. Переконайтеся, що ви ввели правильне ім'я.")
        return None

def count_words(text):
    words = re.findall(r'\b\w+\b', text)
    return len(words)

def count_sentences(text):
    sentences = re.split(r'[.!?]+(?:\s|$)', text)
    return len([s for s in sentences if s.strip()])

def count_sentence_endings(text):
    endings = re.findall(r'\.\.\.|[.!?]', text)
    return len(endings)

def display_text(text):
    print("\nТекст з файлу:")
    print(text)

def analyze_text():
    file_path = input("Введіть ім'я файлу (з розширенням .txt): ").strip()
    text = read_file(file_path)
    
    if text is None:
        return  
    
    display_text(text)

    word_count = count_words(text)
    sentence_count = count_sentences(text)
    ending_count = count_sentence_endings(text)

    print(f"\nКількість слів: {word_count}")
    print(f"Кількість речень: {sentence_count}")
    print(f"Кількість символів, що закінчують речення: {ending_count}")

analyze_text()
