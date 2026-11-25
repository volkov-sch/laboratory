import json  # разбираю ответ сервера и сохраняю его в JSON
import socket  # обрабатываю ошибку ожидания сетевого ответа
from pathlib import Path  # сохраняю результат рядом со скриптом
from urllib.error import HTTPError, URLError  # подключаю сетевые исключения
from urllib.parse import quote  # кодирую логин для адреса
from urllib.request import Request, urlopen  # создаю и выполняю запрос


def fetch_profile(login):  # получаю профиль GitHub по логину
    if not login.strip():  # не отправляю пустой логин
        raise ValueError("Логин не должен быть пустым")
    url = "https://api.github.com/users/" + quote(login.strip(), safe="")  # собираю адрес профиля
    request = Request(url, headers={  # по умолчанию это запрос GET для чтения
        "Accept": "application/vnd.github+json",  # прошу JSON
        "User-Agent": "python-course-lab11",  # указываю название учебной программы
    })
    with urlopen(request, timeout=10) as response:  # жду ответ не дольше заданного таймаута
        data = json.loads(response.read().decode("utf-8"))  # получаю текст и разбираю JSON
    if not isinstance(data, dict) or not isinstance(data.get("login"), str):  # проверяю вид ответа
        raise ValueError("Ответ не похож на профиль пользователя")
    return data  # возвращаю профиль, сохраняя в том числе значения null как None


def main():  # выполняю сетевое упражнение отдельно от анализа задач
    try:
        data = fetch_profile(input("Логин GitHub: "))  # ввожу логин и выполняю запрос
        output = Path(__file__).resolve().parent / "profile.json"  # выбираю файл результата
        with open(output, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=2)
        print(f"Профиль сохранён: {data['login']}")  # сообщаю об успехе после записи
    except HTTPError as error:  # сервер ответил кодом ошибки
        print(f"Сервер вернул HTTP {error.code}")
    except (URLError, TimeoutError, socket.timeout):  # ответ по сети получить не удалось
        print("Не удалось получить ответ по сети")
    except (ValueError, UnicodeError) as error:  # ответ или введённый логин некорректны
        print(f"Ошибка данных: {error}")
    except OSError as error:  # например, нельзя записать результат
        print(f"Ошибка доступа: {error}")


if __name__ == "__main__":  # импорт модуля не выполняет сетевой запрос
    main()
