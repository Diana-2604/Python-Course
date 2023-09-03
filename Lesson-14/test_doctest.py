# Пользователь вводит число от 1 до 999. Используя операции с числами сообщить что введено:
# цифра, двузначное число или трёхзначное число. 
# Для цифры вернуть её квадрат.
# Для двузначного числа вернуть произведение цифр.
# Для трёхзначного числа вернуть его зеркальное отображение.
# Если число не из диапазона, запросить новое число.


def check_number(number: int):
    """
    >>> check_number(0)
    Число должно быть от 1 до 999. Попробуйте еще раз.

    >>> check_number(1000)
    Число должно быть от 1 до 999. Попробуйте еще раз.

    >>> check_number(5)
    Введена цифра 5. Квадрат числа: 25

    >>> check_number(25)
    Введено двузначное число 25. Произведение цифр: 10

    >>> check_number(123)
    Введено трехзначное число 123. Зеркальное отображение: 321
    """

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

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)