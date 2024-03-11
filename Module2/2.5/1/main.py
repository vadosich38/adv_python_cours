def get_summary_rss(path: str) -> str:
    summ = 0
    type_index = 0
    types = ["B", "KB", "MB", "GB", "TB"]

    with open(file=path, mode="r", encoding="utf-8") as file:
        lines = file.readlines()[1:]

        for i_line in lines:
            columns = i_line.split()
            summ += int(columns[5])

    while summ > 1024:
        if type_index == 4:
            break
        else:
            summ = summ / 1024
            type_index += 1
    else:
        summ = round(summ, 2)

    return f"{summ}{types[type_index]}"


if __name__ == "__main__":
    get_summ = get_summary_rss(path="output_file.txt")
    print(get_summ)
