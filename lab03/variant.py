value = int(input("Введите число от 0 до 100: "))

if value < 0 or value > 100:
    print("Ошибка диапазона")
elif value <= 49:
    print("Свободно")
elif value <= 89:
    print("Мало места")
else:
    print("Почти заполнено")