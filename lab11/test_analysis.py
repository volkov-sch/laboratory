import json
from pathlib import Path
from tempfile import TemporaryDirectory
from analysis import completion_counts, select_leader_tasks, select_tasks, top_users, validate_todos


def check_invalid(data):  # проверяю, что неправильная структура отклоняется
    try:
        validate_todos(data)
    except ValueError:
        pass
    else:
        assert False, "Ошибка структуры не обнаружена"


folder = Path(__file__).resolve().parent
with open(folder / "todos.json", "r", encoding="utf-8") as file:
    todos = json.load(file)  # беру точный учебный набор
validate_todos(todos)
saved = []
for task in todos:
    saved.append(task.copy())  # сохраняю исходные записи
assert completion_counts(todos) == {5: 2, 10: 2}
assert top_users(completion_counts(todos)) == [5, 10]  # проверяю несколько лидеров
selected = select_tasks(todos, 5)
ids = []
for task in selected:
    ids.append(task["id"])
assert ids == [1, 5]  # проверяю вариант 2
leader_tasks = select_leader_tasks(todos, top_users(completion_counts(todos)))
ids = []  # проверяю ID выборки лидеров и исходный порядок
for task in leader_tasks:
    ids.append(task["id"])
assert ids == [1, 3, 4, 5]
assert select_leader_tasks([], []) == []
assert select_tasks(todos, 999) == []  # проверяю неизвестного пользователя
assert completion_counts([]) == {}
assert top_users({}) == []
assert top_users({5: 0, 10: 0}) == []
assert top_users({10: 1, 5: 2}) == [5]  # проверяю единственного лидера
assert top_users({10: 2, 2: 2}) == [2, 10]  # ID сортируются как числа

unfinished = [{"id": 1, "userId": 7, "title": "Тест", "completed": False}]
assert completion_counts(unfinished) == {7: 0}  # пользователь с нулём не теряется
assert top_users(completion_counts(unfinished)) == []
assert select_leader_tasks(unfinished, []) == []  # без лидеров итоговая выборка пуста
assert select_tasks(unfinished, 7) == []  # непустой список без совпадений
assert todos == saved  # обработка не меняет исходные записи

check_invalid({})  # корень не список
check_invalid([5])  # запись не словарь
check_invalid([todos[0], todos[0].copy()])  # повторный ID
for key, value in [("id", True), ("id", 0), ("userId", False), ("userId", -1),
                   ("title", "   "), ("completed", "false")]:
    wrong = todos[0].copy()
    wrong[key] = value  # меняю только одну часть корректной записи
    check_invalid([wrong])
wrong = todos[0].copy()
del wrong["userId"]  # проверяю отсутствие обязательного ключа
check_invalid([wrong])
extra = todos[0].copy()
extra["note"] = "Дополнительный ключ допустим"
validate_todos([extra])

with TemporaryDirectory(dir=folder) as directory:  # проверяю сохранение в отдельной папке
    directory = Path(directory).resolve()
    assert directory.parent == folder
    for name, data in [("selected.json", selected), ("leaders.json", leader_tasks)]:
        path = directory / name
        with open(path, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=2)
        with open(path, "r", encoding="utf-8") as file:
            restored = json.load(file)
        assert restored == data  # обе выборки сохранили свою структуру
print("Все проверки JSON пройдены")
