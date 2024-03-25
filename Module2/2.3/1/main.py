import re
from functions import converter

with open("ls-la.txt", mode="r", encoding="utf-8") as read_file:
    directorys_count = 0
    files_count = 0

    total_size = 0

    with open("my_ls-lha.txt", mode="w", encoding="utf-8") as new_file:
        for i_line in read_file:
            file_size = re.findall(pattern=r"\d+ \b", string=i_line)
            if file_size:
                file_size = int(file_size[1].strip())
                formatted_file_size = file_size
                total_size += formatted_file_size

                size_data = converter(size=formatted_file_size)

                new_line = i_line.replace(str(file_size), f"{size_data}")
            else:
                total_size_in_line = re.findall(pattern=r"\d+", string=i_line)
                if total_size_in_line:
                    total_size_in_line = int(total_size_in_line[0].strip())

                    size_data = converter(size=total_size_in_line, name_index=1)

                new_line = f"total {size_data}\n"

            new_file.write(new_line)

            if re.match(pattern=r"\bd.*", string=i_line):
                directorys_count += 1
            else:
                files_count += 1
        else:
            size_data = converter(size=total_size)
            print(f"Общий размер файлов: {size_data}")
            print(f"Файлов: {files_count}, папок: {directorys_count}")



"""
module3.3. С помощью python выясните количество файлов и папок в output
2. Подсчитайте суммарный размер всех файлов в папке /etc в байтах
Переведите его в человекочитаемый формат (1024 байта = module3.3 кБ, 1024 кБ = module3.3 МБ и тд
3. Напишите функцию, которая по output из ls -la выводит суммарный размер файлов в человекочитаемом формате.
"""