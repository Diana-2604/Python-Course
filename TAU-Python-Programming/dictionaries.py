# Dictionaries are a type of Python data collection that stores the data in key/value pairs
# The keys are generally made of Strings, integers, or tuples, and need to be both unique and immutable
# The values can be set to any data type and any number of key/value pairs can be contained in a dictionary
# You can make an empty dictionary by assigning a dictionary name with nothing in the curly braces
# or your dictionary can contain millions of entries
# Dictionaries are mutable and can be changed using the Python dictionary methods
# As of Python 3.7, the order of a dictionary can be maintained

# Dictionaries are created with curly braces and each key is separated from each value by a colon.
# Each key/value pair is separated from each other key/value pair with a comma

years = {"Diana": 1998, "Ruslan": 1993}

# Python Dictionary Methods
# .get method can return the value of one of the keys in the dictionary
stuff = {"food": 15, "energy": 100, "enemies": 3}
print(stuff.get("food"))  # 15

# The items method takes the name of the dictionary and outputs a view of the key/value pairs of the entire dictionary
print(stuff.items())

# The keys method returns a view of all of the keys in the dictionary
print(stuff.keys())

# The popitem method allows us to remove the last item in a dictionary
print(stuff.popitem())  # ('enemies', 3)
print(stuff)

# The setdefault method allows us to see what the value is of a key that is in the dictionary,
# to set a default value when a key is not in the dictionary and
# to add that value to the dictionary.
print(stuff.setdefault("food"))
print(stuff)
print(stuff.setdefault("friends", 123))
print(stuff)

# We can update existing items and add new items at the same time with the update method.
new_items = {"food": 3, "rocks": 4, "arrows": 18}
stuff.update(new_items)
print(stuff)

# you can add items directly to the update method in order to use it
stuff.update(food=450, cookies=6)
print(stuff)
