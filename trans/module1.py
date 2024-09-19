import googletrans
from tabulate import tabulate

languages = googletrans.LANGUAGES
translator = googletrans.Translator()

def TransLate(src: str, lang: str) -> str:
    result = translator.translate(src, dest=lang)
    return result.text

def LangDetect(txt: str) -> str:
    detection = translator.detect(txt)
    return detection

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
            word = TransLate(text,code)
            table_data.append([i, language, code,word])

        headers = ["N", "Language", "ISO-639 code"]

        headers = ["N", "Language", "ISO-639 code"]
        if text:
            headers.append("Text")

        # Форматована таблиця
        table_str = tabulate(table_data, headers, tablefmt="plain", numalign="left", stralign="left")

        if out == "screen":
            print(table_str)
        elif out == "file":
            with open("languages_list.txt", "w", encoding="utf-8") as f:
                f.write(table_str)
        else:
            return "Error: Unsupported output option"

        return "Ok"
