from functions import average, normalize_text, select_numbers, sum_digits


def main():
    number = int(input("Введите целое число: "))

    numbers = []
    for part in input("Введите целые числа через пробел: ").split():
        numbers.append(int(part))

    text = input("Введите текст: ")
    threshold = int(input("Введите неотрицательный порог: "))
    while threshold < 0:
        threshold = int(input("Введите неотрицательный порог: "))

    print("Сумма цифр:", sum_digits(number))

    result = average(numbers)
    if result is None:
        print("Нет данных")
    else:
        print("Среднее:", result)

    print("Нормализованный текст:", normalize_text(text))
    print("Числа меньше порога:", select_numbers(numbers, threshold))


if __name__ == "__main__":
    main()