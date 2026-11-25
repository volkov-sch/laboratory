import json  # читаю и записываю формат JSON
from pathlib import Path  # нахожу файлы рядом с программой
from analysis import completion_counts, select_leader_tasks, select_tasks, top_users, validate_todos  # подключаю обработку


def read_user_id():  # ввожу положительный целый ID с повтором при ошибке
    while True:
        try:
            user_id = int(input("Введите положительный ID пользователя: "))
        except ValueError:
            print("Нужно целое число")
        else:
            if user_id > 0:  # ноль и отрицательные ID не подходят
                return user_id
            print("ID должен быть больше нуля")


def main():  # выполняю локальную обработку JSON
    folder = Path(__file__).resolve().parent  # использую папку скрипта
    try:
        with open(folder / "todos.json", "r", encoding="utf-8") as file:  # читаю входные данные
            todos = json.load(file)  # разбираю JSON
        validate_todos(todos)  # проверяю весь набор до записи результатов
        counts = completion_counts(todos)  # считаю завершённые задачи
        leaders = top_users(counts)  # нахожу лидеров
        leader_tasks = select_leader_tasks(todos, leaders)  # выбираю только завершённые задачи лидеров
        for user_id in sorted(counts):  # вывожу пользователей по числовому ID
            print("Пользователь", user_id, "— выполнено:", counts[user_id])
        print("Лидеры:", leaders)
        user_id = read_user_id()  # отдельно ввожу ID для индивидуального варианта
        selected = select_tasks(todos, user_id)  # выбираю выполненные задачи пользователя
        with open(folder / "leaders.json", "w", encoding="utf-8") as file:  # вход уже проверен
            json.dump(leader_tasks, file, ensure_ascii=False, indent=2)  # сохраняю читаемую кириллицу
        with open(folder / "selected.json", "w", encoding="utf-8") as file:
            json.dump(selected, file, ensure_ascii=False, indent=2)  # сохраняю свой вариант
    except FileNotFoundError:
        print("Файл todos.json не найден")
    except json.JSONDecodeError as error:  # ставлю этот обработчик раньше общего ValueError
        print("Ошибка JSON:", error)
    except UnicodeError:
        print("Ошибка кодировки: нужен UTF-8")
    except ValueError as error:
        print("Ошибка структуры:", error)
    except OSError as error:
        print("Ошибка доступа к файлу:", error)
    else:
        print("Результаты сохранены в leaders.json и selected.json")  # подтверждаю успешную запись


if __name__ == "__main__":  # не запускаю ввод при импорте тестами
    main()
