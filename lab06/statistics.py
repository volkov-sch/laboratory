numbers = []
for part in input("Введите целые числа через пробел: ").split():
    numbers.append(int(part))  # добавляем число в список

if len(numbers) == 0:
    print("Нет данных")
else:
    average = sum(numbers) / len(numbers)
    print("Количество:", len(numbers))
    print("Сумма:", sum(numbers))
    print("Минимум:", min(numbers))
    print("Максимум:", max(numbers))
    print("Среднее:", format(average, ".2f"))