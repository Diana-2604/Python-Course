# variables can contain uppercase letters, lowercase letters, underscores
# variables are case sensitive
# multi-name variables require underscore between each of the words

number_of_cars = 23
kind_of_cars = "Ferrari"

print("There are", number_of_cars, "cars of the kind", kind_of_cars)

# strings can be enclosed in single or double quotes
# strings are immutable (operations cannot be performed)

# integers are whole numbers, mathematical operations can be performed

# floating point - fractional numbers, mathematical operations can be performed
# no need for specification of the decimal places

# python string.format()
print("There are {} cars of the kind {} in the shop".format(number_of_cars, kind_of_cars))
# format function accepts the arguments of our variables and
# transfers those arguments into the curly braces in the order that they appear in the sentence
