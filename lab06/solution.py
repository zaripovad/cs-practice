def count_by_extension(paths: list[str]) -> dict[str, int]:
    result = {}
    for path in paths:
        filename = path.split('/')[-1]

        if '.' in filename:
            ext = filename.rsplit('.', 1)[1].lower()
        else:
            ext = ""

        if ext in result:
            result[ext] += 1
        else:
            result[ext] = 1

    return result


def deepest_path(paths: list[str]) -> str:
    if not paths:
        return ""

    sorted_paths = sorted(paths, key=lambda x: (-x.count('/'), x))

    return sorted_paths[0]


def human_size(n_bytes: int) -> str:
    if n_bytes < 1024:
        return f"{n_bytes} Б"

    units = ["КБ", "МБ", "ГБ", "ТБ"]
    size = n_bytes / 1024
    unit_index = 0

    while size >= 1024 and unit_index < 3:
        size /= 1024
        unit_index += 1

    return f"{size:.1f} {units[unit_index]}"