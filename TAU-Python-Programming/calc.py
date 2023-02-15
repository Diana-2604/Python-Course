# python "reads" the program from top to bottom, and will
# cause errors if functions are called before they are created
calc_on = True


def add():
    a = float(input("Enter a number. "))
    b = float(input("Enter another number. "))
    print(a + b)


def subtract():
    a = float(input("Enter a number. "))
    b = float(input("Enter another number. "))
    print(a - b)


def multiply():
    a = float(input("Enter a number. "))
    b = float(input("Enter another number. "))
    print(a * b)


def divide():
    a = float(input("Enter a number. "))
    b = float(input("Enter another number. "))
    print(a / b)


while calc_on:
    operation = input("Please type +, -, *, / or q ")

    if operation == '+':
        add()

    elif operation == '-':
        subtract()

    elif operation == '*':
        multiply()

    elif operation == '/':
        divide()

    elif operation == 'q':
        calc_on = False

    else:
        print("This operation is not available")
