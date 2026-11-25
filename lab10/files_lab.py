def read_matrix(path):  # читаю таблицу и проверяю весь формат
    with open(path, "r", encoding="utf-8") as file:  # исходник открываю только для чтения
        lines = file.readlines()  # получаю все строки файла
    if len(lines) == 0:  # проверяю пустой файл
        raise ValueError("Файл пустой")  # сообщаю об ошибке вызывающему коду

    header = lines[0].split()  # разбиваю заголовок на части
    if len(header) != 2:  # в заголовке должны быть два значения
        raise ValueError("Строка 1: нужно два размера таблицы")
    try:  # преобразование размеров может не получиться
        rows = int(header[0])  # получаю число строк
        columns = int(header[1])  # получаю число столбцов
    except ValueError:  # обрабатываю нечисловые размеры
        raise ValueError("Строка 1: размеры должны быть целыми числами")
    if rows <= 0 or columns <= 0:  # размеры должны быть положительными
        raise ValueError("Строка 1: размеры должны быть больше нуля")

    matrix = []  # создаю таблицу
    for index in range(rows):  # ожидаю ровно нужное количество строк данных
        line_number = index + 2  # учитываю заголовок и нумерацию с единицы
        if index + 1 >= len(lines):  # проверяю, не закончился ли файл раньше времени
            raise ValueError(f"Строка {line_number}: не хватает строки таблицы")
        parts = lines[index + 1].split()  # беру очередную строку после заголовка
        if len(parts) != columns:  # проверяю длину строки, в том числе пустую строку
            raise ValueError(f"Строка {line_number}: нужно ровно {columns} чисел")
        row = []  # создаю отдельный список для строки
        for part in parts:  # перебираю её ячейки
            try:  # проверяю, можно ли получить целое число
                number = int(part)  # преобразую ячейку
            except ValueError:  # сообщаю номер строки с неправильной ячейкой
                raise ValueError(f"Строка {line_number}: ячейки должны быть целыми числами")
            row.append(number)  # добавляю проверенное число
        matrix.append(row)  # добавляю готовую строку
    if len(lines) > rows + 1:  # после данных не должно быть лишних строк
        raise ValueError(f"Строка {rows + 2}: лишняя строка в файле")
    return matrix  # возвращаю только полностью проверенную таблицу


def selected_sum(matrix):  # вариант 2: сумма отрицательных элементов
    total = 0  # начинаю сумму с нуля
    for row in matrix:  # перебираю строки
        for number in row:  # перебираю ячейки
            if number < 0:  # выбираю отрицательные числа
                total = total + number  # добавляю их к сумме
    return total  # если совпадений нет, возвращаю ноль
