def validate_todos(data):  # проверяю структуру всего учебного набора
    if not isinstance(data, list):  # корнем должен быть список
        raise ValueError("Корень JSON должен быть списком")
    ids = set()  # сохраняю уже встреченные идентификаторы
    for index, task in enumerate(data):  # перебираю записи и их позиции
        if not isinstance(task, dict):  # каждая запись должна быть словарём
            raise ValueError(f"Запись {index + 1}: нужен словарь")
        task_id = task.get("id")  # получаю ID задачи
        user_id = task.get("userId")  # получаю ID пользователя
        if type(task_id) is not int or task_id <= 0:  # bool вместо числа не принимаю
            raise ValueError(f"Запись {index + 1}: id должен быть положительным целым")
        if task_id in ids:  # проверяю уникальность ID
            raise ValueError(f"Повторный id: {task_id}")
        ids.add(task_id)  # запоминаю ID
        if type(user_id) is not int or user_id <= 0:  # проверяю тип и диапазон userId
            raise ValueError(f"Запись {index + 1}: userId должен быть положительным целым")
        title = task.get("title")  # получаю название задачи
        if not isinstance(title, str) or title.strip() == "":  # название не должно быть пустым
            raise ValueError(f"Запись {index + 1}: нужно непустое название")
        if type(task.get("completed")) is not bool:  # статус должен быть именно логическим
            raise ValueError(f"Запись {index + 1}: completed должен быть bool")


def completion_counts(todos):  # считаю выполненные задачи всех пользователей
    counts = {}  # создаю словарь количества
    for task in todos:  # перебираю задачи
        user_id = task["userId"]  # сохраняю числовой ID пользователя
        counts[user_id] = counts.get(user_id, 0)  # учитываю пользователя даже с нулём выполненных
        if task["completed"]:  # проверяю статус задачи
            counts[user_id] = counts[user_id] + 1  # увеличиваю количество выполненных
    return counts  # возвращаю результат


def top_users(counts):  # нахожу всех лидеров
    if len(counts) == 0:  # отдельно проверяю отсутствие пользователей
        return []
    maximum = max(counts.values())  # нахожу наибольшее число завершённых задач
    if maximum == 0:  # без выполненных задач лидеров нет
        return []
    leaders = []  # создаю список лидеров
    for user_id in sorted(counts):  # сортирую числовые идентификаторы
        if counts[user_id] == maximum:  # проверяю достижение максимума
            leaders.append(user_id)  # сохраняю всех с одинаковым результатом
    return leaders


def select_leader_tasks(todos, leaders):  # отдельно выбираю завершённые задачи лидеров
    selected = []  # создаю новый список
    for task in todos:  # сохраняю исходный порядок
        if task["userId"] in leaders and task["completed"]:
            selected.append(task)  # незавершённые задачи сюда не попадают
    return selected


def select_tasks(todos, user_id, parameter=None):  # вариант 2, дополнительный параметр не нужен
    selected = []  # создаю выборку
    for task in todos:  # сохраняю исходный порядок задач
        if task["userId"] == user_id and task["completed"]:  # выбираю выполненные задачи пользователя
            selected.append(task)  # добавляю подходящую запись без её изменения
    return selected  # неизвестный пользователь даст пустой список
