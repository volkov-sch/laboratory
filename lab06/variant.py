# Вариант 2. Отрицательные числа.
numbers = []
for part in input("Введите целые числа через пробел: ").split():
    numbers.append(int(part))

selected = []
for number in numbers:
    if number < 0:
        selected.append(number)

sorted_numbers = sorted(selected)  # получаем новую отсортированную копию

print("Отрицательные числа:", selected)
print("Количество:", len(selected))
print("Сумма:", sum(selected))
print("Отсортированная копия:", sorted_numbers)