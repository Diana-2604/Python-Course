# Напишите функцию, которая получает на вход директорию и рекурсивно обходит её и все вложенные директории.
# Результаты обхода сохраните в файлы json, csv и pickle.
# Для дочерних объектов указывайте родительскую директорию.
# Для каждого объекта укажите файл это или директория.
# Для файлов сохраните его размер в байтах, а для директорий размер файлов в ней с учётом
# всех вложенных файлов и директорий.


import os
import json
import csv
import pickle


def save_directory_info(path):
    """
    Рекурсивно обходит директорию и все вложенные директории,
    сохраняя результаты обхода в файлы форматов JSON, CSV и pickle.

    Параметры:
        path (str): Путь к директории, которую нужно обойти.

    Возвращает:
        None.
    """
    # Создаем пустые списки, в которых будем хранить информацию о каждом объекте
    files_data = []
    dirs_data = []

    # Обходим все объекты в директории и ее поддиректориях
    for root, dirs, files in os.walk(path):
        # Считаем размер директории (включая все вложенные файлы и директории)
        dir_size = sum(os.path.getsize(os.path.join(root, file)) for file in files)
        dir_size += sum(os.path.getsize(os.path.join(root, d, file)) for d, _, files in os.walk(root) for file in files)

        # Добавляем информацию о директории в список dirs_data
        dirs_data.append({
            'path': os.path.relpath(root, path),
            'size': dir_size,
        })

        # Добавляем информацию о каждом файле в список files_data
        for file in files:
            file_path = os.path.join(root, file)
            files_data.append({
                'path': os.path.relpath(file_path, path),
                'size': os.path.getsize(file_path),
            })

    # Сохраняем информацию о директориях в файлы форматов JSON, CSV и pickle
    with open('dirs.json', 'w') as f:
        json.dump(dirs_data, f, indent=4)
    with open('dirs.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['path', 'size'])
        for dir_data in dirs_data:
            writer.writerow([dir_data['path'], dir_data['size']])
    with open('dirs.pickle', 'wb') as f:
        pickle.dump(dirs_data, f)

    # Сохраняем информацию о файлах в файлы форматов JSON, CSV и pickle
    with open('files.json', 'w') as f:
        json.dump(files_data, f, indent=4)
    with open('files.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['path', 'size'])
        for file_data in files_data:
            writer.writerow([file_data['path'], file_data['size']])
    with open('files.pickle', 'wb') as f:
        pickle.dump(files_data, f)
