# How does Python works? Python code that we write goes to python interpreter gets converted from human-readable to
# machine codes i.e. 0's and 1's and then gets executed using a compiler.

# Fundamental Data Types in Python

# int
# float
# bool
# str : '' -> for words, "" ->  for sentence, ''' -> for long paragraphs
# list
# tuple
# set
# dict
# complex

# Classes -> custom types

# Specialized Data Types

# Arithmatic operations in python
print(type(2 + 4))
print(type(2 / 4))
print(2 ** 3)
print(5 // 4)
print(6 % 4)

# Math functions

print(round(3.1))  # rounding off
print(abs(-20))  # absolute value
# Many more useful functions exists refer to 'python math functions documentation'

# Operator precedence((), **, * /, + -)
print((20 - 3) + 2 ** 2)

# complex

print(bin(5))
print(int('0b101', 2))

# Variables : Can store varying values. (Advisable syntax to declare a variable -> snake_case, should start with
# lowercase or underscore and are case-sensitive)

_my_iq = 200
user_age = _my_iq / 4 + 2
print(user_age)

# Constants : Cannot store varying values, value remains the same.
PI = 3.14
print(PI)

# Augmented assignment operator
my_value = 10
my_value += 2  # shorthand for 'my_value = my_value + 2'
print(my_value)

# Here we take user's name as input store it in name variable and then print it.
name = input("Hey, What is your Name?\n")  # '\n' is to move to new-line
print("Hey, " + name)  # string concatenation
