from table import column_sums, diagonal_pattern, row_sums, transform


matrix = [[1, 2, 3], [4, 5, 6]]  # специально беру прямоугольную таблицу 2 на 3
assert row_sums(matrix) == [6, 15]  # проверяю суммы строк
assert column_sums(matrix) == [5, 7, 9]  # проверяю все три столбца
assert matrix == [[1, 2, 3], [4, 5, 6]]  # суммы не изменили таблицу
assert row_sums([[7]]) == [7]  # проверяю одну ячейку
assert column_sums([[7]]) == [7]
assert row_sums([[1], [-1], [0]]) == [1, -1, 0]  # проверяю три строки и один столбец
assert column_sums([[1], [-1], [0]]) == [0]
assert row_sums([]) == []  # проверяю пустую таблицу
assert column_sums([]) == []
assert transform([]) == []

assert diagonal_pattern(1) == [[0]]  # проверяю минимальный размер
pattern = diagonal_pattern(3)  # создаю узор из примера
assert pattern == [[0, 1, 1], [2, 0, 1], [2, 2, 0]]
pattern[0][0] = 9  # меняю только первую строку
assert pattern[1][0] == 2  # остальные строки должны быть независимыми
assert pattern[2][0] == 2

matrix = [[-2, 0, 3], [4, -5, 6]]  # контрольная таблица варианта 2
saved = []  # сохраняю отдельные копии строк
for row in matrix:
    saved.append(row.copy())
result = transform(matrix)  # заменяю положительные числа единицами
assert result == [[-2, 0, 1], [1, -5, 1]]
assert matrix == saved  # проверяю сохранность исходной матрицы
result[0][0] = 100  # меняю результат
assert matrix == saved  # исходная таблица не должна измениться
assert result[1] == [1, -5, 1]  # строки результата тоже независимы
assert transform([[0, -1]]) == [[0, -1]]  # проверяю набор без положительных чисел
assert transform([[7]]) == [[1]]
print("Все проверки таблиц пройдены")
