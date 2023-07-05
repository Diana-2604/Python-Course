# Задание 1.8
# Нарисовать в консоли ёлку, спросив у пользователя количество рядов

rows = int(input("Введите количество рядов ёлки: "))

for row in range(1, rows + 1):
    for space in range(rows - row):
        print(" ", end="")
    for star in range(row * 2 - 1):
        print("*", end="")
    print()