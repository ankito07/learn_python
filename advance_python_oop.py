"""
In this python tutorial we will learn about the 'OOP' paradigm, which stands for Object-Oriented Programming.
Object-oriented programming (OOP) is a computer programming model that organizes software design around data,
or objects, rather than functions and logic. An object can be defined as a data field that has unique attributes and
behavior.
"""

# class & objects
"""A class is considered as a blueprint of objects. We can think of the class as a sketch (prototype) of a house. It 
contains all the details about the floors, doors, windows, etc. Based on these descriptions we build the house. House 
is the object. """

# init
"""The __init__ method in Python is a special method used in classes, and it is commonly referred to as the 
constructor method. It is automatically called when an object (instance) of the class is created. The primary purpose 
of the __init__ method is to initialize the attributes (variables) of the class instance. """

# self
"""The self parameter is used to set instance attributes during the object's initialization. Within the __init__ 
method, you can use self to assign values to instance variables, making them specific to each instance of the class. """

# @classmethod
"""The first parameter of a class method is cls, which refers to the class itself. It is similar to using self for 
instance methods, but cls is used for class-level operations. 

Class methods are bound to the class and can be called on the class itself (e.g., MyClass.class_method_name()) or on 
an instance of the class (e.g., instance.class_method_name()). 

Since class methods are not bound to specific instances, they cannot access or modify instance-specific data (
attributes). Instead, they can work with class-level data (class attributes) or perform operations that apply to the 
class as a whole. """

# @staticmethod
"""The @staticmethod decorator is used to indicate that the method is a static method. It does not require self or 
cls as the first parameter. 

Static methods are not bound to the instance or the class and don't have access to instance or class-level 
attributes. They can only access other static members within the class. 

Static methods are defined within a class primarily for code organization purposes, as they are logically related to 
the class but do not rely on instance-specific or class-specific data. """


class PlayerCharacter:
    # Class object attribute
    membership = True

    def __init__(self, name='anonymous', age=0):
        if age > 18:
            self.name = name
            self.age = age

    def speak(self):
        print(f'My name is {self.name}')

    @classmethod
    def goal_tracker(cls, match1, match2):
        return match1 + match2

    @classmethod
    def goal_tracker2(cls, match1, match2):
        return cls('Teddy', match1 + match2)

    @staticmethod
    def goal_tracker3(match1, match2):
        return match1 + match2


player1 = PlayerCharacter('John', 23)  # object 1 of class PlayerCharacter
player2 = PlayerCharacter('Tom', 29)  # object 2 of class PlayerCharacter
player1.club = 'striker'
player2.club = 'defender'

print(player1.name, player1.age, player1.club, player1.membership)
print(player2.name, player2.age, player2.club, player2.membership)
print(player1.speak())
print(player1.goal_tracker(45, 78))
print(PlayerCharacter.goal_tracker(23, 67))
player3 = PlayerCharacter.goal_tracker2(10, 10)  # object 3 of PlayerCharacter using @classmethod decorator
print(player3.age)
print(PlayerCharacter.goal_tracker3(3, 9))

# Encapsulation
"""Encapsulation is one of the fundamental principles of object-oriented programming (OOP) and refers to the idea of 
bundling data (attributes) and methods that operate on that data within a single unit, called a class. It provides a 
way to control access to the data and behavior of an object, preventing direct access to internal details from 
outside the class. """

# Abstraction
"""Abstraction is a fundamental concept in object-oriented programming (OOP) that focuses on representing the 
essential features of an object while hiding unnecessary details. It provides a way to create a simplified model of 
an object or system, emphasizing only the relevant characteristics and behavior, and abstracting away the 
complexities. """

# Private vs Public variables
# Public Variables:
"""A public variable is accessible from outside the class, meaning it can be accessed, modified, and used directly by 
external code. In Python, all class attributes are public by default."""

# Private Variables:
"""A private variable is not accessible from outside the class. In Python, you can indicate a private variable by 
prefixing its name with two underscores (__). Syntax : self.__private_var = 12"""


class PublicPrivateVar:
    def __init__(self):
        self.public_var = 42  # This is a public variable


obj = PublicPrivateVar()
print(obj.public_var)  # Output: 42
obj.public_var = 10  # Modifying the public variable
print(obj.public_var)  # Output: 10

# Inheritance
"""Inheritance is a fundamental concept in object-oriented programming (OOP) that allows a new class to inherit the 
characteristics (attributes and methods) of an existing class. The existing class is called the "base class" or 
"parent class," and the new class is called the "derived class" or "child class." 

Inheritance enables the derived class to reuse the code and functionality defined in the base class, promoting code 
re-usability and hierarchical organization of classes. The derived class can add additional attributes and methods or 
override the ones inherited from the base class to tailor its behavior according to its specific needs. 

Types of Inheritance: Inheritance supports different types, including single inheritance (one base class), 
multiple inheritance (more than one base class), and multi-level inheritance (a derived class inherits from another 
derived class). 

Overriding Methods: If a method is present in both the base class and the derived class, the version in the derived 
class can override the one in the base class. This allows the derived class to have its implementation of the method, 
tailoring its behavior as needed. """


# Base class
class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        pass


# Derived class (inherits from Animal)
class Dog(Animal):
    def make_sound(self):
        return "Woof!"


# Derived class (inherits from Animal)
class Cat(Animal):
    def make_sound(self):
        return "Meow!"


# Creating instances of the derived classes
dog = Dog("Buddy")
cat = Cat("Whiskers")

# Using methods from the base class
print(dog.name)  # Output: Buddy
print(cat.name)  # Output: Whiskers

# Using methods overridden in the derived classes
print(dog.make_sound())  # Output: Woof!
print(cat.make_sound())  # Output: Meow!

# Polymorphism
"""Polymorphism is a fundamental concept in object-oriented programming (OOP) that allows objects of different 
classes to be treated as if they belong to a common superclass or share a common interface. It enables a single 
interface to represent multiple types or classes, providing a unified way to interact with various objects regardless 
of their specific implementations. 

Compile-time Polymorphism (Static Polymorphism):

Also known as static polymorphism, compile-time polymorphism occurs during the compile-time of the program.
It is achieved through method overloading and operator overloading.

Run-time Polymorphism (Dynamic Polymorphism):

Also known as dynamic polymorphism, run-time polymorphism occurs during the run-time of the program.
It is achieved through method overriding and is based on the concept of inheritance and virtual functions (methods)."""


class Animal:
    def make_sound(self):
        # To explain polymorphism
        pass


class Dog(Animal):
    def make_sound(self):
        return "Woof!"


class Cat(Animal):
    def make_sound(self):
        return "Meow!"


# Function that interacts with the common interface (Animal)
def animal_sound(animal):
    print(animal.make_sound())


# Creating instances of the derived classes
dog = Dog()
cat = Cat()

# Using polymorphism to call the same method on different objects
animal_sound(dog)  # Output: Woof!
animal_sound(cat)  # Output: Meow!

# super()
"""super() is a built-in function used primarily in the context of inheritance. It provides a way to call a method or 
access an attribute in a base class from within a derived class. The super() function is especially useful when a 
derived class overrides a method from its base class and still wants to utilize the behavior of the overridden 
method. """


class Parent:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello, I am {self.name}.")


class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)  # Call the __init__ method of the base class
        self.age = age

    def greet(self):
        super().greet()  # Call the greet method of the base class
        print(f"I am {self.age} years old.")


child = Child("Alice", 5)
child.greet()

# Output:
# Hello, I am Alice.
# I am 5 years old.

"""In this example, Child is a derived class that inherits from the Parent base class. The Child class overrides the 
greet() method, but it still wants to use the behavior defined in the Parent class. By using super(), the Child class 
can call the greet() method of the Parent class before adding additional functionality in its own greet() method. """

# Dunder methods
"""Dunder methods, short for "double underscore methods," are special methods in Python that have names surrounded by 
double underscores on both sides, such as __init__, __str__, __add__, __len__, etc. These methods play a crucial role 
in defining the behavior of objects, enabling built-in functionalities, operator overloading, and customization of 
various operations for user-defined classes. 

Dunder methods are also known as magic methods or special methods because they provide special behaviors that are 
automatically invoked by the Python interpreter in response to specific operations or actions performed on objects. """

"""Here are some common dunder methods and their purposes:

__init__(self, ...) - The constructor method, automatically called when an object is created. It initializes the 
object's attributes. 

__str__(self) - The string representation method, called by the str() function or print() to display a human-readable 
string representation of the object. 

__repr__(self) - The "official" string representation method, called by the repr() function to provide an unambiguous 
representation of the object for debugging purposes. 

__add__(self, other) - The addition method, invoked when the + operator is used to add two objects.

__sub__(self, other) - The subtraction method, invoked when the - operator is used to subtract two objects."""


class Toy:
    def __init__(self, color, age):
        self.color = color
        self.age = age

    def __len__(self):
        return 5


action_figure = Toy('red', 1)
print(len(action_figure))

# MRO
"""Method Resolution Order (MRO) is a critical concept in Python's multiple inheritance. It determines the order in 
which methods are looked up and called when a method is invoked on an object that is derived from multiple base 
classes. Python uses a depth-first search algorithm to determine the MRO. """
