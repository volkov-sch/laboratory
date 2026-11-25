def validate_records(records):
    """Проверяю весь список без изменений. При ошибке вызываю ValueError."""
    if not isinstance(records, list):  # корнем JSON должен быть список
        raise ValueError("Корень JSON должен быть списком")
    ids = set()  # собираю использованные ID
    for index, record in enumerate(records):  # проверяю каждую запись
        if not isinstance(record, dict):
            raise ValueError(f"Запись {index + 1}: нужен словарь")
        for key in ["id", "title", "category", "amount", "completed"]:  # обязательные поля
            if key not in record:
                raise ValueError(f"Запись {index + 1}: нет поля {key}")
        record_id = record["id"]  # получаю идентификатор книги
        if type(record_id) is not int or record_id <= 0:  # не принимаю bool вместо числа
            raise ValueError(f"Запись {index + 1}: id должен быть положительным целым")
        if record_id in ids:  # не допускаю повторных ID
            raise ValueError(f"Повторный id: {record_id}")
        ids.add(record_id)  # запоминаю проверенный ID
        for key in ["title", "category"]:  # проверяю два текстовых поля
            if not isinstance(record[key], str) or record[key].strip() == "":
                raise ValueError(f"Запись {index + 1}: поле {key} должно быть непустой строкой")
        if type(record["amount"]) is not int or record["amount"] < 0:  # страницы — целое неотрицательное
            raise ValueError(f"Запись {index + 1}: amount должен быть целым не меньше нуля")
        if type(record["completed"]) is not bool:  # статус должен быть строго логическим
            raise ValueError(f"Запись {index + 1}: completed должен быть bool")


def add_record(records, title, category, amount):
    """Добавляю книгу в список и возвращаю новую запись. При неверных полях список сохраняется."""
    if not isinstance(title, str) or title.strip() == "":  # сначала проверяю все новые данные
        raise ValueError("Название не должно быть пустым")
    if not isinstance(category, str) or category.strip() == "":
        raise ValueError("Категория не должна быть пустой")
    if type(amount) is not int or amount < 0:
        raise ValueError("Количество страниц должно быть целым не меньше нуля")
    new_id = 1  # для пустого списка начинаю с единицы
    for record in records:  # ищу число на один больше максимального существующего ID
        if record["id"] >= new_id:
            new_id = record["id"] + 1
    new_record = {  # собираю словарь новой книги
        "id": new_id,
        "title": title.strip(),  # убираю пробелы по краям
        "category": category.strip(),
        "amount": amount,
        "completed": False,  # новая книга ещё не прочитана
    }
    records.append(new_record)  # добавляю книгу только после проверки полей
    return new_record  # возвращаю запись, чтобы показать её ID


def find_record(records, record_id):
    """Возвращаю запись по ID или None. Список не меняю."""
    for record in records:  # перебираю книги
        if record["id"] == record_id:  # ищу точное совпадение ID
            return record
    return None  # нужной записи нет


def find_records(records, query):
    """Возвращаю список совпадений без изменения данных. Пустой запрос вызывает ValueError."""
    if not isinstance(query, str) or query.strip() == "":
        raise ValueError("Поисковый запрос не должен быть пустым")
    query = query.strip().lower()  # поиск выполняю без учёта регистра
    result = []
    for record in records:
        if query in record["title"].lower():  # ищу подстроку названия
            result.append(record)
    return result


def set_completed(records, record_id, completed):
    """Меняю статус найденной записи. Возвращаю True при успехе, False для неизвестного ID."""
    if type(completed) is not bool:  # нельзя случайно передать строку вместо статуса
        raise ValueError("Статус должен быть bool")
    record = find_record(records, record_id)
    if record is None:
        return False
    record["completed"] = completed  # явно устанавливаю выбранный статус
    return True


def delete_record(records, record_id):
    """Удаляю запись из списка. Возвращаю True при успехе, False для неизвестного ID."""
    record = find_record(records, record_id)
    if record is None:
        return False
    records.remove(record)  # удаляю только найденную книгу
    return True  # остальные идентификаторы не меняю


def statistics(records):
    """Возвращаю статистику текущего списка. Исходные записи не меняю."""
    completed = 0  # считаю прочитанные книги
    amount = 0  # суммирую страницы всех книг
    by_category = {}  # собираю суммы страниц по категориям
    for record in records:
        if record["completed"]:
            completed = completed + 1
        amount = amount + record["amount"]
        category = record["category"].strip()  # сравниваю категории после удаления краевых пробелов
        by_category[category] = by_category.get(category, 0) + record["amount"]
    return {
        "total": len(records),
        "completed": completed,
        "pending": len(records) - completed,
        "amount": amount,
        "by_category": by_category,
    }
