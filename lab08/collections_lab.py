def word_counts(text):  # считаю, сколько раз встретилось каждое слово
    counts = {}  # создаю словарь частот
    for word in text.lower().split():  # делаю буквы маленькими и перебираю слова
        word = word.strip(".,!?;:")  # убираю знаки по краям слова
        if word != "":  # пропускаю пустые результаты
            counts[word] = counts.get(word, 0) + 1  # увеличиваю частоту слова
    return counts  # возвращаю словарь


def print_counts(counts):  # вывожу частоты отдельной функцией
    for word in sorted(counts):  # перебираю ключи по алфавиту
        print(word + ":", counts[word])  # вывожу слово и его частоту


def common_topics(first, second):  # нахожу общие темы
    return sorted(set(first) & set(second))  # убираю повторы и сортирую пересечение


def all_topics(first, second):  # нахожу все уникальные темы
    return sorted(set(first) | set(second))  # объединяю множества и сортирую результат


def totals_by_category(records):  # считаю экземпляры книг по категориям
    totals = {}  # создаю словарь сумм
    for record in records:  # перебираю записи, не меняя их
        category = record["category"]  # получаю категорию книги
        totals[category] = totals.get(category, 0) + record["amount"]  # добавляю количество
    return totals  # возвращаю суммы


def titles_in_category(records, category):  # ищу названия в нужной категории
    titles = []  # создаю список результата
    for record in records:  # сохраняю порядок исходных записей
        if record["category"] == category:  # сравниваю категории точно
            titles.append(record["title"])  # добавляю название
    return titles  # неизвестная категория даст пустой список


def main():  # показываю работу всех заданий
    text = input("Введите текст: ")  # ввожу текст для подсчёта слов
    print("Частоты слов:")  # вывожу заголовок
    print_counts(word_counts(text))  # считаю и вывожу частоты

    first = input("Темы первого студента маленькими буквами: ").split()  # ввожу первый список
    second = input("Темы второго студента маленькими буквами: ").split()  # ввожу второй список
    print("Общие темы:", common_topics(first, second))  # вывожу пересечение
    print("Все темы:", all_topics(first, second))  # вывожу объединение

    record = {"title": "Python", "hours": 4}  # создаю запись со строковыми ключами
    record["hours"] = 6  # меняю существующее значение
    record["completed"] = False  # добавляю новый ключ
    pair = (record["title"], record["hours"])  # создаю кортеж из двух значений
    title, hours = pair  # распаковываю пару в две переменные
    print("Запись:", record)  # вывожу словарь
    print("Пара:", title, hours)  # вывожу распакованные значения

    # Вариант 2. В amount храню количество экземпляров книги.
    records = [
        {"title": "Маленький принц", "category": "художественная", "amount": 3},
        {"title": "Изучаем Python", "category": "учебная", "amount": 4},
        {"title": "Атлас мира", "category": "справочная", "amount": 2},
        {"title": "Капитанская дочка", "category": "художественная", "amount": 5},
        {"title": "Алгебра", "category": "учебная", "amount": 1},
    ]
    totals = totals_by_category(records)  # получаю суммы по трём категориям
    print("Экземпляры по категориям:")  # вывожу заголовок сводки
    for category in sorted(totals):  # сортирую названия категорий
        print(category + ":", totals[category])  # вывожу сумму категории
    category = input("Введите категорию книг: ").strip()  # ввожу категорию для поиска
    print("Названия:", titles_in_category(records, category))  # вывожу найденные книги


if __name__ == "__main__":  # запускаю диалог только при прямом запуске файла
    main()  # вызываю основную функцию
