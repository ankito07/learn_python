import re  # This is used below when you will learn about Regular expression ignore if you have just started.

"""Learn about decorators, Error handling, Generators, File I/O and Regular expressions in python"""

# Decorators

"""Decorators are a powerful feature that allow you to modify or extend the behavior of functions or methods without 
changing their actual code. Decorators are often used for aspects like logging, authentication, caching, 
access control, etc., and they help you keep your code clean and organized """


# Syntax : To define a decorator, you use the @ symbol followed by the decorator name

def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")

    return wrapper


@my_decorator
def say_hello():
    print("Hello!")


say_hello()

"""In this example, my_decorator is a function that takes another function func as an argument. It defines a nested 
function wrapper, which adds behavior before and after calling func. The @my_decorator above say_hello() is 
equivalent to say_hello = my_decorator(say_hello). (You can also use decorators with arguments.)"""


# Decorator Pattern


def the_decorator(func):
    def wrap_func(greeting, emoji):
        print("***********")
        func(greeting, emoji)
        print("***********")

    return wrap_func


@the_decorator
def hello(greeting, emoji):
    print(greeting, emoji)


hello('Hi', ':-)')

# Error handling

"""Error handling, also known as exception handling, is a crucial aspect of writing robust and reliable code. In 
Python, exceptions are used to handle runtime errors or exceptional conditions that may occur during the execution of 
a program. By handling exceptions properly, you can gracefully recover from errors, avoid program crashes, 
and provide meaningful error messages to users. """

try:
    age = int(input("Enter a number: "))
    result = 10 / age
    print("Result:", result)
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
except ValueError:
    print("Error: Invalid input. Please enter a valid number.")
else:
    print('Thank You')
finally:
    print("This will always execute, no matter what.")

# Generators

"""Generators are a type of iterable in Python that allow you to generate a sequence of values one at a time, 
on-the-fly, instead of creating the entire sequence upfront in memory. This makes generators memory-efficient and 
particularly useful for dealing with large datasets or infinite sequences. """


def countdown(n):
    while n > 0:
        yield n
        n -= 1


# Using the generator function
for num in countdown(5):
    print(num)

"""Generator Expressions: Generator expressions are similar to list comprehensions, but they create generator objects 
instead of lists. They are written within parentheses () instead of square brackets []. Like generator functions, 
generator expressions also generate values on-the-fly and are memory-efficient. """

even_numbers = (num for num in range(1, 11) if num % 2 == 0)

# Using the generator expression
for num in even_numbers:
    print(num)

# Modules

"""In Python, a module is a file that contains Python code, including functions, classes, and variables, that can be 
imported and used in other Python programs. Modules allow you to organize your code into separate files, 
making it easier to manage and reuse. 

When you import a module into your Python program, you gain access to all the functions, classes, and variables 
defined in that module. This makes your code more modular, easier to maintain, and less prone to naming conflicts. """

# Suppose you have a file named my_module.py

# Now, in another Python file, you can import and use the functions from my_module: import my_module

# To import only specific functions from a module, you can use the form keyword: from my_module import <your_function>

# Packages

"""A package is a collection of one or more Python modules organized in directories. Packages allow you to create a 
hierarchy of modules and sub-packages to create more extensive and well-structured projects. A package typically 
includes an __init__.py file in its directory, which makes Python treat the directory as a package. You can think of 
a package as a directory that contains multiple modules and an __init__.py file to make it a package, 
whereas a module is a single file with Python code. """

# __name__

"""The __name__ is a built-in Python variable that holds the name of the current module. When a Python script is 
executed, the __name__ variable in that script is set to '__main__'. However, when a script is imported as a module 
into another script, the __name__ variable in the imported module is set to the name of the module. """

# Scenario to understand if __name__ == "__main__"

"""The block inside the if __name__ == "__main__": conditional is not executed when my_module.py is imported into 
main.py different python file. It only executes when you run my_module.py directly as the main script. """

# File Input/Output (I/O)

"""File Input/Output (I/O) in Python allows you to interact with files on your computer. It enables reading data from 
files (File Input) and writing data to files (File Output). Python provides several built-in functions and methods to 
work with files, making file I/O straightforward. """

# Opening a File:

# Open a file in read mode
file = open('example.txt', 'r')

# Reading from a File:

# Read the entire file contents
contents = file.read()
print(contents)

# Read one line at a time
line = file.readline()
print(line)

# Read all lines into a list
lines = file.readlines()
print(lines)

# Writing to a File:

# Open a file in write mode (creates a new file or overwrites the existing one)
file = open('output.txt', 'w')

# Write to the file
file.write('This is a line of text.')

# Appending to a File:

# Open a file in append mode
file = open('output.txt', 'a')

# Append to the file
file.write('This is another line of text.')

# Closing the file
file.close()

"""Using "with" Statement: To ensure that the file is automatically closed when you're done with it, it's a good 
practice to use the with statement. The with statement handles the opening and closing of the file for you, 
even if an exception occurs. """

# Using 'with' statement to open and automatically close the file
with open('example.txt', 'r') as file:
    contents = file.read()
    print(contents)
# The file is automatically closed outside the 'with' block


# Remember to handle exceptions when working with files, as they may not always exist or be accessible.

# Regular Expression

"""Regular expressions (regex) in Python are a powerful tool for pattern matching and text manipulation. They allow 
you to search, match, and extract specific patterns from strings. The re module in Python provides support for 
regular expressions. """

# Here are some commonly used functions and methods in the re module:

# re.search(pattern, string): Searches for the pattern in the entire string and returns a match object if found. It
# stops at the first occurrence of the pattern.

pattern = r'apple'
text = "I have an apple and a banana."

match = re.search(pattern, text)
if match:
    print("Pattern found:", match.group())
else:
    print("Pattern not found.")

# re.match(pattern, string): Searches for the pattern only at the beginning of the string and returns a match object
# if found.

pattern = r'banana'
text = "I have an apple and a banana."

match = re.match(pattern, text)
if match:
    print("Pattern found:", match.group())
else:
    print("Pattern not found.")

# re.findall(pattern, string) : Returns all occurrences of the pattern in the string as a list.

pattern = r'\d+'  # Matches one or more digits
text = "I have 123 apples and 456 bananas."

matches = re.findall(pattern, text)
print("Matches:", matches)

# re.finditer(pattern, string): Returns an iterator yielding match objects for all occurrences of the pattern in the
# string. python

pattern = r'\w+'  # Matches one or more word characters
text = "Hello, World!"

matches = re.finditer(pattern, text)
for match in matches:
    print("Match:", match.group())

# re.sub(pattern, replacement, string): Replaces occurrences of the pattern with the specified replacement string.

pattern = r'\d+'
text = "I have 123 apples and 456 bananas."

replaced_text = re.sub(pattern, 'X', text)
print("Replaced text:", replaced_text)

# Exercise regular expression :

"""A password checker program that validates if a password meets the following criteria:

At least 8 characters long.
Contains at least one lowercase letter.
Contains at least one uppercase letter.
Contains at least one digit.
Contains at least one special character from the set @#$%^&*!.
We'll use regular expressions to implement the password validation:"""


def is_valid_password(password):
    # Check length (at least 8 characters)
    if len(password) < 8:
        return False

    # Check if it contains at least one lowercase letter
    if not re.search(r'[a-z]', password):
        return False

    # Check if it contains at least one uppercase letter
    if not re.search(r'[A-Z]', password):
        return False

    # Check if it contains at least one digit
    if not re.search(r'\d', password):
        return False

    # Check if it contains at least one special character
    if not re.search(r'[@#$%^&*!]', password):
        return False

    return True


def main():
    password = input("Enter your password: ")
    if is_valid_password(password):
        print("Password is valid.")
    else:
        print("Password is invalid. Please make sure it has at least 8 characters, "
              "including at least one lowercase letter, one uppercase letter, one digit, "
              "and one special character (@#$%^&*!).")


if __name__ == "__main__":
    main()
