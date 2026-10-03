surname = input("Введите свою фамилию: ") 
name = input("Введите своё имя: ") 
group = input("Введите свою группу: ") 
city = input("Введите ваш город: ") 
age = int(input("Введите ваш возраст: ")) 
subject = input("Введите свой любимый предмет: ") 
studTime = float(input("Введите часы подготовки в неделю: ")) 

age4 = age + 4 # возраст через 4 года
month = studTime * 4 # подготовка за 4 недели
day = studTime / 7 # подготовка за один день

print()
print("-------КАРТОЧКА СТУДЕНТА-------")
print("Имя:", name, surname)
print("Группа:", group)
print("Город:", city)
print("Возраст через 4 года:", age4)
print("Любимый предмет:", subject)
print("Подготовка за 4 недели:", month)
print("Подготовка в день:", day)
