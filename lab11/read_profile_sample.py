import json  # читаю учебный локальный пример
from pathlib import Path  # нахожу файл рядом со скриптом


def main():  # этот вариант запускаю, если интернет недоступен
    path = Path(__file__).resolve().parent / "profile_sample.json"  # выбираю локальный файл
    try:
        with open(path, "r", encoding="utf-8") as file:
            data = json.load(file)  # читаю JSON без сетевого запроса
        if not isinstance(data, dict) or not isinstance(data.get("login"), str):
            raise ValueError("В примере нет строкового логина")
        print("Использованы учебные локальные данные")  # явно указываю источник
        print("Логин:", data["login"])  # вывожу demo
    except (OSError, ValueError) as error:  # обрабатываю ошибки файла, кодировки и JSON
        print("Ошибка локального примера:", error)


if __name__ == "__main__":
    main()
