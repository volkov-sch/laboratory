total = int(input("Введите количество книг: "))

capacity = int(input("Введите количество книг в одной коробке: "))

full = total // capacity # считаем количество полных коробок

rest = total % capacity # считаем остаток книг

boxes = (total + capacity - 1) // capacity # считаем общее количество коробок

print()

print("Полных коробок:", full)

print("Остаток книг:", rest)

print("Всего коробок:", boxes)
