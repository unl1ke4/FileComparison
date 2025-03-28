import re

def read_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print("Файл не знайдено. Переконайтеся, що ви ввели правильне ім'я.")
        return None
    
def analyze_text():
    file_path = input("Введіть ім'я файлу (з розширенням .txt): ").strip()
    text = read_file(file_path)
    
    if text is None:
        return  

    word_count = count_words(text)
    sentence_count = count_sentences(text)

    print(f"\nКількість слів: {word_count}")
    print(f"Кількість речень: {sentence_count}")

analyze_text()