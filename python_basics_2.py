# Once you are done with python_basics_1 and learned all the basic elements of python coding now it's time to enhance
# you skill with performing useful actions and giving logical reasoning on your python code.


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
