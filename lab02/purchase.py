price = int(input("Введите цену одной тетради: "))
count = int(input("Введите количество тетрадей: "))
paid = int(input("Введите переданную сумму: "))

cost = price * count # считаем стоимость покупки
change = paid - cost # считаем сдачу

print()
print("Стоимость:", cost)
print("Сдача:", change)