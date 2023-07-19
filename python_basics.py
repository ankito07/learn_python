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

# Type Conversion
a = str(100)
b = int(a)
c = type(b)
print(type(int(str(100))))

# Escape Sequence
weather = "It's a sunny day"
temperature = "It\'s\t\"kind of\" warm"
print(weather + '\n' + temperature)

# Formatted strings
name = 'Tom'
age = 55
print(f'Hi, {name}. You are {age} year\'s old')
print('Hi {}. You are {} \"years\" old'.format(name, age))  # Old deprecated way, used till python 2.0

# String index
name = "Hey my name is Tom"
print(name[0])
name = '012345678'
# [start:stop:step-over]
print(name[0:3])  # this is referred as range(string slicing)
print(name[0:3:2])
print(name[::2])
print(name[::-1])  # negative is used to refer to the index of end of the string

# Immutability : Strings in python are immutable

# Python built-in function refer to python docs and some we have used above like abs(), round()
greet = "hellooo"
print(len(greet))
print(greet[0:len(greet)])
print(greet.split('o'))  # splits the string when it encounters letter 'o'
print(greet.capitalize())  # capitalize first letter in the given string
print(greet.find('oo'))  # finds the 'oo' in the string and prints it occurrence
greet2 = greet.replace("lo", "it")
print(greet2)

# booleans : It's either 'True' or 'False'
name = 'Tom'
is_happy = True  # value is 1
does_workout = False  # value is 0
