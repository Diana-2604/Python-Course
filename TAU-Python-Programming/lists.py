# A Python list is a collection of items
# List can contain any/all data types in a single list
# List can contain other collections (lists, dictionaries, tuples) as list items
# Lists are mutable (items can be added, removed, changed)
# Lists maintain order so you can use index to find an item
fruits = ["peaches", "pears",  "apples"]
years = [3, "1998", 2.5, 987, "1994"]

print(fruits, years)

# List Method: Append
# With the append method, I use the name of the list; .append and then I can add a single item to the list
fruits.append("oranges")
print(fruits)

# List Method: Extend
# extend the list with another list by adding multiple items to a list
fruits.extend(years)
print(fruits)

# List Method: Remove
# take an item out of a list by using the exact item match that you want to remove
fruits.remove("oranges")
print(fruits)

# List Method: Pop
# remove an element by index
fruits.pop(0)
print(fruits)
# access the last item in the list
fruits.pop(-1)
print(fruits)

# List Method: Sort
# the sort method can only be used with lists of like types
# In a numbers list, you can combine integers and floating-point numbers and they'll be sorted
numbers = [5, 1928, 4, 17, 68, 73.76, 20.458]
numbers.sort()

print(numbers)

# Checking Membership in a List
# Python has a function called in and this function allows us to check membership

fruits = ["peaches", "apples", "pears", "apples", "apples"]
print("apple" in fruits)  # false
print("apples" in fruits)  # true

# check membership and the number of items with the count function
print(fruits.count("apples"))

# check membership as well as the index position using the index function
print(fruits.index("apples"))
