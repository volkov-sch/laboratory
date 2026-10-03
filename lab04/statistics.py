n = int(input("Введите количество чисел: "))
number = int(input("Введите число: "))

total = number # начальная сумма
positive = 0 # количество положительных чисел

if number > 0:
    positive = 1
maximum = number # первое число считаем максимумом

for i in range(1, n):
    number = int(input("Введите число: "))
    total = total + number # добавляем число к сумме
    if number > 0:
        positive = positive + 1 # увеличиваем количество положительных
    if number > maximum:
        maximum = number # запоминаем новое максимальное число

print()
print("Сумма:", total)
print("Положительных чисел:", positive)
print("Максимум:", maximum)