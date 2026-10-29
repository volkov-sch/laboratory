numbers = []
for part in input("Введите целые числа через пробел: ").split():
    numbers.append(int(part))

new_numbers = []  # создаём отдельный список
for number in numbers:
    new_numbers.append(abs(number))

print("Исходный список:", numbers)
print("Новый список:", new_numbers)