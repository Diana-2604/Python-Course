# Три друга взяли вещи в поход. Сформируйте словарь, где ключ — имя друга, а значение — кортеж вещей.
# Ответьте на вопросы: Какие вещи взяли все три друга? Какие вещи уникальны, есть только у одного друга?
# Какие вещи есть у всех друзей кроме одного и имя того, у кого данная вещь отсутствует?
# Для решения используйте операции с множествами. Код должен расширяться на любое большее количество друзей

friends = {
    'friend1': ('tent', 'sleeping bag', 'backpack', 'water bottle'),
    'friend2': ('sleeping bag', 'backpack', 'flashlight', 'knife'),
    'friend3': ('tent', 'backpack', 'water bottle', 'map')
}

# Вещи, которые взяли все три друга
all_items = set.intersection(*[set(items) for items in friends.values()])
print("These items were taken by all three friends: ", all_items)

# Вещи, которые взяли хотя бы два друга
common_items = set()
for i, (name1, items1) in enumerate(friends.items()):
    for name2, items2 in list(friends.items())[i+1:]:
        common_items.update(set(items1).intersection(set(items2)))

# Вещи, которые есть только у одного друга
unique_items = set.union(*[set(items) for items in friends.values()]) - common_items
print("These items were taken only by one friend: ", unique_items)

# Вещи, которые есть у всех кроме одного и имя того, у кого данная вещь отсутствует
all_but_one = {}
for friend, items in friends.items():
    friend_items = set(items)
    diff_items = common_items - friend_items
    if diff_items:
        all_but_one[friend] = diff_items
print("These items were taken by all but one friend: ")
for friend, items in all_but_one.items():
    print(friend, items)
    