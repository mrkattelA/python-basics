import os
from pathlib import Path

def file_path(relative_path):
    start_dir = Path(__file__).parent
    return Path(start_dir,relative_path)

def file_to_list(path):
    with open(file_path(path), encoding="utf-8") as f:
        lines = f.read().splitlines()
    return lines

def subtract_list(list1,list2):
    return [x for x in list1 if x not in list2]

def dups(list1, list2, sort = True):
    dup_list = []
    for item in list1:
        if item in list2:
            dup_list.append(item)

    if sort:
        dup_list.sort()

    return dup_list

def list_to_file(path, the_list):
    content = "\n".join(the_list)

    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

def main():
    boys_2018_path = Path(r"C:\Users\mrkat\OneDrive\Desktop\Webucator\Python\file-processing\data\2018-boys.txt")
    girls_2018_path = Path(r"C:\Users\mrkat\OneDrive\Desktop\Webucator\Python\file-processing\data\2018-girls.txt")
    boys_1880_path = Path(r"C:\Users\mrkat\OneDrive\Desktop\Webucator\Python\file-processing\data\1880-boys.txt")
    girls_1880_path = Path(r"C:\Users\mrkat\OneDrive\Desktop\Webucator\Python\file-processing\data\1880-girls.txt")

    boys_2018 = file_to_list(boys_2018_path)
    girls_2018 = file_to_list(girls_2018_path)
    boys_1880 = file_to_list(boys_1880_path)
    girls_1880 = file_to_list(girls_1880_path)

    boys_only_2018 = subtract_list(boys_2018,girls_2018)
    girls_only_2018 = subtract_list(girls_2018,boys_2018)
    boys_only_1880 = subtract_list(boys_1880,girls_1880)
    girls_only_1880 = subtract_list(girls_1880,boys_1880)

    boys_name_to_girls_name = dups(girls_only_2018, boys_only_1880)
    girls_name_to_boys_name = dups(boys_only_2018,girls_only_1880)

    list_to_file(Path(r"C:\Users\mrkat\OneDrive\Desktop\Webucator\Python\file-processing\data\boys_name_to_girls_name",
                      ),boys_name_to_girls_name)
    list_to_file(Path(r"C:\Users\mrkat\OneDrive\Desktop\Webucator\Python\file-processing\data\girls_name_to_boys_name",
                      ),girls_name_to_boys_name)

main()


        