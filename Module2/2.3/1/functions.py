def converter(size: int, name_index: int = 0) -> str:
    sizes_names = ["", "K", "M", "GB", "TB"]

    while size >= 1024:
        size = size / 1024
        name_index += 1
    formatted_size = formatting_size(size=size)

    return f"{formatted_size}{sizes_names[name_index]}"


def formatting_size(size: int) -> int:
    if size < 10:
        formatted_file_size = round(size, 1)
    else:
        formatted_file_size = round(size)
    return formatted_file_size

