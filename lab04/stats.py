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
        temp = float(temp_str.strip())
    except ValueError:
        raise ValueError(f"температура не является числом в строке: {line}")

    return {"city": city.strip(), "temperature": temp, "date": date.strip()}


def read_valid(lines: list[str]) -> list[dict]:
    valid_records = []

    for line in lines:
        if not line.strip():  # пропускаем пустые строки молча
            continue

        try:
            record = parse_record(line)
            valid_records.append(record)
        except ValueError:
            pass  # просто пропускаем негодные строки, не считая их здесь

    return valid_records


def average_by_city(records: list[dict]) -> dict:
    total = {}
    count = {}

    for rec in records:
        city = rec["city"]
        temp = rec["temperature"]
        total[city] = total.get(city, 0.0) + temp
        count[city] = count.get(city, 0) + 1

    return {city: round(total[city] / count[city], 1) for city in total}


def warmest_city(records: list[dict]) -> str:
    averages = average_by_city(records)
    if not averages:
        return ""

    sorted_cities = sorted(averages.items(), key=lambda x: (-x[1], x[0]))
    return sorted_cities[0][0]
