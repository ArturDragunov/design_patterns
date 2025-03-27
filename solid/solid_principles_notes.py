#%%
###Types of Classes###

# Inheritance: A mechanism where a new class (subclass) inherits properties and methods from an existing class (superclass). It promotes code reuse.
class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"
    
# Abstract class: Interface method - class that cannot be instantiated on its own and is meant to be subclassed.
# It can define abstract methods that must be implemented by subclasses.
# It's also named as Inheritance:Interfaces -> Interface Contract. Children will have to implement all of the abstract methods.
# In an interface class methods have no implementation. Thus, we use pass. It's blueprint for children. 
from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def area(self): # HAS TO BE IN CLASS
        return "Calculating area for Circle"
    
# Abstract class with inheritance
from abc import ABC, abstractmethod
class Shape(ABC):
    def __init__(self, color):
        self.color = color
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, color, width, height):
        super().__init__(color)
        self.width = width
        self.height = height
    def area(self): # HAS TO BE IN CLASS
        return self.width * self.height

#%% SOLID Principles in SWE -> Single Responsibility Principle (SRP)
# Violation example
"""
SRP -> A class should have only one reason to change,
meaning it should have only one primary responsibility or job.
This promotes more focused, maintainable code by keeping classes focused and modular.
The ToDoList class handles multiple responsibilities:
1.managing tasks (add_task, delete_task, remove_task)
2.handling user input (input_task, remove_task)
3.displaying tasks (display_tasks)
This violates the SRP, which states that a class should have only one reason to change."""
class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def delete_task(self, task):
        self.tasks.remove(task)

    def display_tasks(self):
        for task in self.tasks:
            print(task)

    def input_task(self):
        task = input("Enter a task: ")
        self.add_task(task)

    def remove_task(self):
        task = input("Enter the task to remove: ")
        self.delete_task(task)

# Python staticmethod is used to convert a function to a static function.
# Static methods are independent of class instances (of self),
# meaning they can be called on the class itself
# without requiring an object of the class.

# Calling the static method directly from the function
# Use static method when you have a function that belongs to
# the class logically but doesn't need to interact with the
# class or its instances (no self needed) -> input will be given from OUTSIDE

# refactored version around 3 areas
# Testability: Each class can be tested in isolation
class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def delete_task(self, task):
        self.tasks.remove(task)

class TaskPresenter:
    """
    Utility Functions: They're used for methods that are conceptually related to the class
    but don't need to modify the class's state. 
    Namespace Organization: They provide a way to group related utility functions within
    a class without creating an instance.
    """
    @staticmethod
    def display_tasks(tasks):
        for task in tasks:
            print(task)

class TaskInput:
    @staticmethod
    def input_task():
        return input("Enter a task: ")

    @staticmethod
    def remove_task():
        return input("Enter the task to remove: ")

# Example of how to use these classes together
def main():
    # Create a task manager to store tasks
    task_manager = TaskManager()

    # Use TaskInput to get a new task
    new_task = TaskInput.input_task()
    task_manager.add_task(new_task)

    # Display tasks using TaskPresenter
    TaskPresenter.display_tasks(task_manager.tasks)

    # Remove a task
    task_to_remove = TaskInput.remove_task()
    task_manager.delete_task(task_to_remove)

#%% Open/Closed Principle (OCP)
"""
Software entities (classes, modules, functions) should be open for extension but closed for modification.
This means you can add new functionality without changing existing code,
typically achieved through inheritance and interfaces.
Key Advantages:
- Follows Open/Closed Principle (OCP): Design allows extension without modification
- Provides high flexibility and extensibility for shape calculations
- Delegates area calculation responsibility to individual shape classes
- Enables seamless addition of new shapes without altering existing code
- Eliminates complex conditional logic through polymorphic behavior
"""
# Bad design
class AreaCalculator:
    def area(self, shape):
        if isinstance(shape, Circle):
            return 3.14159 * shape.radius**2
        elif isinstance(shape, Rectangle):
            return shape.width * shape.height

class Circle:
    def __init__(self, radius):
        self.radius = radius

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
# Good design
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius**2

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class AreaCalculator:
    def area(self, shape):
        return shape.area()
    
#%% Liskov Substitution Principle (ISP)
# Objects of a superclass should be replaceable with objects of its subclasses without breaking the application.
# Subclasses must maintain the behavior and expectations established by the base class.

# Wrong example - we are overwriting fly method with behavior which is not consistent with Bird
class Bird:
    def fly(self):
        print('I can fly')

class Penguin(Bird):
    def fly(self):
        print("I can't fly")

# Correct alternative
from abc import ABC, abstractmethod
class Bird(ABC):
    @abstractmethod
    def fly(self):
        pass

class FlyingBird(Bird):
    def fly(self):
        print('I can fly')

class NonFlyingBird(Bird):
    def fly(self):
        print('I cannot fly')

class Penguin(NonFlyingBird):
    pass

#%% Interface Separation Principle (ISP)
"""
Clients should not be forced to depend on interfaces they do not use.
This means breaking larger interfaces into smaller, more specific ones
so that implementing classes only need to worry about the methods they actually use.

Why the Second Design is Better:

Follows Interface Segregation Principle (ISP)
Separates concerns into smaller, more focused interfaces
Reduces unnecessary method implementations
More modular and flexible design
Prevents classes from being forced to implement irrelevant methods

You can also do multiple inheritance if needed -> second code allows to do it easily
"""
# Bad code - Printer/Scanner/Copier have methods which they MUST implement BUT which they don't need!
class IMultiFunctionDevice:
    def print(self):
        pass
    def scan(self):
        pass
    def copy(self):
        pass
    def fax(self):
        pass

class Printer(IMultiFunctionDevice):
    def print(self):
        print("Printing...")

class Scanner(IMultiFunctionDevice):
    def scan(self):
        print("Scanning...")

class Copier(IMultiFunctionDevice):
    def copy(self):
        print("Copying...")

# Good code - each specific method has its own class
class IPrinter: # I means an interface contract. Naming convention
    def print(self):
        pass

class IScanner:
    def scan(self):
        pass

class ICopier:
    def copy(self):
        pass

class IFax:
    def fax(self):
        pass

class Printer(IPrinter):
    def print(self):
        print("Printing...")

class Scanner(IScanner):
    def scan(self):
        print("Scanning...")

class Copier(ICopier):
    def copy(self):
        print("Copying...")

class Fax(IFax):
    def fax(self):
        print("Faxing...")

class PrinterScanner(IPrinter, IScanner):
    def print(self):
        print("Printing...")
    
    def scan(self):
        print("Scanning...")

#%% Dependency Inversion Principle
"""
High-level modules should not depend on low-level modules. Both should depend on abstractions.
Additionally, abstractions should not depend on details; details should depend on abstractions.
This promotes loose coupling and makes systems more flexible and easier to modify.

Dependency Inversion Principle (DIP): Depends on abstractions (IMessageService) instead of concrete classes
More flexible: Can easily add new message services without modifying existing code
Loose coupling: NotificationService is not tightly bound to specific email or SMS implementations
"""
# First Approach (Less Flexible)
class EmailService:
    def send_email(self, message, receiver):
        print(f"Sending email: {message} to {receiver}")

class SmsService:
    def send_sms(self, message, receiver):
        print(f"Sending SMS: {message} to {receiver}")

class NotificationService:
    def __init__(self):
        self.email_service = EmailService()
        self.sms_service = SmsService()
    
    def send_notification(self, message, receiver, method):
        if method == "email":
            self.email_service.send_email(message, receiver)
        elif method == "sms":
            self.sms_service.send_sms(message, receiver)

# Improved Approach (Following Dependency Inversion Principle)
# Both high-level and low-level classes depend on an abstract method!
from abc import ABC, abstractmethod

class IMessageService(ABC):
    @abstractmethod
    def send(self, message, receiver):
        pass

class EmailService(IMessageService):
    def send(self, message, receiver):
        print(f"Sending email: {message} to {receiver}")

class SmsService(IMessageService):
    def send(self, message, receiver):
        print(f"Sending SMS: {message} to {receiver}")

class NotificationService:
    def __init__(self, message_service: IMessageService):
        self.message_service = message_service
    
    def send_notification(self, message, receiver):
        self.message_service.send(message, receiver)