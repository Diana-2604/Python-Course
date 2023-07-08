# Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
# Программа должна возвращать сумму и произведение дробей.
# Для проверки своего кода используйте модуль fractions.

from fractions import Fraction

# Получаем первую дробь от пользователя
frac1_str = input("Введите первую дробь в формате a/b: ")
frac1_parts = frac1_str.split('/')
frac1_num = int(frac1_parts[0])
frac1_denom = int(frac1_parts[1])

# Получаем вторую дробь от пользователя
frac2_str = input("Введите вторую дробь в формате a/b: ")
frac2_parts = frac2_str.split('/')
frac2_num = int(frac2_parts[0])
frac2_denom = int(frac2_parts[1])

# Вычисляем общий знаменатель и числитель для суммы
if frac1_denom % frac2_denom == 0:
    common_denom = frac1_denom
    sum_num = frac1_num + frac2_num * (frac1_denom / frac2_denom)
elif frac2_denom % frac1_denom == 0:
    common_denom = frac2_denom
    sum_num = frac2_num + frac1_num * (frac2_denom / frac1_denom)
else:
    common_denom = frac1_denom * frac2_denom
    sum_num = frac1_num * frac2_denom + frac2_num * frac1_denom

# Вычисляем числитель и знаменатель для произведения
prod_num = frac1_num * frac2_num
prod_denom = frac1_denom * frac2_denom

# Проверяем с помощью fractions
frac1 = Fraction(frac1_str)
frac2 = Fraction(frac2_str)
sum_frac = frac1 + frac2
prod_frac = frac1 * frac2

# Выводим результаты на экран
print("Сумма дробей:", str(int(sum_num)) + '/' + str(common_denom))
print("Проверка суммы дробей:", sum_frac)
print("Произведение дробей:", str(prod_num) + '/' + str(prod_denom))
print("Проверка произведения дробей:", prod_frac)
