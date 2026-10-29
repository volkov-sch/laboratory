# Вариант 2. Слова, которые заканчиваются на я.
text = input("Введите текст: ")
count = 0

for word in text.split():
    word = word.strip(".,!?;:").lower()  # убираем знаки по краям слова
    if word == "":
        continue
    if word.endswith("я"):
        print(word)
        count = count + 1

if count == 0:
    print("Нет совпадений")

print("Количество:", count)