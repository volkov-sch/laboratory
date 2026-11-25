import json  # отдельно обрабатываю ошибку синтаксиса JSON
from pathlib import Path  # нахожу data.json рядом с программой
from logic import add_record, delete_record, find_record, find_records, set_completed, statistics
from storage import load_records, save_records  # подключаю чтение и сохранение


def read_text(prompt):  # получаю непустой текст без краевых пробелов
    while True:
        text = input(prompt).strip()
        if text != "":
            return text
        print("Текст не должен быть пустым")


def read_integer(prompt, minimum=0):  # получаю целое число не меньше заданной границы
    while True:
        try:
            number = int(input(prompt))
        except ValueError:
            print("Нужно целое число")
        else:
            if number >= minimum:
                return number
            print("Число должно быть не меньше", minimum)


def read_status():  # пользователь явно выбирает новый статус
    while True:
        answer = input("Книга прочитана? 1 — да, 0 — нет: ").strip()
        if answer == "1":
            return True
        if answer == "0":
            return False
        print("Введите 1 или 0")


def record_id(record):  # эта функция сообщает sorted, по какому значению сортировать
    return record["id"]


def show_records(records):  # показываю книги по возрастанию ID
    if len(records) == 0:
        print("Нет записей")
        return
    for record in sorted(records, key=record_id):  # получаю отсортированный список без изменения исходного
        if record["completed"]:
            status = "прочитана"
        else:
            status = "не прочитана"
        print(record["id"], "|", record["title"], "|", record["category"].strip(),
              "|", record["amount"], "стр. |", status)


def show_statistics(records):  # вывожу показатели текущего списка
    result = statistics(records)
    print("Всего книг:", result["total"])
    print("Прочитано:", result["completed"])
    print("Не прочитано:", result["pending"])
    print("Всего страниц:", result["amount"])
    print("Страницы по категориям:")
    for category in sorted(result["by_category"]):  # категории показываю по алфавиту
        print(category + ":", result["by_category"][category])


def save_current(path, records):  # общее сохранение для команды меню и выхода
    try:
        save_records(path, records)
    except (OSError, ValueError, TypeError) as error:
        print("Не удалось сохранить данные:", error)
        return False  # при ошибке работа с текущим списком продолжается
    else:
        print("Данные сохранены")  # сообщаю об успехе только после записи
        return True


def main():  # все текущие записи храню в локальной переменной
    path = Path(__file__).resolve().parent / "data.json"
    try:
        records = load_records(path)
    except FileNotFoundError:
        records = []  # первый запуск без файла начинаю с пустого списка
        print("Файл data.json не найден. Начинаю с пустого списка.")
    except json.JSONDecodeError as error:  # этот обработчик ставлю перед ValueError
        print("Ошибка JSON:", error)
        return  # повреждённый файл не перезаписываю
    except UnicodeError:
        print("Ошибка кодировки data.json: нужен UTF-8")
        return
    except ValueError as error:
        print("Ошибка структуры данных:", error)
        return
    except OSError as error:
        print("Ошибка доступа к data.json:", error)
        return

    while True:  # показываю меню до команды выхода
        print("\nСписок книг для чтения")
        print("1 — Показать книги")
        print("2 — Добавить книгу")
        print("3 — Найти по названию")
        print("4 — Изменить статус")
        print("5 — Удалить книгу")
        print("6 — Статистика")
        print("7 — Сохранить")
        print("8 — Выйти")
        command = input("Выберите команду: ").strip()

        if command == "1":
            show_records(records)
        elif command == "2":
            title = read_text("Название книги: ")
            category = read_text("Категория: ")
            amount = read_integer("Количество страниц: ")
            record = add_record(records, title, category, amount)
            print("Книга добавлена. ID:", record["id"])
        elif command == "3":
            query = read_text("Часть названия: ")
            found = find_records(records, query)
            if len(found) == 0:
                print("Ничего не найдено")
            else:
                show_records(found)
        elif command == "4":
            book_id = read_integer("ID книги: ", 1)
            if find_record(records, book_id) is None:
                print("Книга с таким ID не найдена")
            else:
                completed = read_status()
                set_completed(records, book_id, completed)
                print("Статус изменён")
        elif command == "5":
            book_id = read_integer("ID книги: ", 1)
            if find_record(records, book_id) is None:
                print("Книга с таким ID не найдена")
            else:
                answer = input("Удалить книгу? Введите да для подтверждения: ").strip().lower()
                if answer == "да":
                    delete_record(records, book_id)
                    print("Книга удалена")
                else:
                    print("Удаление отменено")
        elif command == "6":
            show_statistics(records)
        elif command == "7":
            save_current(path, records)
        elif command == "8":
            while True:  # неправильный ответ повторяет вопрос о сохранении
                answer = input("Сохранить перед выходом? да/нет: ").strip().lower()
                if answer == "да":
                    if save_current(path, records):
                        return  # выхожу только после успешного сохранения
                    break  # при ошибке возвращаюсь в основное меню
                elif answer == "нет":
                    print("Выход без сохранения")
                    return
                else:
                    print("Введите да или нет")
        else:
            print("Неизвестная команда")  # повторяю меню после неправильного выбора


if __name__ == "__main__":
    main()
