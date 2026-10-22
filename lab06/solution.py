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