# Написать программу на python, которая получает целое число и
# возвращает его шестнадцатеричное строковое представление без использования функции hex.
# Использовать функцию hex для проверки результата.

num = int(input("Введите целое число: "))

# Получаем шестнадцатеричное представление числа с помощью hex()
hex_num = hex(num)
print("Шестнадцатеричное представление числа (с помощью hex()):", hex_num)

# Список символов шестнадцатеричной системы счисления
hex_chars = "0123456789abcdef"

# Переменная для хранения шестнадцатеричного представления числа
hex_str = ""

# Проходим по битам числа, начиная со старшего
while num > 0:
    # Находим остаток от деления числа на 16
    remainder = num % 16
    # Добавляем соответствующий символ шестнадцатеричной системы в начало строки
    hex_str = hex_chars[remainder] + hex_str
    # Делаем целочисленное деление на 16, чтобы перейти к следующему биту
    num //= 16

print("Шестнадцатеричное представление числа:", hex_str)

