firstroom = input("Введите первую аудиторию: ") 
secondroom = input("Введите вторую аудиторию: ") 

print("До обмена:")
print("Первая аудитория:", firstroom)
print("Вторая аудитория:", secondroom)

temp = firstroom # временно сохраняем первую аудиторию
firstroom = secondroom # первой аудитории присваиваем вторую
secondroom = temp # второй аудитории присваиваем первую

print("После обмена:")
print("Первая аудитория:", firstroom)
print("Вторая аудитория:", secondroom)
