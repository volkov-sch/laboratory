x = float(input("Введите координаты x: "))
y = float(input("Введите координаты y: "))

if 0 <= x <= 5 and 0 <= y <= 3:
    print("Внутри или на границе")
else:
    print("Снаружи")