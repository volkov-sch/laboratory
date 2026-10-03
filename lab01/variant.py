order = input("Введите название заказа: ")
customer = input("Введите имя заказчика: ")
position1 = input("Введите название первой позиции: ")
quantity1 = int(input("Введите количество первой позиции: "))
price1 = float(input("Введите цену первой позиции: "))
position2 = input("Введите название второй позиции: ")
quantity2 = int(input("Введите количество второй позиции: "))
price2 = float(input("Введите цену второй позиции: "))
delivery = float(input("Введите стоимость доставки: "))
paid = float(input("Введите внесённую сумму: "))
cost1 = quantity1 * price1 # считаем стоимость первой позиции (кол-во 1 позиции * на цену)
cost2 = quantity2 * price2 # считаем стоимость второй позиции
goods = cost1 + cost2 # складываем стоимость товаров
total = goods + delivery # добавляем доставку
quantity = quantity1 + quantity2 # считаем общее количество товаров
change = paid - total # считаем сдачу

print()
print("-------ЗАКАЗ-------")
print("Заказ:", order)
print("Заказчик:", customer)
print("Первая позиция:", position1)
print("Количество:", quantity1)
print("Цена:", price1)
print("Стоимость:", cost1)
print("Вторая позиция:", position2)
print("Количество:", quantity2)
print("Цена:", price2)
print("Стоимость:", cost2)
print("Стоимость товаров:", goods)
print("Доставка:", delivery)
print("Итого:", total)
print("Количество товаров:", quantity)
print("Сдача:", change)
