import json
from pathlib import Path
from tempfile import TemporaryDirectory
from storage import load_records, save_records


folder = Path(__file__).resolve().parent
with TemporaryDirectory(dir=folder) as directory:  # все записи теста находятся во временной папке
    directory = Path(directory).resolve()
    assert directory.parent == folder
    path = directory / "data.json"
    try:
        load_records(path)  # проверяю отсутствующий файл
    except FileNotFoundError:
        pass
    else:
        assert False, "Отсутствующий файл не обнаружен"

    save_records(path, [])  # проверяю сохранение пустого списка
    assert load_records(path) == []
    records = [
        {"id": 1, "title": "Книга", "category": "учёба", "amount": 4, "completed": False},
        {"id": 2, "title": "Атлас", "category": "справочная", "amount": 2, "completed": True, "note": "Своя заметка"},
    ]
    save_records(path, records)
    assert load_records(path) == records  # поля, статусы и дополнительный ключ восстановились
    assert "Книга" in path.read_text(encoding="utf-8")  # кириллица читаемая
    assert not path.with_name("data.json.tmp").exists()  # временный файл заменил основной

    for text in ["{", "{}", '[{"id": 1}]', json.dumps([records[0], records[0]])]:
        path.write_text(text, encoding="utf-8")
        saved = path.read_bytes()
        try:
            load_records(path)  # повреждённый синтаксис или структура должны вызвать ошибку
        except ValueError:
            pass
        else:
            assert False, "Неверный JSON принят"
        assert path.read_bytes() == saved  # чтение не перезаписывает повреждённый файл

    path.write_bytes(b'\xff')  # проверяю неподходящую кодировку
    try:
        load_records(path)
    except UnicodeError:
        pass
    else:
        assert False, "Ошибка кодировки не обнаружена"
    assert path.read_bytes() == b'\xff'

    save_records(path, records)
    saved = path.read_bytes()
    try:
        save_records(path, [{"id": True}])  # неправильные данные нельзя записывать
    except ValueError:
        pass
    else:
        assert False, "Неправильный набор записан"
    assert path.read_bytes() == saved

    blocked = path.with_name("data.json.tmp")
    blocked.mkdir()  # вместо временного файла создаю папку, чтобы запись завершилась ошибкой
    try:
        save_records(path, [])
    except OSError:
        pass
    else:
        assert False, "Ошибка записи не обнаружена"
    assert path.read_bytes() == saved  # прежний основной файл сохранился
    blocked.rmdir()  # удаляю только созданную пустую папку
    save_records(path, records)  # после устранения ошибки сохранение снова работает
    assert load_records(path) == records
print("Все проверки хранения проекта пройдены")
