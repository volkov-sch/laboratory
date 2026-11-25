import json  # использую стандартный модуль JSON
from pathlib import Path  # работаю с путями к файлам
from logic import validate_records  # использую общую проверку записей


def load_records(path):
    """Читаю и проверяю записи, возвращаю список. Ошибки передаю основной программе."""
    with open(path, "r", encoding="utf-8") as file:  # исходный файл не открываю для записи
        records = json.load(file)
    validate_records(records)  # проверяю весь набор до начала работы
    return records


def save_records(path, records):
    """Сохраняю проверенный список, возвращаю None. При ошибке записи старый файл сохраняется."""
    validate_records(records)  # неправильный список не должен испортить файл
    text = json.dumps(records, ensure_ascii=False, indent=2)  # готовлю весь текст до записи
    path = Path(path)
    temporary = path.with_name(path.name + ".tmp")  # сначала пишу в соседний временный файл
    with open(temporary, "w", encoding="utf-8") as file:
        file.write(text)
    temporary.replace(path)  # заменяю основной файл только после успешной записи
