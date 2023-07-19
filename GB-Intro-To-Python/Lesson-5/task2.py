# Напишите функцию, которая принимает на вход строку - абсолютный путь до файла.
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.

import os


def split_filepath(filepath):
    path, file = os.path.split(filepath)
    name, ext = os.path.splitext(file)
    return path, name, ext


my_path, my_name, my_ext = split_filepath("/path/to/my_file.txt")


print("Path:", my_path)
print("Name:", my_name)
print("Extension:", my_ext)
