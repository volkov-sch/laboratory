total = int(input("Введите количество секунд: "))
hours = total // 3600 # считаем часы
minutes = (total % 3600) // 60 # считаем минуты
seconds = total % 60 # считаем секунды

print()
print("Часов:", hours)
print("Минут:", minutes)
print("Секунд:", seconds)
print(hours, "ч", minutes, "мин", seconds, "с")