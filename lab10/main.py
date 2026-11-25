from pathlib import Path  # использую пути относительно папки программы
from files_lab import read_matrix, selected_sum  # подключаю чтение и вариант
from table import column_sums, row_sums  # подключаю функции девятой лабораторной


def read_positive_integer():  # повторяю ввод положительного целого числа
    while True:  # выхожу из цикла только после правильного значения
        try:  # преобразование введённого текста может вызвать ошибку
            number = int(input("Введите положительный размер: "))  # ввожу целое число
        except ValueError:  # текст не удалось преобразовать
            print("Это не целое число")  # отличаю ошибку типа ввода от ошибки диапазона
        else:  # число успешно получено
            if number <= 0:  # проверяю положительность
                print("Число должно быть больше нуля")
            else:  # число подходит
                return number  # возвращаю его и заканчиваю ввод


def numbers_text(numbers):  # оформляю список чисел для отчёта
    parts = []  # создаю список строк
    for number in numbers:  # перебираю числа
        parts.append(str(number))  # преобразую их в строки
    return " ".join(parts)  # соединяю одним пробелом


def main():  # выполняю задания лабораторной
    number = read_positive_integer()  # показываю работу надёжного ввода размера
    print("Принятый размер:", number)  # размер из первого задания не меняет файл таблицы
    folder = Path(__file__).resolve().parent  # получаю папку скрипта
    try:  # обрабатываю ошибки чтения, проверки и записи
        matrix = read_matrix(folder / "matrix.txt")  # читаю и проверяю все данные
        rows = row_sums(matrix)  # вычисляю суммы строк
        columns = column_sums(matrix)  # вычисляю суммы столбцов
        result = selected_sum(matrix)  # вычисляю сумму отрицательных элементов
        report = "Суммы строк: " + numbers_text(rows) + "\n"  # создаю первую строку отчёта
        report = report + "Суммы столбцов: " + numbers_text(columns) + "\n"  # добавляю столбцы
        report = report + "Результат варианта: " + str(result) + "\n"  # добавляю вариант 2
        with open(folder / "report.txt", "w", encoding="utf-8") as file:  # пишу только после проверки
            file.write(report)  # сохраняю готовый отчёт
    except FileNotFoundError:  # входного файла нет
        print("Файл matrix.txt не найден")
    except UnicodeError:  # файл записан в неподходящей кодировке
        print("Ошибка кодировки: нужен UTF-8")
    except ValueError as error:  # формат таблицы не прошёл проверку
        print("Ошибка формата:", error)
    except OSError as error:  # не удалось прочитать или записать файл
        print("Ошибка доступа к файлу:", error)
    else:  # запись завершилась успешно
        print(report, end="")  # показываю содержимое отчёта без лишней пустой строки
        print("Отчёт сохранён в report.txt")  # сообщаю об успехе после записи


if __name__ == "__main__":  # не запускаю ввод при импорте
    main()
