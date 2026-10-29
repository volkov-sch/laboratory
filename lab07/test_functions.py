from functions import average, normalize_text, select_numbers, sum_digits


# Проверяем сумму цифр.
assert sum_digits(0) == 0
assert sum_digits(507) == 12
assert sum_digits(-507) == 12

# Проверяем среднее и сохранение исходного списка.
assert average([]) is None
assert average([2, 4, 6]) == 4
assert average([8]) == 8
assert abs(average([1, 2, 2]) - 5 / 3) < 1e-9
numbers = [2, 4, 6]
saved = numbers.copy()
assert average(numbers) == 4
assert numbers == saved

# Проверяем регистр, пробелы и пустой текст.
assert normalize_text("  ПРИВЕТ   Мир  ") == "привет мир"
assert normalize_text("   ") == ""
assert normalize_text("") == ""
assert normalize_text("\tПривет\tМИР\n") == "привет мир"

# Вариант 2: граница не входит, порядок и повторы сохраняются.
assert select_numbers([-5, 0, 2, 5], 2) == [-5, 0]
assert select_numbers([], 2) == []
assert select_numbers([1, 2, 3], 2) == [1]
assert select_numbers([2, 3, 5], 2) == []
assert select_numbers([1, -3, 1, 2], 2) == [1, -3, 1]
assert select_numbers([-1, 0, 1], 0) == [-1]

numbers = [-5, 0, 2, 5]
saved = numbers.copy()
selected = select_numbers(numbers, 2)
assert numbers == saved
selected.append(100)  # изменение результата не меняет исходный список
assert numbers == saved

print("Все проверки пройдены")