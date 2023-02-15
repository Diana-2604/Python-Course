# Python classes allow programmers to group data and information like variables and functions
# into a single organized unit

# Classes can be organized one to a file, or
# multiple classes that share similar types of functionality can be organized into the same file

# Class Features
# Inheritance allows us to borrow from one class and use elements of that class to create another class.
# Multiple inheritance allows a class to inherit attributes from multiple classes
# Inherited or derived classes can override the base or parent classes
# All classes in Python are Objects
#
# The statements or information inside of a class are usually functions,
# but a class can also contain class variables that are specific to the class and usable throughout the entire class.
#
# There are also variables called instance variables
# and those variables are specific to any Objects that are created by the class

# The init method
# The __init__ method sets attributes for an object at object creation; is a constructor
# Generally used to set default state of object when it is created
# The __init__ method is the first method for a class

# The Self Variable
# The self variable in Python represents an instance of a class, and specifically
# it references the instance of the class that has been created.
# We use self in order to make available all of the attributes to the methods throughout the class.

# Creating a Custom Class in Python

class Person:
    def __init__(self, firstname, lastname, health, status):
        # In order to be able to use the __init__ method, we need to create what are called the attributes.
        # The attributes are the characteristics that each Object can have.
        self.firstname = firstname
        self.lastname = lastname
        self.health = health
        self.status = status

    def introduce(self):
        print("Hi, I'm {} {}.".format(self.firstname, self.lastname))

    def emote(self):
        emotion = random.randrange(1, 3)

        if emotion == 1:
            print("{} is happy today".format(self.firstname))

        elif emotion == 2:
            print("{} is sad right now".format(self.firstname))

    def health_check(self):
        if self.health == 100:
            print("{} is totally healthy!".format(self.firstname))

        elif self.health >= 76:
            print("{} is a little tired today.".format(self.firstname))

        elif self.health >= 51:
            print("{} feels unwell.".format(self.firstname))

        elif self.health >= 40:
            print("{} goes to the doctor".format(self.firstname))

        else:
            print("{} is unconscious.".format(self.firstname))


Maria = Person("Maria", "Gutierrez", 100, status=True)
Lola = Person("Lola", "Brown", 45, status=True)
Rey = Person("Rey", "Jones", 88, status=False)
Lee = Person("Lee", "Williams", 72, status=True)

print("{} is my friend? {}".format(Maria.firstname, Maria.status))
print("{} is my friend? {}".format(Lola.firstname, Lola.status))
print("{} is my friend? {}".format(Rey.firstname, Rey.status))
print("{} is my friend? {}".format(Lee.firstname, Lee.status))

Maria.introduce()
Lola.introduce()
Rey.introduce()
Lee.introduce()

Maria.health_check()
Lola.health_check()
Rey.health_check()
Lee.health_check()
