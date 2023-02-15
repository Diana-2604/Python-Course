# A function is a unit of code that can be reused throughout a program
# On every function, we have the letters def, a unique function name, the parenthesis and the colon
# The body of our function is always indented 4 spaces (1 tab) and
# we remove the spaces when we want to call a function

def addition():
    a = int(input("Enter your first number: "))
    b = int(input("Enter your second number: "))
    print("The output is:", a+b)


addition()