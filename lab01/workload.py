subject1 = input("Введите первый предмет: ")
lessons1 = int(input("Введите количество занятий по первому предмету: "))
minutes1 = int(input("Введите продолжительность одного занятия: "))
subject2 = input("Введите второй предмет: ")
lessons2 = int(input("Введите количество занятий по второму предмету: "))
minutes2 = int(input("Введите продолжительность одного занятия: "))
available = float(input("Введите доступное время в неделю: "))

time1 = lessons1 * minutes1  # сколько минут занимает первый предмет
time2 = lessons2 * minutes2  # сколько минут занимает второй предмет
total = time1 + time2  # складываем время обоих предметов
hours = total / 60  # переводим минуты в часы
free = available - hours  # считаем свободное время
month = hours * 4  # считаем нагрузку за 4 недели

print()
print("Предмет:", subject1)
print("Время:", time1, "мин.")
print("Предмет:", subject2)
print("Время:", time2, "мин.")
print("Общая нагрузка:", total, "мин.")
print("Общая нагрузка: {:.2f} ч.".format(hours))
print("Свободное время: {:.2f} ч.".format(free)) 
print("Нагрузка за 4 недели: {:.2f} ч.".format(month))