# Напишите функцию, которая ищет json файлы в указанной
# директории и сохраняет их содержимое в виде
# одноимённых pickle файлов.

import os
import json
import pickle


def convert_json_to_pickle(directory):
    """
    Ищет JSON-файлы в указанной директории и сохраняет их содержимое в виде одноименных файлов формата pickle.

    Параметры:
        directory (str): Путь к директории, в которой нужно искать JSON-файлы.

    Возвращает:
        None.
    """
    for filename in os.listdir(directory):
        if filename.endswith('.json'):
            with open(os.path.join(directory, filename), 'r') as f:
                data = json.load(f)
            with open(os.path.join(directory, os.path.splitext(filename)[0] + '.pickle'), 'wb') as f:
                pickle.dump(data, f)


convert_json_to_pickle('/path/to/directory')
