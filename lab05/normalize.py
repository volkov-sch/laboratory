text = input("Введите текст: ")

words = text.split()  # разбиваю текст на слова
normalized = " ".join(words)  # соединяю слова одним пробелом

print("Исходная длина:", len(text))
print("Новая длина:", len(normalized))
print("Нормализованный текст:", normalized)
print("Количество слов:", len(words))