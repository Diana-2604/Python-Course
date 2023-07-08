# Написать программу-банкомат на python:
# Начальная сумма равна нулю.
# Допустимые действия: пополнить, снять, выйти.
# Сумма пополнения и снятия кратны 50 у.е.
# Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
# После каждой третьей операции пополнения или снятия начисляются проценты - 3%.
# Нельзя снять больше, чем на счёте.
# При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой операцией, даже ошибочной.
# Любое действие выводит сумму денег

balance = 0    # начальный баланс
count = 0      # счетчик операций
tax_threshold = 5000000  # порог налога на богатство
tax_rate = 0.1  # ставка налога на богатство

while True:
    print("Текущий баланс:", balance, "у.е.")
    action = input("Выберите действие: пополнить, снять, выйти: ").lower()

    if action == "выйти":
        break
    elif action == "пополнить":
        deposit = int(input("Введите сумму пополнения (кратную 50): "))
        if deposit % 50 != 0:
            print("Сумма пополнения должна быть кратна 50")
            continue
        balance += deposit
        count += 1
        if count % 3 == 0:
            balance += balance * 0.03
    elif action == "снять":
        withdrawal = int(input("Введите сумму снятия (кратную 50): "))
        if balance < withdrawal:
            print("На вашем счете недостаточно средств")
            continue
        if withdrawal % 50 != 0:
            print("Сумма снятия должна быть кратна 50")
            continue
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
    else:
        print("Некорректное действие")
        continue

print("Спасибо за использование нашего банкомата!")