# Singleton Pattern Implementations in Python

#%% Lazy Instantiation - Creates the instance only when it's first requested
# Singleton class should consist of Meta class which relies on type.
#  You can create different Singleton classes out of Meta class
# E.g., one class for loggers, one for cache etc. 
class SingletonMeta(type):
    # Dictionary stores single instance of the class for each subclass of the SingletonMeta metaclass
    _instances = {}

# __call__ method is triggered every time you use class constructor!
# It's a special method in Python that gets automatically
# called when you try to "call" a class as if it were a function.    
    
    def __call__(cls, *args, **kwargs):
        # Check if an instance has already been created
        if cls not in cls._instances:
            # Create the instance by calling the parent's call method
            # super() here refers to type
            # This calls the original type.__call__() method
            # which creates a new instance of the class
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

class Singleton(metaclass=SingletonMeta):
    def some_business_logic(self):
        # Add your specific business logic here
        pass

# Eager Loading Implementation - Creates the instance immediately when the class is defined
# from the very beginning -> when you start the file, it's initiated together with libraries
class SingletonMeta(type):
    # Dictionary stores single instance of the class for each subclass of the SingletonMeta metaclass
    _instances = {}
    
    def __init__(cls, name, bases, dct):
        super().__init__(name, bases, dct)
        # Eager loading of the class instance
        cls._instances[cls] = super().__call__()
    
    def __call__(cls, *args, **kwargs):
        return cls._instances[cls]

class Singleton(metaclass=SingletonMeta):
    def __init__(self):
        # Initialize your attributes here
        pass

# Example usage
s1 = Singleton()  # Will always return the same instance
s2 = Singleton()  # s1 and s2 are the same object

print(s1 is s2)  # Should print True

#%% Demonstrate metaclass inheritance and instance creation
class ParentMeta(type):
    def __call__(cls, *args, **kwargs):
        print("Parent metaclass __call__ method")
        print(f"Creating instance of {cls.__name__}")
        return super().__call__(*args, **kwargs)
# Python automatically passes the class (cls) as the first argument
class ChildMeta(ParentMeta):
    def __call__(cls, *args, **kwargs):
        print("Child metaclass __call__ method")
        # This will call the parent's __call__ method
        return super().__call__(*args, **kwargs)

class MyClass(metaclass=ChildMeta):
    def __init__(self):
        print("MyClass __init__ method")

# Create an instance
print("Creating instance:")
obj = MyClass()
# Creating instance:
# Child metaclass __call__ method
# Parent metaclass __call__ method
# Creating instance of MyClass
# MyClass __init__ method

class Receptionist(type):
    def __call__(cls, *args, **kwargs):
        # Python automatically passes the class itself as the first argument
        print(f"Someone wants to create an object of {cls.__name__}")
        
        # This is the magic part - Python knows which class is being created
        # So it automatically passes the class as the first argument
        
        # Create the actual object
        instance = super().__call__(*args, **kwargs)
        
        return instance

class Employee(metaclass=Receptionist):
    def __init__(self, name):
        self.name = name
        print(f"Creating employee: {name}")

# Demonstration
bob = Employee("Bob")  # This triggers the __call__ method
bob
# Someone wants to create an object of Employee
# Creating employee: Bob
# <__main__.Employee at 0x1efd0d513f0>
#%% Thread-Safety example
from threading import Thread
from threading import Lock
import sys

class Counter:
    """
    A thread-safe counter class that uses a lock to ensure that the increment operation
    is atomic. This means that even if multiple threads try to increment the counter
    simultaneously, the lock mechanism will ensure that only one thread can access the
    increment method at a time, preventing race conditions.

    Attributes:
        count (int): The current count value.
        lock (Lock): A lock object used to synchronize access to the count variable.

    Methods:
        increment(): Increments the count by 1 in a thread-safe manner.
    """

    def __init__(self):
        self.count = 0
        self.lock = Lock()

    def increment(self):
        """
        Increments the count by 1. This method is thread-safe because it acquires a lock
        before modifying the count and releases the lock afterwards. This ensures that
        only one thread can increment the count at a time.
        """
        self.lock.acquire()
        try:
            self.count += 1
        finally:
            self.lock.release()

counter = Counter()
threads = []

# Create multiple threads to increment the counter
for i in range(10):
    thread = Thread(target=counter.increment)
    threads.append(thread)
    thread.start()

# Wait for all threads to finish
for thread in threads:
    thread.join()

print(f"Final count: {counter.count}")
"""
Explanation:
Lock Mechanism: The Lock object from the threading module is used to ensure that only one thread
can execute the increment method at a time. This prevents race conditions where multiple threads
might try to read and write the count variable simultaneously, leading to incorrect results.

Acquiring and Releasing the Lock:

self.lock.acquire(): This line acquires the lock. If another thread has already acquired the lock,
the current thread will block until the lock is released.
self.lock.release(): This line releases the lock, allowing other threads to acquire it.
Try-Finally Block: The try-finally block ensures that the lock is always released,
even if an exception occurs during the increment operation. This is important to prevent deadlocks.

Thread Creation and Joining: The example usage creates multiple threads that increment the counter.
The join method is used to wait for all threads to finish execution before printing the final count.
"""
import threading

class ThreadSafeSingleton:
    """
    A thread-safe singleton class that ensures only one instance of the class is created,
    even when accessed by multiple threads simultaneously. This is achieved using a class-level
    lock to synchronize access to the instance creation code.

    Attributes:
        _instance (ThreadSafeSingleton): The single instance of the class.
        _lock (Lock): A lock object used to ensure thread safety during instance creation.
    """

    # Class-level variable to store the single instance
    _instance = None

    # Class-level lock to ensure thread safety
    _lock = threading.Lock()

    def __new__(cls):
        """
        Override the __new__ method to implement a thread-safe singleton.
        This method ensures that only one instance of the class is created,
        even when accessed by multiple threads simultaneously.

        Returns:
            ThreadSafeSingleton: The single instance of the class.
        """
        # Acquire the lock to ensure thread safety
        with cls._lock:
            # Check if the single instance has been created yet
            if not cls._instance:
                # Create the single instance of the class
                cls._instance = super().__new__(cls)

        # Return the single instance of the class
        return cls._instance

# Example usage:
def create_singleton():
    singleton = ThreadSafeSingleton()
    print(f"Singleton instance: {singleton}")

# Create multiple threads to test the singleton implementation
threads = []
for i in range(5):
    thread = threading.Thread(target=create_singleton)
    threads.append(thread)
    thread.start()

# Wait for all threads to finish
for thread in threads:
    thread.join()

