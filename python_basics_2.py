"""
Once you are done with python_basics_1 and learned all the basic elements of python coding now it's time to enhance
your skill with performing useful actions and giving logical reasoning on your python code.
"""


# Conditional-logic

is_eighteen_plus = False
is_licensed = True

# if-else is a condition statement, if condition is 'True' it gets executed, if condition is 'False',
# elif is 'True' this executes or
# else executes, when neither 'if' nor elif is true. To execute any code within if,elif or else
# condition make sure it has correct indentation or some say spacing, use tab after initiating the condition.

if is_eighteen_plus:
    print("Yes, You are old enough to drive")
elif is_licensed:
    print("You can drive")
else:
    print("Sorry, No you cannot drive")

# Ternary Operator : also called as conditional expression this gets evaluated to a value based on condition.
# in-short simplified form of if-else conditioning

is_friend = False
can_message = "Message allowed" if is_friend else "you cannot message, the person is not in your friend list"
print(can_message)

# Short Circuiting

is_friend = False
is_user = True

if is_friend and is_user:  # and is an operator which checks both LHS and RHS is 'True' to execute the statement.
    print("Sorry, not your friend")
elif is_friend or is_user:  # or is another operator that checks either LHS or RHS in the conditional statement is true.
    print("Not your friend but as a user can send anonymous message")

# Logical operator
# >,<,==, !=, and, or, not

age = 20
height = 165
if age > 18:
    print("You are eligible to vote")

print(age == 20)
print(age != 20)  # not equal to

# For loops : this is a powerful logic which keeps on getting executed unless the given condition gets false.
num = [40, 56, 70, 'hello']

for item in num:  # item is iterator which iterates on the given value until it reaches the end or condition is false
    print(item)

# Nested looping : loop inside a loop
for item in (1, 2, 3, 4):
    for x in ['a', 'b', 'c', 'd']:
        print(item, x)

# iterable - list, dictionary, tuple, set, string
# iterator - one by one check each item in the given iterable

# Iterating over dictionary
user = {
    'name': 'Stark',
    'age': 57,
    'can_dance': False
}

for item in user:
    print(item)

for item in user.values():
    print(item)

for item in user.keys():
    print(item)

for key, value in user.items():
    print(key, value)

for item in range(100):
    print(item)

for item in range(0, 10, 2):  # start, stop, step over value
    print(item)

for _ in range(10, 0, -1):
    print(_)

for _ in range(3):
    print(list(range(10)))

# enumerate() : method adds a counter to an iterable and returns it in a form of enumerating object

for i, char in enumerate("Hellooo"):
    print(i, char)

# While loops : with the while loop we can execute a set of statements as long as a condition is true. A while loop may
# have an optional else block. Here, the else part is executed after the condition of the loop evaluates to False.

i = 0
while i < 50:
    print(i)
    i += 1
print("Execution completed")

# Useful use case which can be used to develop a chatbot type application.
while True:
    user_response = input("Hi, say something: ")
    if user_response == 'bye':
        break

# break, continue, pass

for i in [1, 2, 3, 4, 5]:
    if i == 2:
        continue  # skips the given condition
    elif i == 4:
        break  # stops the iteration as the condition become true
    print(i)

for i in [1, 2, 3]:
    # will code later
    pass


# Functions : A function is a block of code which only runs when it is called. It is initiated with 'def' keyword
# You can pass data, known as parameters, into a function.
# A function can return data as a result.
def my_function():
    print("Hello")


my_function()
my_function()  # a function can be called and executed multiple times


# Arguments and Parameters : A parameter is the variable listed inside the parentheses in the function definition.
# An argument is the value that are sent to the function when it is called.

def calculator(a=1, y=1):
    result = a + y
    return result


num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print(calculator(num1, num2))
print(calculator())


# Methods vs Functions : A function doesn't need any object and is independent, while the method is a function,
# which is linked with any object. We can directly call the function with its name, while the method is called by the
# object's name. Function is used to pass or return the data, while the method operates the data in a class.

# input(), print(), max(), min() : These are functions
# capitalize(), lower() : These are methods

# Docstring

def doc_string_func():
    """
    Info: This function is used to learn docstring in python
    :parameter : You can write about what parameter this function is accepting here
    :return : Write what is being returned
    """
    print("hello")


doc_string_func()


# *args : argument, **kwargs : keyword arguments
# Rule : params, *args, default params, **kwargs
def sum_func(*args):
    return sum(args)  # args here are tuple of argument


print(sum_func(1, 2, 3, 4))


def sum_func_again(**kwargs):
    return sum(kwargs.values())  # kwargs here are dictionary of arguments


print(sum_func_again(number1=25, number2=25))


# Exercise to find highest even value in the given list
def highest_even(li):
    even = []
    for items in li:
        if items % 2 == 0:
            even.append(items)
    return max(even)


print(f" The highest even value in the given list is: {highest_even([10, 2, 3, 4, 8, 11])}")

# Walrus operator : ":="
word = "preoperational"

if (n := len(word)) > 5:
    print(f"given word is too long has {n} elements")

# Exercise to reduce a variable by one from last index in each iteration
while (n := len(word)) > 1:
    print(n)
    word = word[:-1]

# Global variable and local variable

global_var = 5


def local_variable():
    local_var = 7
    return local_var


print(global_var)
print(local_variable())
