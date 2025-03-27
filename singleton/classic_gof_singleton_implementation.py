class ClassicSingleton:
    # class-level variable to store single class instance
    _instance = None 
 
    # override the __init__ method to control initialization
    def __init__(self): 
        print('<init> called...')
        # raise an error to prevent constructor utilization
        # We want to prevent  s0 = ClassicSingleton()
        raise RuntimeError('Call get_instance() instead')

    @classmethod
    def get_instance(cls):
        print('<get_instance> called...')
        if not cls._instance: 
            # create new instance of the class 
            cls._instance = cls.__new__(cls)  
        # return the single instance of the class, either 
        # newly created one or existing one
        return cls._instance 
    
# s0 = ClassicSingleton()
s1 = ClassicSingleton.get_instance()
s2 = ClassicSingleton.get_instance()

print(s1 is s2) # True
print(s1)
print(s2)

# In Python, the __new__ method is a special method that is
# responsible for creating a new instance of a class. 
# It is called before the __init__ method and is used to 
# control the creation of a new instance. The __new__ 
# method is a static method that takes the class as its 
# first argument (cls) and returns the new instance.

# In the context of the ClassicSingleton class you provided,
# the __new__ method is used to create a new instance of 
# the class without invoking the __init__ method. 
# This is important for implementing the singleton pattern,
# where you want to ensure that only one instance of the
# class is created.