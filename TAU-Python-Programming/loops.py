# A loop is a useful construct for when you'd like to repeat the same actions any number of times
# A for loop is useful when you'd like to iterate over each item in a list

fruits = ["apple", "orange", "pears", "cherries", "grapes"]

for fruit in fruits:
    print("Would you like {} ?".format(fruit))

# looping over a range of numbers
for number in range(1, 11):
    print("Number {}".format(number))

# A while loop will run any time a condition remains true
temp_f = 40
while temp_f > 32:
    print("The water is {} degrees.".format(temp_f))
    temp_f -= 1

# You can control the flow of a loop with some loop statements. Python includes break, continue, and pass.
# break - to end the loop and go to the next statement in the program outside the loop
# temp_f = 40
# while temp_f > 32:
#     print("The water is {} degrees.".format(temp_f))
#     temp_f -= 1
#     if temp_f == 33:
#         break

# continue - to skip the current part of the loop and move to the next part of the loop
# for number in range(1, 11):
#     if number == 7:
#         print("We're skipping number 7.")
#         continue
#     print("This is the number {}.".format(number))

# pass - to skip any part of the loop where "pass" appears - best used for testing code
# for number in range(1,11):
#     if number == 3:
#         pass
#     else:
#         print("The number is {}.".format(number))
