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