#%% Exercise 1
from abc import ABC, abstractmethod

class Computer:
    def __init__(self, processor, memory, storage, graphics_card, operating_system, extras):
        # Initialize the attributes
        self.processor = processor
        self.memory = memory
        self.storage = storage
        self.graphics_card = graphics_card
        self.operating_system = operating_system
        self.extras = extras

class ComputerBuilder(ABC):
    @abstractmethod
    def add_processor(self):
        pass

    @abstractmethod
    def add_memory(self):
        pass

    @abstractmethod
    def add_storage(self):
        pass

    @abstractmethod
    def add_graphics_card(self):
        pass

    @abstractmethod
    def add_operating_system(self):
        pass

    @abstractmethod
    def add_extras(self):
        pass
    @abstractmethod
    def get_result(self):
        pass
    
class CustomComputerBuilder(ComputerBuilder):
    def __init__(self):
        # Initialize a Computer object
        self.reset()

    """
    return self allows method chaining in a builder pattern.
    When a method returns the object itself (self),
    you can call another method immediately on the result.

    Without method chaining:
    builder = CustomComputerBuilder()
    builder.add_processor(specs)
    builder.add_memory(specs)
    builder.add_storage(specs)
    computer = builder.get_result()

    With method chaining:
    computer = (CustomComputerBuilder()
              .add_processor(specs)
              .add_memory(specs)
              .add_storage(specs)
              .get_result())
    """    
    
      # Override abstract methods and set Computer attributes
    def reset(self):
        self.computer = Computer(None, None, None, None, None, [])
        return self 

    def add_processor(self, specs):
        self.computer.processor = specs['processor']
        return self

    def add_memory(self, specs):
        self.computer.memory = specs['memory']
        return self

    def add_storage(self, specs):
        self.computer.storage = specs['storage']
        return self

    def add_graphics_card(self, specs):
        self.computer.graphics_card = specs['graphics_card']
        return self

    def add_operating_system(self, specs):
        self.computer.operating_system = specs['operating_system']
        return self

    def add_extras(self, specs):
        self.computer.extras = specs['extras']
        return self

    def get_result(self):
        return self.computer

class ComputerDirector:
    def __init__(self, builder):
        # Initialize the builder instance
        self.builder = builder
    def build_computer(self, specs):
        # Call the add_* methods of the builder with the specs
        return (self.builder
                .add_processor(specs)
                .add_memory(specs)
                .add_storage(specs)
                .add_graphics_card(specs)
                .add_operating_system(specs)
                .add_extras(specs)
                .get_result())

# Helper function to test the computer building process
def test_computer_building(specs, expected_output):
    builder = CustomComputerBuilder()
    director = ComputerDirector(builder)
    computer = director.build_computer(specs)
    assert computer.__dict__ == expected_output, f"Expected {expected_output}, but got {computer.__dict__}"

# Test cases
test_specs = {
    'processor': 'Intel Core i5',
    'memory': '8GB',
    'storage': '512GB SSD',
    'graphics_card': 'Integrated',
    'operating_system': 'Windows 11',
    'extras': ['Wi-Fi']
}

expected_output = {
    'processor': 'Intel Core i5',
    'memory': '8GB',
    'storage': '512GB SSD',
    'graphics_card': 'Integrated',
    'operating_system': 'Windows 11',
    'extras': ['Wi-Fi']
}

test_computer_building(test_specs, expected_output)

print("All tests passed!")


#%% Exercise 2
# 1. Create the User class with required and optional fields
class User:
  def __init__(self, firstName, lastName, emailAddress, age=None, 
               phoneNumber=None, address=None):
    # TODO: Initialize all attributes (required and optional)
    self.__firstName = firstName
    self.__lastName = lastName
    self.__emailAddress = emailAddress
    self.__age = age
    self.__phoneNumber = phoneNumber
    self.__address = address
    
  # TODO: Add getter methods for all attributes (no setters)
  def getFirstName(self):
      return self.__firstName
  def getLastName(self):
      return self.__lastName
  def getEmailAddress(self):
      return self.__emailAddress
  def getAge(self):
      return self.__age
  def getPhoneNumber(self):
      return self.__phoneNumber
  def getAddress(self):
      return self.__address          
# 2. Create the UserBuilder class
class UserBuilder:
  def __init__(self):
    # TODO: Initialize builder attributes
    self.__firstName = None
    self.__lastName = None
    self.__emailAddress = None
    self.__age = None
    self.__phoneNumber = None
    self.__address = None
    
  # TODO: Add methods for setting required fields (firstName, lastName, emailAddress)
  def firstName(self, firstName):
    self.__firstName = firstName
    return self
    
  def lastName(self, lastName):
    self.__lastName = lastName
    return self
    
  def emailAddress(self, emailAddress):
    self.__emailAddress = emailAddress
    return self
    
  def age(self, age):
    self.__age = age
    return self
    
  def phoneNumber(self, phoneNumber):
    self.__phoneNumber = phoneNumber
    return self
    
  def address(self, address):
    self.__address = address
    return self
    
  def build(self):
    # Validate required fields
    if not self.__firstName:
      raise ValueError("firstName is required")
    if not self.__lastName:
      raise ValueError("lastName is required")
    if not self.__emailAddress:
      raise ValueError("emailAddress is required")
      
    return User(
      self.__firstName,
      self.__lastName, 
      self.__emailAddress,
      self.__age,
      self.__phoneNumber,
      self.__address
    )
  
