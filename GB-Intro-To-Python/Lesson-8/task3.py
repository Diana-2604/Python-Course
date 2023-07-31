# Прочитайте созданный в прошлом задании csv файл без использования csv.DictReader.
# Распечатайте его как pickle строку.


import csv
import pickle

with open('data.csv', 'r') as f:
    reader = csv.reader(f)
    header = next(reader)
    data = [dict(zip(header, row)) for row in reader]

pickle_string = pickle.dumps(data)
print(pickle_string)
