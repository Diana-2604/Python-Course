# Multiple inheritance is when one class inherits from multiple classes
# and is able to use attributes and methods from both classes

# There are 2 ways to do multiple inheritance in Python.
# The first way requires a bit more maintenance. However, it's easier to see exactly what's happening.
# The second way is to use the super method as we did with a single inheritance.
# However, this method can be complicated and quite confusing

# Parent class 1
class Item():
    def __init__(self, sku):
        self.sku = sku

    def print_sku(self):
        print("The sku is {}.".format(self.sku))


# Parent class 2
class Garment():
    def __init__(self, section, kind):
        self.section = section
        self.kind = kind

    def print_garment(self):
        print("The garment is in section {}, {}.".format(self.section, self.kind))


# Child Class
class Shirts(Item, Garment):

    def __init__(self, sku, section, kind, name, color):
        self.name = name
        self.color = color

        Item.__init__(self, sku)
        Garment.__init__(self, section, kind)

    def print_shirt(self):
        print("{} {} on sale!".format(self.color, self.name))


Blouse = Shirts("00001", 43, "Tops", "Formal Blouse", "White")
Blouse.print_sku()
Blouse.print_garment()
Blouse.print_shirt()
