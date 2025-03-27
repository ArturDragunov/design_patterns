#%% oop1
# Define the Greeting class
class Greeting:
    # Constructor for the Greeting class
    def __init__(self, name):
        # Initialize the 'name' attribute with the provided value
        self.name = name

    # Define the 'say_hello' method for the Greeting class
    def say_hello(self):
        # Print a personalized greeting message using the 'name' attribute
        print(f"Hello, {self.name}!")

class BetterGreeting(Greeting) :
    # we are overwriting hello method of a parent class
    def say_hello(self): 
        # calling parent class implementation of say_hello
        super().say_hello()
        print(f"Hello, Better {self.name}!") 

# Create an object of the Greeting class, initializing it with the name 'John'
greeting = Greeting("John")
greeting.say_hello()
greeting = BetterGreeting("John")
#print both Hello, John! and Hello, Better John!
greeting.say_hello()

#%% oop2 - CLASS AGGREGATIONS
# Define the Author class
class Author:
    def __init__(self, name, birth_year):
        self.name = name
        self.birth_year = birth_year

    def get_author_info(self):
        return f"{self.name} (born {self.birth_year})"

# Define the Book class
class Book:
    # Aggregation - we are taking author object as a parameter instead of inheriting it as Book(Author)
    def __init__(self, title, publication_year, author: Author):
        self.title = title
        self.publication_year = publication_year
        self.author = author
    # referring to author attribute which we took as a parameter 
    def get_book_info(self):
        return f"'{self.title}' by {self.author.get_author_info()}, published in {self.publication_year}"

# Create an Author object
author_obj = Author("George Orwell", 1903)

# Create a Book object with the Author object as a property
book_obj = Book("1984", 1949, author_obj)

# Print the book information, which includes author information
print(book_obj.get_book_info())

#%% oop3 ABSTRACT CLASS
from abc import ABC, abstractmethod

# Define an abstract class 'Animal'
class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

    # Sound is abstract (thus we use pass). It HAS to be implemented.
    #  But description is optional -> if child class doesn't implement it,
    # it will use parent method.
    def description(self):
        # class name is Dog or Cat
        print(f"{self.__class__.__name__} says: {self.sound()}")

# Define a concrete class 'Dog' that inherits from 'Animal'
class Dog(Animal):
    # We have to implement sound! But description method is optional
    def sound(self):
        return "Woof!"
    
    def description(self):
        print(f"My little dog says: {self.sound()}")

# Define a concrete class 'Cat' that inherits from 'Animal'
class Cat(Animal):
    def sound(self):
        return "Meow!"
    # you can write it explicitly but it's not necessary - description is by default inherited from Animal
    # def description(self):
    #     # we inherit description from family class
    #     return super().description()

dog = Dog()
dog.description() # My little dog says: Woof!

cat = Cat()
cat.description() # Cat says: Meow!
#%% oop4 ENCAPSULATION
"""
Encapsulation is a fundamental OOP principle that hides internal state and requires interaction through well-defined interfaces. Your code demonstrates this well:

Data hiding: The __balance is private, preventing direct access/modification
Control access: Getters/setters control how data is accessed/modified
Input validation: Methods like set_balance() ensure data integrity by checking values
Implementation hiding: Users interact with methods without knowing internal details

Prevents unexpected state changes
Centralizes validation logic
Enables changing implementation without affecting external code
Reduces bugs from direct property manipulation
Enforces business rules (e.g., no negative balance)
"""
class BankAccount:
    def __init__(self, account_number, balance):
        self._account_number = account_number  # Protected attribute (single underscore)
        self.__balance = balance  # Private attribute (double underscore - name mangling)
        # you won't be able to access balance attribute directly using account object
        # you can change balance only with get_balance and set_balance methods

    # Getter method for the private attribute
    def get_balance(self):
        return self.__balance

    # Setter method for the private attribute
    def set_balance(self, balance):
        if balance >= 0: # if input balance is not >= 0, then we don't initialize balance
            self.__balance = balance
        else:
            print("Invalid balance")

    # Public method that uses the private attribute
    def deposit(self, amount):
        if amount > 0: # if amount is < 0, then we don't add it to balance.
            self.__balance += amount
        else:
            print("Invalid deposit amount")

    # Public method that uses the private attribute
    # the balance logic is set up inside the class and not outside
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Invalid withdrawal amount")

# Testing the encapsulation
account = BankAccount("123456", 1000)

# Accessing the protected attribute (not recommended, but possible)
print("Account number:", account._account_number)

# Accessing and modifying the private attribute through getter and setter methods
print("Initial balance:", account.get_balance())
account.set_balance(500)
print("Updated balance:", account.get_balance())

# Using public methods that internally use the private attribute
account.deposit(100)
print("Balance after deposit:", account.get_balance())
account.withdraw(50)
print("Balance after withdrawal:", account.get_balance())

#%% oop5 Interface Contract
# Same way it's created from an Abstract class. The main difference is in implementation.
# A Contract is a class WHERE ALL METHODS are abstract -> THEY MUST BE IMPLEMENTED by child classes
# While a tradional Abstract class can have abstract methods and usual ones.
# Abstract methods must be implemented and usual ones could be inherited if needed
# Abstract class can have __init__ and attributes which is not part of Contract class.
from abc import ABC, abstractmethod

# Creating a blueprint - contract for all the derivative classes. MyInterface is fully abstract,
#  you can't create an object out of it.
class MyInterface(ABC):
    @abstractmethod
    def my_method(self):
        pass

class MyClass(MyInterface):
    def my_method(self):
       print("my_method implementation in MyClass")

class AnotherClass(MyInterface):
    # by contract, my_method HAS to be implemented
    def my_method(self):
        print("my_method implementation in AnotherClass")

# Testing the implementation
# The idea of Interface Contract is that we KNOW FOR GRANTED that all the classes
# derived from MyInterface MUST HAVE my_method()
my_obj = MyClass()
my_obj.my_method()

another_obj = AnotherClass()
another_obj.my_method()

#%% oop6
from abc import ABC, abstractmethod
from typing import Type

class MyInterface(ABC):
    @abstractmethod
    def my_method(self):
        pass

class MyClass(MyInterface):
    def my_method(self):
        print("my_method implementation in MyClass")

class AnotherClass(MyInterface):
    def my_method(self):
        print("my_method implementation in AnotherClass")

class NotImplementingInterface:
    def some_method(self):
        print("I am not implementing MyInterface")

# takes as an argument object of MyInterface class
def process_my_interface(obj: MyInterface): 
    obj.my_method()
    print("The object has correctly implemented MyInterface")

# Testing the implementation
my_obj = MyClass()
process_my_interface(my_obj)

another_obj = AnotherClass()
process_my_interface(another_obj)

# This will not raise a runtime error, but static type checkers like mypy will complain
not_implementing_interface = NotImplementingInterface()
process_my_interface(not_implementing_interface)  # Static type checkers will warn about this

#%% oop7
from abc import ABC, abstractmethod

# Define an abstract class 'Shape'
class Shape(ABC):
    def __init__(self, color):
        self.color = color

    # This we want to be implemented by child classes
    @abstractmethod
    def area(self):
        pass

    # This we want to be implemented by child classes
    @abstractmethod
    def perimeter(self):
        pass

    # Make the 'description' base implementation
    def description(self):
        print(f"{self.__class__.__name__} has the color: {self.color}")    

# Define a concrete class 'Rectangle' that inherits from 'Shape'
# In Python's inheritance model, the parent class initializer isn't automatically called.
#  So when you create a Rectangle object without calling super().__init__(color),
#  the Shape.__init__ method never runs, and self.color is never set.
class Rectangle(Shape):
    # constructor with width, height and color
    def __init__(self, width, height, color):
        # we inherit color from Shape. As it's used in description, we MUST have it.
        # Otherwise, we could skip it.
        super().__init__(color) 
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


# Define a concrete class 'Circle' that inherits from 'Shape'
class Circle(Shape):
    def __init__(self, radius, color):
        super().__init__(color)
        self.radius = radius

    def area(self):
        return 3.141592653589793 * (self.radius ** 2)

    def perimeter(self):
        return 2 * 3.141592653589793 * self.radius

# Interface contract method -> we don't care what code children have
# we know for sure that they have description -> either inherited from Shape,
# OR implemented on their own.
# process_my_color is a future-proof method
def process_my_color(obj: Shape):
    obj.description()

# Create instances of concrete classes and use their methods
rectangle = Rectangle(4, 5, "red")
print(f"Rectangle area: {rectangle.area()}")
print(f"Rectangle perimeter: {rectangle.perimeter()}")
# print(f"Rectangle color: {rectangle.color}")

circle = Circle(3, "blue")
print(f"Circle area: {circle.area()}")
print(f"Circle perimeter: {circle.perimeter()}")
# print(f"Circle color: {circle.color}")

process_my_color(rectangle)
process_my_color(circle)