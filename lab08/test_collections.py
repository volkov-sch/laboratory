from collections_lab import all_topics, common_topics, titles_in_category, totals_by_category, word_counts


assert word_counts("Python, python! SQL") == {"python": 2, "sql": 1}  # проверяю регистр и знаки
assert word_counts("!!!") == {}  # проверяю строку только из знаков
assert word_counts("") == {}  # проверяю пустой текст
assert word_counts("Я\tя;\nя") == {"я": 3}  # проверяю пробельные символы и повторы

first = ["python", "sql", "python"]  # создаю темы первого студента
second = ["sql", "git"]  # создаю темы второго студента
assert common_topics(first, second) == ["sql"]  # проверяю пересечение
assert all_topics(first, second) == ["git", "python", "sql"]  # проверяю объединение
assert common_topics([], second) == []  # проверяю пустой первый список
assert common_topics(first, []) == []  # проверяю пустой второй список
assert all_topics([], second) == ["git", "sql"]  # проверяю объединение с пустым списком
assert all_topics(first, []) == ["python", "sql"]  # проверяю удаление повторов
assert first == ["python", "sql", "python"]  # исходные темы не изменились

records = [
    {"title": "A", "category": "основное", "amount": 4},
    {"title": "B", "category": "дополнительное", "amount": 2},
    {"title": "C", "category": "основное", "amount": 3},
]
saved = []  # сохраняю копии всех записей
for record in records:
    saved.append(record.copy())
assert totals_by_category(records) == {"основное": 7, "дополнительное": 2}  # проверяю суммы
assert titles_in_category(records, "основное") == ["A", "C"]  # проверяю порядок названий
assert titles_in_category(records, "нет") == []  # проверяю неизвестную категорию
assert totals_by_category([]) == {}  # проверяю пустой набор
assert titles_in_category([], "основное") == []  # проверяю поиск в пустом наборе
assert records == saved  # функции не изменили исходные словари

books = [
    {"title": "Маленький принц", "category": "художественная", "amount": 3},
    {"title": "Изучаем Python", "category": "учебная", "amount": 4},
    {"title": "Атлас мира", "category": "справочная", "amount": 2},
    {"title": "Капитанская дочка", "category": "художественная", "amount": 5},
    {"title": "Алгебра", "category": "учебная", "amount": 1},
]
assert totals_by_category(books) == {"художественная": 8, "учебная": 5, "справочная": 2}
assert titles_in_category(books, "учебная") == ["Изучаем Python", "Алгебра"]
assert totals_by_category([{"title": "Книга", "category": "учебная", "amount": 0}]) == {"учебная": 0}
print("Все проверки коллекций пройдены")  # это сообщение появится после успешных assert
