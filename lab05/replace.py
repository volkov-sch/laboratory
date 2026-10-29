text = input("Введите текст: ")

count = text.count(":")  # считаем двоеточия до замены
new_text = text.replace(":", "-")

print("Количество замен:", count)
print("Новая строка:", new_text)