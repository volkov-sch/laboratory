def sum_digits(number):
    number = abs(number)  # работаем с модулем числа
    total = 0
    while number > 0:
        total = total + number % 10  # добавляем последнюю цифру
        number = number // 10  # убираем последнюю цифру
    return total


def average(numbers):
    if len(numbers) == 0:
        return None
    return sum(numbers) / len(numbers)


def normalize_text(text):
    return " ".join(text.lower().split())


def select_numbers(numbers, threshold):
    # Вариант 2. Числа меньше порога.
    selected = []
    for number in numbers:
        if number < threshold:
            selected.append(number)
    return selected
