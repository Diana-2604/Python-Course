# Написать программу-банкомат:
# Начальная сумма равна нулю.
# Допустимые действия: пополнить, снять, выйти.
# Сумма пополнения и снятия кратны 50 у.е.
# Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
# После каждой третьей операции пополнения или снятия начисляются проценты - 3%.
# Нельзя снять больше, чем на счёте.
# При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой операцией, даже ошибочной.
# Любое действие выводит сумму денег.
# Разбить задачу на отдельные операции — функции.
# Дополнительно сохранять все операции поступления и снятия средств в список.

def print_balance(balance):
    # Выводит текущий баланс на экран
    print("Текущий баланс:", balance, "у.е.")


def deposit_funds(balance, count):
    # Пополнение баланса
    deposit = int(input("Введите сумму пополнения (кратную 50): "))
    if deposit % 50 != 0:
        print("Сумма пополнения должна быть кратна 50")
        return balance, count
    balance += deposit
    count += 1
    if count % 3 == 0:
        balance += balance * 0.03
    return balance, count


def withdraw_funds(balance, count):
    # Снятие средств
    withdrawal = int(input("Введите сумму снятия (кратную 50): "))
    if balance < withdrawal:
        print("На вашем счете недостаточно средств")
        return balance, count
    if withdrawal % 50 != 0:
        print("Сумма снятия должна быть кратна 50")
        return balance, count
    if balance > tax_threshold:
        balance -= balance * tax_rate
    if withdrawal >= 600:
        commission = 600
    elif withdrawal <= 30:
        commission = 30
    else:
        commission = withdrawal * 0.015
    balance -= withdrawal + commission
    count += 1
    if count % 3 == 0:
        balance += balance * 0.03
    return balance, count


def print_exit():
    # Выводит сообщение о завершении работы
    print("Спасибо за использование нашего банкомата!")


# Начальные значения
balance = 0
count = 0
tax_threshold = 5000000
tax_rate = 0.1
transactions = []

while True:
    print_balance(balance)
    action = input("Выберите действие: пополнить, снять, выйти: ").lower()

    if action == "выйти":
        break
    elif action == "пополнить":
        balance, count = deposit_funds(balance, count)
        transactions.append(('Пополнение', balance))
    elif action == "снять":
        balance, count = withdraw_funds(balance, count)
        transactions.append(('Снятие', balance))
    else:
        print("Некорректное действие")
        continue

print_exit()
