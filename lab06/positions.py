numbers = []
for part in input("Введите целые числа через пробел: ").split():
    numbers.append(int(part))

if len(numbers) == 0:
    print("Нет данных")
else:
    maximum = max(numbers)
    positions = []
    for index, number in enumerate(numbers):  # индексы начинаются с нуля
        if number == maximum:
            positions.append(index)
    print("Индексы максимума:", positions)
