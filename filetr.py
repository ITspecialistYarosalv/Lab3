import os
from configparser import ConfigParser
from trans.module2 import TransLate,LangDetect
import re

def count_sentences(text):
    sentences = re.split(r'[.!?]+', text)
    return len(sentences) if sentences[-1] else len(sentences) - 1

def count_words(text):
    words = text.split()
    return len(words)

def read_config():
    config = ConfigParser()
    config.read('config.ini')
    return config

def main():
        config = read_config()

        # Читання налаштувань із конфігураційного файлу
        text_file = config['Settings']['text_file']
        target_language = config['Settings']['target_language']
        output = config['Settings']['output']
        max_chars = int(config['Settings']['max_chars'])
        max_words = int(config['Settings']['max_words'])
        max_sentences = int(config['Settings']['max_sentences'])

        if not os.path.exists(text_file):
            print(f"Error: File {text_file} not found.")
            return

        with open(text_file, 'r', encoding='utf-8') as f:
            text = f.read()
        file_size = os.path.getsize(text_file)
        char_count = len(text)
        word_count = count_words(text)
        sentence_count = count_sentences(text)

        print(f"File: {text_file}")
        print(f"Size: {file_size} bytes")
        print(f"Characters: {char_count}")
        print(f"Words: {word_count}")
        print(f"Sentences: {sentence_count}")
        print(f"Language: {LangDetect(text)}")

        if char_count > max_chars:
            text = text[:max_chars]
        elif word_count > max_words:
            words = text.split()[:max_words]
            text = ' '.join(words)
        elif sentence_count > max_sentences:
            sentences = re.split(r'(?<=[.!?]) ', text)[:max_sentences]
            text = ' '.join(sentences)

        # Переклад тексту
        translated_text = TransLate(text, target_language)

        # Виведення результату на екран або у файл
        if output == 'screen':
            print(f"Translated to {target_language}:")
            print(translated_text)
        elif output == 'file':
            output_file = f"{os.path.splitext(text_file)[0]}_{target_language}.txt"
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(translated_text)
            print("Ok")


main()