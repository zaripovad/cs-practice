import json

def csv_to_records(text: str) -> list[dict]:
    lines = text.strip().split('\n')

    if not lines or not lines[0]:
        return []

    headers = [header.strip() for header in lines[0].split(',')]

    records = []
    for line in lines[1:]:

        if not line.strip():
            continue

        values = [val.strip() for val in line.split(',')]

        record = dict(zip(headers, values))
        records.append(record)

    return records


def parse_settings(lines: list[str]) -> dict:
    result = {}
    current_key = None

    for line in lines:
        if '#' in line:
            line = line.split('#')[0]

        line = line.strip()


        if not line:
            continue

        if line.startswith('- '):
            value_str = line[2:].strip()
            value = convert_yaml_value(value_str)

            if current_key is not None and isinstance(result[current_key], list):
                result[current_key].append(value)

        elif ':' in line:
            key, value_str = line.split(':', 1)
            key = key.strip()
            value_str = value_str.strip()

            current_key = key

            if value_str:
                result[key] = convert_yaml_value(value_str)
            else:
                result[key] = []

    return result


def convert_yaml_value(val_str: str):
    lower_val = val_str.lower()
    if lower_val in ('true', 'yes'):
        return True
    if lower_val in ('false', 'no'):
        return False

    try:
        if '.' not in val_str:
            return int(val_str)
        else:
            return float(val_str)
    except ValueError:
        return val_str