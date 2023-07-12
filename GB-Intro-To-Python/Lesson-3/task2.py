# Дан список повторяющихся элементов.
# Вернуть список с дублирующимися элементами.
# В результирующем списке не должно быть дубликатов.

check_list = [1, 2, 3, 2, 4, 1, 5, 6, 5]


def get_duplicates(lst):
    # Создаем множество для отслеживания уникальных элементов
    unique_items = set()
    # Создаем множество для отслеживания дублирующихся элементов
    duplicates = set()
    # Проходимся по каждому элементу списка
    for item in lst:
        # Если элемент уже встречался ранее, то добавляем его в множество дублирующихся элементов
        if item in unique_items:
            duplicates.add(item)
        # В любом случае добавляем элемент в множество уникальных элементов
        unique_items.add(item)
    # Возвращаем список дублирующихся элементов без дубликатов
    return list(set(duplicates))


def remove_duplicates(lst):
    # Создаем множество для отслеживания уникальных элементов
    unique_items = set()
    # Создаем список для хранения уникальных элементов в том же порядке, что и в исходном списке
    unique_lst = []
    # Проходимся по каждому элементу списка
    for item in lst:
        # Если элемент еще не встречался ранее, то добавляем его в список уникальных элементов и множество уникальных элементов
        if item not in unique_items:
            unique_lst.append(item)
            unique_items.add(item)
    # Возвращаем список уникальных элементов
    return unique_lst


print("Duplicates:", get_duplicates(check_list))
print("List without duplicates:", remove_duplicates(check_list))
