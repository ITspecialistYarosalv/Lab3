from deep_translator import GoogleTranslator
from langdetect import detect
from tabulate import tabulate
# Створюємо екземпляр перекладача
translator_instance = GoogleTranslator(source='auto', target='en')

# Отримуємо список підтримуваних мов через екземпляр
languages = translator_instance.get_supported_languages(as_dict=True)

def TransLate(src: str, lang: str) -> str:
        result = GoogleTranslator(source='auto', target=lang).translate(src)
        return result

def LangDetect(txt: str) -> str:
        lang = detect(txt)
        return lang

def CodeLang(code: str) -> str:
    for key, val in languages.items():
        if code == val:
            return f"The language code is - {key}"
        elif code == key:
            return f"The language name is - {val}"
    return "Language not found"

def LanguageList(out: str = "screen", text: str = "") -> str:
        table_data = []
        for i, (code, language) in enumerate(languages.items(), start=1):
            translated_word = TransLate(text, code) if text else ""
            table_data.append([i, language, code, translated_word])

        headers = ["N", "Language", "ISO-639 code"]
        if text:
            headers.append("Text")

        table_str = tabulate(table_data, headers, tablefmt="plain", numalign="left", stralign="left")

        if out == "screen":
            print(table_str)
        elif out == "file":
            with open("languages_list.txt", "w", encoding="utf-8") as f:
                f.write(table_str)
        else:
            return "Error: Unsupported output option"

        return "Ok"

