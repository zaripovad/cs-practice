import sys
from stats import read_valid, average_by_city, warmest_city


def main():
    lines = sys.stdin.read().splitlines()
    valid_records, skipped = read_valid(lines)
    parsed_count = len(valid_records)

    # вывод 1: сколько записей разобрано
    print(parsed_count)

    # вывод 2: сколько строк пропущено
    print(skipped)

    # вывод 3: средняя температура самого теплого города
    if parsed_count > 0:
        warm_city = warmest_city(valid_records)
        result_temp = average_by_city(valid_records)[warm_city]
        print(result_temp)
    else:
        print(0.0)


if __name__ == "__main__":
    main()
