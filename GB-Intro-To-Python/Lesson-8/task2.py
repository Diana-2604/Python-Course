# Напишите функцию, которая преобразует pickle файл хранящий список словарей в табличный csv файл.
# Функция должна извлекать ключи словаря для заголовков столбца из переданного файла.

import pickle
import csv


def pickle_to_csv(pickle_file, csv_file):
    """
    Преобразует файл формата pickle, хранящий список словарей, в табличный файл формата CSV.

    Параметры:
        pickle_file (str): Путь к файлу формата pickle.
        csv_file (str): Путь к файлу формата CSV, в который нужно сохранить данные.

    Возвращает:
        None.
    """
    with open(pickle_file, 'rb') as f:
        data = pickle.load(f)

    with open(csv_file, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)


pickle_to_csv('data.pickle', 'data.csv')
