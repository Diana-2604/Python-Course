# If, else/if and else — if, elif and else — are control structures in Python
# once the condition is met, none of the other conditions matter

name = input("What's your name? ")
if name == "Natasha":
    print("Hello, nice to see you {}!".format(name))
elif name == "Nadya":
    print("Hello {}, you are a lovely person!".format(name))
elif name == "Ruslan":
    print("Hi {}, let's have lunch soon!".format(name))
else:
    print("Have a nice day!")

# You should use else whenever you want to catch any conditions not identified in "if" or "elif" statements.
# It can be used only once per conditional block
