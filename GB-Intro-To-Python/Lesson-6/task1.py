# Создайте модуль и напишите в нём функцию, которая получает на вход дату в формате DD.MM.YYYY
# Функция возвращает истину, если дата может существовать или ложь, если такая дата невозможна.
# Для простоты договоримся, что год может быть в диапазоне [1, 9999].
# Весь период (1 января 1 года - 31 декабря 9999 года) действует Григорианский календарь.
# Проверку года на високосность вынести в отдельную защищённую функцию.

# Функция is_valid_date принимает дату в формате DD.MM.YYYY и
# возвращает True, если дата может существовать и False, если такая дата невозможна.
def is_valid_date(date_str):
    day, month, year = map(int, date_str.split('.'))
    if year < 1 or year > 9999:
        return False
    if month < 1 or month > 12:
        return False
    if day < 1 or day > days_in_month(month, year):
        return False
    return True


# Функция days_in_month принимает номер месяца и год и возвращает количество дней в этом месяце.
# Она использует функцию is_leap_year для определения количества дней в феврале.
def days_in_month(month, year):
    days = [31, 28 if not is_leap_year(year) else 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return days[month - 1]


# Функция is_leap_year принимает год и возвращает
# True, если год является високосным, и False, если он не является високосным
def is_leap_year(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True


input_date = '29.02.2020'
if is_valid_date(input_date):
    print(f"{input_date} is a valid date")
else:
    print(f"{input_date} is not a valid date")
