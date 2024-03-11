import sys


def get_mean_size(data_lines: list) -> str:
    size_summ = 0
    size_types = ["B", "KB", "MB", "GB", "TB"]
    size_type_index = 0

    for i_line in data_lines:
        columns = i_line.split()
        size_summ += int(columns[4])

    while size_summ > 1024:
        if size_type_index == 4:
            break
        else:
            size_summ = size_summ / 1024
            size_type_index += 1

    return f"Общий размер файлов в папке: {size_summ}{size_types[size_type_index]}"


if __name__ == "__main__":
    lines = sys.stdin.readlines()[1:]
    res = get_mean_size(data_lines=lines)
    print(res)