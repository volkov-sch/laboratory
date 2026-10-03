number = int(input("Введите положительное число: "))
attempts = 0

while number <= 0:
    attempts += 1
    number = int(input("Введите положительное число: "))

print("Квадрат:", number * number)
print("Отклонено:", attempts)