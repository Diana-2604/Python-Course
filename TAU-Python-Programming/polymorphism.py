# Polymorphism occurs when we want to allow the child class to have a method
# with the same name and a similar implementation as the parent class and
# we wish for that method you override the parent class method.
# Let's override the introduce method

# Parent class
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

Maria.introduce()
Lola.introduce()
Rey.introduce()
Lee.introduce()

# Child class
class Enemy(Person):
    def __init__(self, weapon, firstname, lastname, health, status):
        super().__init__(firstname, lastname, health, status)
        self.weapon = weapon

    # When we make a method in the child's class with the same name as the one in the parent class,
    # the child class method overrides the parent class method.
    def introduce(self):
        print("I'm {}, and I'm your mortal enemy!!!".format(self.firstname))

    def hurt(self, other):
        if self.weapon == 'rock':
            other.health -= 10
        elif self.weapon == 'stick':
            other.health -= 5
        print("{}, your health is now {}!".format(other.firstname, other.health))

    def insult(self, other):
        if other.health <= 80:
            print("{}, you are tired and weak!".format(other.firstname))

    def steal(self, other):
        print("ha ha ha, {}, I have your stuff!".format(other.firstname))
        if other.status == True:
            other.status = False


Alex = Enemy('rock', 'Alex', 'Wayne', 75, status=False)
Alex.introduce()