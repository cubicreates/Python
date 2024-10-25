# First Python Program
print("Hello World!")

# Variables
a = 75
print(a)

# Id functions --> gives the memory location of the variable
var1 = "Adit Ghosh"
print(id(var1)) # Answer 1 (var1 = 34) --> 140710766243288
                # Answer 2 (var1 = "Adit Ghosh") --> 1692649809264 and ever changing

# Comments
# This is how you comment.

# Datatypes in python
type1 = 23
type2 = 23.3
type3 = "Adit Ghosh"

t1 = type(type1)
t2 = type(type2)
t3 = type(type3)

print(type1)
print(t1)

print(type2)
print(t2)

print(type3)
print(t3)

# Input Function in Python
user_input = input("Enter your name: ")
print(user_input)