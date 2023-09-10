# Создайте модуль и напишите в нём функцию, которая получает на вход дату в формате DD.MM.YYYY
# Функция возвращает истину, если дата может существовать или ложь, если такая дата невозможна.
# Для простоты договоримся, что год может быть в диапазоне [1, 9999].
# Весь период (1 января 1 года - 31 декабря 9999 года) действует Григорианский календарь.
# Проверку года на високосность вынести в отдельную защищённую функцию.
import argparse
import logging

logging.basicConfig(level=logging.NOTSET)
logger = logging.getLogger(__name__)

logger.info('Функция is_valid_date принимает дату в формате DD.MM.YYYY и возвращает True, если дата может существовать и False, если такая дата невозможна')
def is_valid_date(date_str):
    day, month, year = map(int, date_str.split('.'))
    if year < 1 or year > 9999:
        logger.warning('Год находится вне допустимого диапазона значений')
        return False
    if month < 1 or month > 12:
        logger.error('Такого месяца не бывает')
        return False
    if day < 1 or day > days_in_month(month, year):
        logger.debug('Похоже, дня с таким числом не может быть в указанном месяце')
        return False
    return True


logger.info('Функция days_in_month принимает номер месяца и год и возвращает количество дней в этом месяце. Она использует функцию is_leap_year для определения количества дней в феврале.') 
def days_in_month(month, year):
    days = [31, 28 if not is_leap_year(year) else 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    logger.warning('Номер месяца передается на 1 значение больше имеющегося в массиве, поэтому требуется вычитание')
    return days[month - 1]

logger.info('Функция is_leap_year принимает год и возвращает True, если год является високосным, и False, если он не является високосным')
def is_leap_year(year):
    if year % 4 != 0:
        logger.debug('Базовая проверка на високосность')
        return False
    elif year % 100 != 0:
        logger.info('Внезапно: деление на 100 дает високосность')
        return True
    elif year % 400 != 0:
        logger.warning('Каждый 400-ый год не является високосным, хоть и делится на 4')
        return False
    else:
        return True


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Date validator')
    parser.add_argument('date', type=str, help='Date to validate in the format DD.MM.YYYY')
    args = parser.parse_args()

    logger.info('Вывод результата проверки даты')
    if is_valid_date(args.date):
        print(f"{args.date} is a valid date")
    else:
        print(f"{args.date} is not a valid date")

# Для запуска кода из терминала, ввести команду типа "python3 Downloads/date_validator_Lesson15.py 29.02.2024"
