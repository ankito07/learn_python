"""Functional programming is a programming paradigm that treats computation as the evaluation of mathematical
functions and avoids changing state and mutable data. Python, while primarily an imperative and object-oriented
language, also supports functional programming concepts.

In functional programming, the focus is on writing functions that take input arguments and return outputs without any
side effects. This means that a function's behavior is solely determined by its input, and it doesn't modify any
external state or data. """


# map() applies a function to each item in an iterable and returns an iterator of the results.

def multiply_by2(item):
    return item * 2


print(list(map(multiply_by2, [1, 2, 3])))


# filter() filters elements of an iterable based on a given function's condition.

def check_odd(item):
    return item % 2 != 0


print(list(filter(check_odd, [1, 2, 3])))

# zip(): Takes multiple iterables

names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 22]

# Using zip to combine names and ages into pairs
name_age_pairs = list(zip(names, ages))

print(name_age_pairs)  # Output: [('Alice', 25), ('Bob', 30), ('Charlie', 22)]

# reduce()
"""Applies a function cumulatively to the items of an iterable, reducing it to a single value. Note:
Starting from Python 3, to reduce() function is no longer a built-in function and must be imported from the
functools module."""

from functools import reduce


def multiply(x, y):
    print(x, y)
    return x * y


numbers = [1, 2, 3, 4, 5]

# Using reduce and the multiply function to calculate the product of all elements in the list
product = reduce(multiply, numbers, 2)

print(product)  # Output: 120 (1 * 2 * 3 * 4 * 5)

# Lambda expression
"""A lambda expression, also known as a lambda function, is an anonymous function in Python. Unlike regular functions 
defined using the def keyword, lambda expressions are defined using the lambda keyword and are typically used for 
short, simple functions that don't require a full function definition. """

# Syntax: lambda arguments: expression, in map() above we saw how can we map each item in iterable and multiply it by 2
# with lambda we are going to do the same thing with only one line.

print(list(map(lambda item: item * 2, [1, 2, 3])))
print(reduce(lambda x, y: x * y, [1, 2, 3]))

# Exercise : List Sorting

a = [(0, 2), (4, 3), (10, -1), (9, 9)]
a.sort(key=lambda x: x[1])
print(a)

# Comprehensions in python
"""List, set, and dictionary comprehensions are concise and expressive ways to create lists, sets, and dictionaries 
in Python. They allow you to generate these data structures using a single line of code with a compact syntax. """

# List Comprehension:

# Syntax : new_list = [expression for item in iterable if condition]

# Using list comprehension to create a list of squares from 1 to 5
squared_numbers = [x ** 2 for x in range(1, 6)]

print(squared_numbers)  # Output: [1, 4, 9, 16, 25]

# Set Comprehension:

# Syntax : new_set = {expression for item in iterable if condition}

# Dictionary Comprehension:

# Syntax : new_dict = {key_expression: value_expression for item in iterable if condition}

simp_dict = {
    'a': 2,
    'b': 4,
    'c': 6,
    'd': 7
}
# Using dictionary comprehension to create a dictionary mapping numbers to their squares from 1 to 5
number_square_dict = {key: value ** 2 for key, value in simp_dict.items() if value % 2 == 0}

print(number_square_dict)  # Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
