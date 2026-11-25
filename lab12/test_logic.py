from logic import add_record, delete_record, find_record, find_records, set_completed, statistics, validate_records


def copy_records(records):  # делаю копии словарей для проверки сохранности
    result = []
    for record in records:
        result.append(record.copy())
    return result


def check_invalid(records):  # проверяю неправильную структуру набора
    try:
        validate_records(records)
    except ValueError:
        pass
    else:
        assert False, "Неправильные записи приняты"


records = []
validate_records(records)
assert statistics(records) == {"total": 0, "completed": 0, "pending": 0, "amount": 0, "by_category": {}}
assert find_records(records, "книга") == []
assert find_record(records, 1) is None
assert set_completed(records, 1, True) is False
assert delete_record(records, 1) is False

first = add_record(records, "  Python  ", "  учёба  ", 4)  # проверяю очистку текста
assert first == {"id": 1, "title": "Python", "category": "учёба", "amount": 4, "completed": False}
second = add_record(records, "Python", "учёба", 2)  # одинаковое название разрешено
assert second["id"] == 2
assert set_completed(records, 2, True) is True
assert statistics(records) == {"total": 2, "completed": 1, "pending": 1, "amount": 6, "by_category": {"учёба": 6}}
assert find_records(records, "PY") == records  # поиск не учитывает регистр
assert find_records(records, "нет совпадений") == []
assert set_completed(records, 2, False) is True  # статус можно явно вернуть обратно
assert second["completed"] is False
set_completed(records, 2, True)
third = add_record(records, "Атлас", "справочная", 10)  # добавляю вторую категорию
assert statistics(records)["by_category"] == {"учёба": 6, "справочная": 10}
saved = copy_records(records)
find_records(records, "python")  # поиск должен быть без изменений
statistics(records)  # статистика тоже не меняет записи
assert records == saved
assert set_completed(records, 999, True) is False
assert delete_record(records, 999) is False
assert records == saved  # неизвестный ID не меняет данные

assert delete_record(records, 1) is True
assert records[0]["id"] == 2  # после удаления ID не перенумеровываются
assert add_record(records, "Новая", "учёба", 0)["id"] == 4  # новый ID больше максимального

two = []  # отдельно проверяю точный сценарий из методички
add_record(two, "Первая", "учёба", 4)
add_record(two, "Вторая", "учёба", 2)
delete_record(two, 1)
assert two[0]["id"] == 2
assert add_record(two, "Третья", "учёба", 1)["id"] == 3

valid = {"id": 1, "title": "Книга", "category": "учёба", "amount": 4, "completed": False}
check_invalid({})
check_invalid(["книга"])
check_invalid([valid, valid.copy()])  # повторный идентификатор
for key in valid:  # проверяю отсутствие каждого обязательного ключа
    wrong = valid.copy()
    del wrong[key]
    check_invalid([wrong])
for key, value in [("id", True), ("id", 0), ("id", 1.0), ("title", " "),
                   ("category", ""), ("amount", True), ("amount", -1),
                   ("amount", 2.5), ("completed", "false"), ("completed", 0)]:
    wrong = valid.copy()
    wrong[key] = value
    check_invalid([wrong])
extra = valid.copy()
extra["note"] = "Дополнительное поле"
validate_records([extra])  # дополнительные поля допустимы
trimmed = valid.copy()
trimmed["category"] = " учёба "
assert statistics([valid, trimmed])["by_category"] == {"учёба": 8}

for title, category, amount in [(" ", "учёба", 1), ("Книга", "", 1),
                                 ("Книга", "учёба", -1), ("Книга", "учёба", True)]:
    saved = copy_records(records)
    try:
        add_record(records, title, category, amount)
    except ValueError:
        pass
    else:
        assert False, "Неверная книга добавлена"
    assert records == saved  # неуспешное добавление не меняет список
try:
    find_records(records, "   ")
except ValueError:
    pass
else:
    assert False, "Пустой поиск разрешён"
try:
    set_completed(records, 2, "да")
except ValueError:
    pass
else:
    assert False, "Строка принята вместо bool"
print("Все проверки логики проекта пройдены")
