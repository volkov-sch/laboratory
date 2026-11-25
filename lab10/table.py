def row_sums(matrix):  # нахожу суммы строк без изменения таблицы
    result = []  # создаю список сумм
    for row in matrix:  # перебираю строки
        result.append(sum(row))  # добавляю сумму очередной строки
    return result  # для пустой матрицы вернётся пустой список


def column_sums(matrix):  # нахожу суммы столбцов
    if len(matrix) == 0:  # отдельно проверяю пустую таблицу
        return []  # у неё нет столбцов
    result = []  # создаю список сумм
    for column in range(len(matrix[0])):  # беру реальное количество столбцов
        total = 0  # начинаю сумму столбца с нуля
        for row in matrix:  # перебираю все строки
            total = total + row[column]  # добавляю элемент нужного столбца
        result.append(total)  # сохраняю сумму столбца
    return result  # возвращаю все суммы


def diagonal_pattern(size):  # создаю квадратный узор положительного размера
    matrix = []  # создаю внешний список
    for row in range(size):  # перебираю индексы строк
        new_row = []  # для каждой строки создаю отдельный список
        for column in range(size):  # перебираю индексы столбцов
            if row == column:  # проверяю главную диагональ
                new_row.append(0)  # на диагонали ставлю ноль
            elif row < column:  # проверяю область выше диагонали
                new_row.append(1)  # выше ставлю единицу
            elif row > column:  # проверяю область ниже диагонали
                new_row.append(2)  # ниже ставлю двойку
        matrix.append(new_row)  # добавляю готовую независимую строку
    return matrix  # возвращаю узор


def transform(matrix):  # вариант 2: положительные числа заменяю единицами
    result = []  # создаю новую таблицу
    for row in matrix:  # перебираю исходные строки
        new_row = []  # создаю отдельную строку результата
        for number in row:  # перебираю элементы строки
            if number > 0:  # проверяю положительность
                new_row.append(1)  # заменяю положительное число единицей
            else:  # нули и отрицательные оставляю прежними
                new_row.append(number)  # копирую исходное значение
        result.append(new_row)  # добавляю новую строку
    return result  # исходная таблица не меняется
