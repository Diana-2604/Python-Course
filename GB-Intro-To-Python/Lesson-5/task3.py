# Напишите однострочный генератор словаря, который принимает на вход три списка одинаковой длины:
# имена str, ставка int, премия str с указанием процентов вида “10.25%”.
# В результате получаем словарь с именем в качестве ключа и суммой премии в качестве значения.
# Сумма рассчитывается как ставка умноженная на процент премии

def generate_bonus(names, rates, bonuses):
    return {name: rate * float(bonus.rstrip("%")) / 100
            for name, rate, bonus in zip(names, rates, bonuses)}
# Используем функцию zip для итерации по трем спискам одновременно
# Генератор словаря для создания словаря, где ключами являются имена, а значениями - сумма премии
# Метод rstrip для удаления знака процента в конце строки


list_names = ['Alice', 'Bob', 'Charlie']
list_rates = [100, 200, 300]
list_bonuses = ['10.25%', '5%', '15%']

print(generate_bonus(list_names, list_rates, list_bonuses))
