a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
c = int(input("Введите третье число: "))

if a <= b and a <= c:
    min = a
elif b <= a and b <= c:
    min = b
else:
    min = c

print("Минимум:", min)