# Задание 1.7
# Пользователь вводит число от 1 до 999. Используя операции с числами сообщить что введено:
# цифра, двузначное число или трёхзначное число. Для цифры вернуть её квадрат.
# Для двузначного числа вернуть произведение цифр.
# Для трёхзначного числа вернуть его зеркальное отображение.
# Если число не из диапазона, запросить новое число.

number = int(input("Введите число от 1 до 999: "))

if number < 1 or number > 999:
    print("Число должно быть от 1 до 999. Попробуйте еще раз.")
elif number < 10:
    print(f"Введена цифра {number}. Квадрат числа: {number ** 2}")
elif number < 100:
    digit1 = number // 10
    digit2 = number % 10
    print(f"Введено двузначное число {number}. Произведение цифр: {digit1 * digit2}")
else:
    reversed_number = int(str(number)[::-1])
    print(f"Введено трехзначное число {number}. Зеркальное отображение: {reversed_number}")