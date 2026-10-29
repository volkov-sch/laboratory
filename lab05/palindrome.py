text = input("Введите текст: ")

cleaned = text.lower().replace(" ", "")  # убираем только обычные пробелы

if cleaned == "":
    print("Нет текста")
elif cleaned == cleaned[::-1]:  # сравниваем с перевёрнутой строкой
    print("Палиндром")
else:
    print("Не палиндром")