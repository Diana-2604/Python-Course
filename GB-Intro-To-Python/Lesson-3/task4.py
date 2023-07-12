# Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
# Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность.

backpack_items = {
    'tent': 100,
    'knife': 10,
    'water bottle': 30,
    'sleeping bag': 50,
    'flashlight': 15
}

backpack_max_weight = 170


def fit_items_in_backpack(items, max_weight):
    # Сортируем список предметов по убыванию массы
    sorted_items = sorted(items.items(), key=lambda x: x[1], reverse=True)
    # Создаем пустой словарь для хранения предметов, помещенных в рюкзак
    backpack = {}
    # Проходимся по каждому предмету в отсортированном списке
    for item, weight in sorted_items:
        # Если предмет помещается в рюкзак, то добавляем его в словарь backpack
        if weight <= max_weight:
            backpack[item] = weight
            max_weight -= weight
    # Возвращаем словарь с предметами, помещенными в рюкзак
    return backpack


print("Вещи, которые поместятся в рюкзак: ", fit_items_in_backpack(backpack_items, backpack_max_weight))
