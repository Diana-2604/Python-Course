# args - Positional Arguments
def user_info(name, age, city):
    '''This function prints name, age, and city from an argument provided to the function.'''
    print("{} is {} years old, from {}".format(name, age, city))


user_info("Diana", 24, "St. Petersburg City")


# These are positional arguments because Python is reading these arguments _in order_,
# in the position that they are given in the function definition

# kwargs - Keyword Arguments
# we can set some defaults when we're using keyword arguments, so that way
# our function knows what to do if we don't provide the value that it's looking for, for any of the arguments.

def user_kwargs(name, age=0, city="Moscow"):
    print("{} is {} years old, from {}".format(name, age, city))


user_kwargs("Lisa")
user_kwargs(age=56, name="Kate")


# with keyword arguments, you don't need to follow the positional order of the argument
# As long as you have a default specified for anything you're not providing,
# you will be able to overwrite the values of the defaults that you do provide and
# any arguments that are required, of course you'll need to provide as well

# *args & **kwargs
# The *args allows a function to take any number of positional arguments
def add(*args):
    print(sum(args))


add(2, 3, 4)
add(10, 5, 7, 3, 25)


# The **kwargs allows a function to take any number of keyword arguments
# All three argument types can be used in a single function.
# They must be used in order: formal positional arguments, *args, **kwargs
def application(fname, lname, email, company, *args, **kwargs):
    print("{} {} works at {}. Her email is {}.".format(fname, lname, company, email))


application("Jess", "Ingrass", "mail @ mail.com", "Teach Code", 75000, hire_date="September 2010")
