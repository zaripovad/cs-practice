import sys
from stats import read_valid, average_by_city, warmest_city


def main():
    lines = sys.stdin.read().splitlines()

    # теперь read_valid возвращает только список валидных словарей
    valid_records = read_valid(lines)
    parsed_count = len(valid_records)

    # вычисляем пропущенные строки:
    # всего строк - пустые строки - валидные записи
    empty_lines = sum(1 for line in lines if not line.strip())
    skipped_count = len(lines) - empty_lines - parsed_count

    print(parsed_count)
    print(skipped_count)

    if parsed_count > 0:
        warm_city = warmest_city(valid_records)
        result_temp = average_by_city(valid_records)[warm_city]
        print(result_temp)
    else:
        print(0.0)


if __name__ == "__main__":
    main()
