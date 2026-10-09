# заготовка stats.py

def parse_record(line: str) -> dict:
    parts = line.split(";")
    if len(parts) != 3:
        raise ValueError(f"строка не содержит ровно три поля: {line}")

    city, temp_str, date = parts

    if not city.strip():
        raise ValueError(f"город не указан в строке: {line}")
    if not date.strip():
        raise ValueError(f"дата не указана в строке: {line}")

    try:
        temp = float(temp_str)
    except ValueError:
        raise ValueError(f"температура не является числом в строке: {line}")

    return {"city": city.strip(), "temperature": temp, "date": date.strip()}


def read_valid(lines: list[str]) -> tuple[list[dict], int]:
    valid_records = []
    skipped_count = 0

    for line in lines:
        if not line.strip():  # Пропускаем пустые строки молча
            continue

        try:
            record = parse_record(line)
            valid_records.append(record)
        except ValueError:
            skipped_count += 1

    return valid_records, skipped_count


def average_by_city(records: list[dict]) -> dict:
    pass


def warmest_city(records: list[dict]) -> str:
    pass
