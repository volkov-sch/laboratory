from pathlib import Path
from tempfile import TemporaryDirectory
from files_lab import read_matrix, selected_sum


def check_error(path, text, expected):  # проверяю неправильный формат файла
    path.write_text(text, encoding="utf-8")  # записываю проверяемый пример
    try:
        read_matrix(path)  # пытаюсь прочитать неправильную таблицу
    except ValueError as error:
        assert expected in str(error)  # проверяю пояснение и номер строки
    else:
        assert False, "Ошибка не обнаружена"  # тест должен остановиться без исключения


folder = Path(__file__).resolve().parent  # временную папку создаю рядом с тестом
with TemporaryDirectory(dir=folder) as directory:  # тестовые файлы удалятся после проверок
    directory = Path(directory).resolve()
    assert directory.parent == folder  # проверяю, что временная папка находится внутри lab10
    path = directory / "matrix.txt"
    path.write_text("1 2\n7 -1\n", encoding="utf-8")
    assert read_matrix(path) == [[7, -1]]  # проверяю пример из методички
    path.write_text("1 1\n0", encoding="utf-8")
    assert read_matrix(path) == [[0]]  # последнего перевода строки может не быть
    path.write_text("2 3\n1 -2 3\n4 0 -6\n", encoding="utf-8")
    matrix = read_matrix(path)
    assert matrix == [[1, -2, 3], [4, 0, -6]]
    assert selected_sum(matrix) == -8  # проверяю свой вариант
    assert selected_sum([[0, 2, 5]]) == 0  # проверяю отсутствие отрицательных
    assert selected_sum([[-7]]) == -7  # проверяю одну ячейку

    check_error(path, "", "пустой")
    check_error(path, "0 3\n", "Строка 1")
    check_error(path, "1 0\n", "Строка 1")
    check_error(path, "x 3\n", "Строка 1")
    check_error(path, "1 2 3\n", "Строка 1")
    check_error(path, "1 2\n1\n", "Строка 2")
    check_error(path, "1 2\n1 x\n", "Строка 2")
    check_error(path, "1 1\n2\n3\n", "Строка 3")
    check_error(path, "1 1\n2\n\n", "Строка 3")  # лишняя пустая строка тоже ошибка
    check_error(path, "1 1\n\n", "Строка 2")
    check_error(path, "2 1\n2\n", "Строка 3")
    try:
        read_matrix(directory / "missing.txt")  # проверяю отсутствующий файл
    except FileNotFoundError:
        pass  # ожидаемая ошибка получена
    else:
        assert False, "Отсутствующий файл не обнаружен"
    path.write_bytes(b"\xff")  # создаю неправильную кодировку только во временном файле
    try:
        read_matrix(path)
    except UnicodeError:
        pass
    else:
        assert False, "Ошибка кодировки не обнаружена"

print("Все проверки файлов пройдены")
