#%% Exercise 1
from abc import ABC, abstractmethod
from enum import Enum

# Step 0: Create an enumeration for vehicle types
class VehicleType(Enum):
    CAR = "Car"
    MOTORCYCLE = "Motorcycle"
    BICYCLE = "Bicycle"

# Step 1: Create an abstract Vehicle class
class Vehicle(ABC):
    @abstractmethod
    def get_name(self) -> str:
        pass

# Step 2: Create concrete vehicle classes
class Car(Vehicle):
    # Implement the get_name() method

    def get_name(self):
        return type(self).__name__
        # you could also use self.__class__.__name__

class Motorcycle(Vehicle):
    # Implement the get_name() method

    def get_name(self):
        return type(self).__name__

class Bicycle(Vehicle):
    # Implement the get_name() method

    def get_name(self):
        return type(self).__name__

# Step 3: Create a VehicleFactory class
class VehicleFactory:
    def create_vehicle(self, vehicle_type: VehicleType) -> Vehicle:
        # Implement the logic to create a vehicle based on the vehicle_type parameter
        if vehicle_type == VehicleType.CAR:
            return Car()
        elif vehicle_type == VehicleType.MOTORCYCLE:
            return Motorcycle()            
        elif vehicle_type == VehicleType.BICYCLE:
            return Bicycle()
        else:
            raise ValueError('Wrong vehicle')


# Step 4: Test the VehicleFactory class
def main():
    vehicle_factory = VehicleFactory()

    # Test the VehicleFactory by creating different types of vehicles
    car = vehicle_factory.create_vehicle(VehicleType.CAR)
    print(car.get_name())

    motorcycle = vehicle_factory.create_vehicle(VehicleType.MOTORCYCLE)
    print(motorcycle.get_name())

    bicycle = vehicle_factory.create_vehicle(VehicleType.BICYCLE)
    print(bicycle.get_name())

if __name__ == "__main__":
    main()


#%% Exercise 2 - interesting way how to assign attributes to a class using dict

from abc import ABC, abstractmethod
from enum import Enum

# Step 0: Create an enumeration for animal types
class AnimalType(Enum):
    DOG = "Dog"
    CAT = "Cat"
    FISH = "Fish"

# Step 1: Create an abstract Animal class
class Animal(ABC):
    @abstractmethod
    def get_info(self) -> str:
        pass

# Step 2: Create concrete animal classes
class Dog(Animal):
    # Implement the __init__ and get_info() methods
    def __init__(self, context):
    # This loops through the dictionary's key-value pairs
    # and uses setattr() to create an attribute with the
    # same name as each key and assign it the corresponding value.        
      for key, value in context.items():
        setattr(self, key, value)
    
    def get_info(self):
        return f'I am a {self.__class__.__name__}'
class Cat(Animal):
    # Implement the __init__ and get_info() methods
    def __init__(self, context):
      for key, value in context.items():
        setattr(self, key, value)
    
    def get_info(self):
        return f'I am a {self.__class__.__name__}'

class Fish(Animal):
    # Implement the __init__ and get_info() methods
    def __init__(self, context):
      for key, value in context.items():
        setattr(self, key, value)

    def get_info(self):
        return f'I am a {self.__class__.__name__}'

# Step 3: Create an AnimalFactory class
class AnimalFactory:
    def create_animal(self, animal_type: AnimalType, context: dict) -> Animal:
        # Implement the logic to create an animal based on the animal_type parameter and context data
        if animal_type == AnimalType.DOG:
            return Dog(context)
        elif animal_type == AnimalType.CAT:
            return Cat(context)
        elif animal_type == AnimalType.FISH:
            return Fish(context)
        else:
            raise ValueError('Unknown type')

# Step 4: Test the AnimalFactory class
def main():
    animal_factory = AnimalFactory()
    context = {'nose':'wet', 'size':'small'}
    # Test the AnimalFactory by creating different types of animals and passing context data
    dog = AnimalFactory(AnimalType.DOG,context)
    print(dog.get_info())
    pig = AnimalFactory(AnimalType.PIG,context)
    print(pig.get_info())
if __name__ == "__main__":
    main()
#%% Extra Exercise 1
"""
Todo List:

Create the abstract SpaceShip class

Define basic properties (position, size, displayName, speed)
Include necessary abstract methods
Add constructor for initialization


Implement concrete spaceship classes

Create MilleniumFalcon class extending SpaceShip
Create UNSCInfinity class extending SpaceShip
Create USSEnterprise class extending SpaceShip
Create Serenity class extending SpaceShip
Implement specific features for each spaceship


Create a SpaceShipType enumeration

Define enum values for each spaceship type
This will be used as a parameter for the factory


Implement the SpaceShipFactory class

Create a factory class with a create_spaceship method
Method should accept a SpaceShipType parameter
Method should return the appropriate SpaceShip subclass instance
Add error handling for unknown spaceship types


Write test code

Create instances of each spaceship type using the factory
Verify that each instance has the correct properties
Test error handling for invalid types
"""
from abc import ABC, abstractmethod
from enum import Enum

# Step 1: Create SpaceShipType enum
class SpaceShipType(Enum):
    MILLENNIUM_FALCON = "MillenniumFalcon"
    UNSC_INFINITY = "UNSCInfinity"
    USS_ENTERPRISE = "USSEnterprise"
    SERENITY = "Serenity"

# Step 2: Create abstract SpaceShip class
class SpaceShip(ABC):
  def __init__(self, position:dict, size:dict, displayName:str, speed:dict):
    """Factory Method Constructor

    Args:
      position (dict): x/y values - location on the screen
      size (dict): height/width
      displayName (str): _description_
      speed (dict): x/y vector
    """
    # Initialize properties
    self.position = position
    self.size = size
    self.displayName = displayName
    self.speed = speed
  
  # Add any abstract methods here
  @abstractmethod
  def get_name(self):
    pass
# Step 3: Implement concrete spaceship classes
class MillenniumFalcon(SpaceShip):
  # Implementation
  def get_name(self):
    return self.__class__.__name__    

class UNSCInfinity(SpaceShip):
  # Implementation
  def get_name(self):
    return self.__class__.__name__

class USSEnterprise(SpaceShip):
  # Implementation
  def get_name(self):
    return self.__class__.__name__

class Serenity(SpaceShip):
  # def __init__(self, position, size, displayName, speed): #-> unnecessary since we are not adding new information
  #    super().__init__(position, size, displayName, speed)  
  # Implementation
  def get_name(self):
    return self.__class__.__name__

# Step 4: Create SpaceShipFactory
class SpaceShipFactory:
  def create_spaceship(self, ship_type: SpaceShipType, **kwargs):
    # Factory implementation
    if ship_type == SpaceShipType.MILLENNIUM_FALCON:
       return MillenniumFalcon(**kwargs)
    elif ship_type == SpaceShipType.UNSC_INFINITY:
      return UNSCInfinity(**kwargs)
    elif ship_type == SpaceShipType.USS_ENTERPRISE:
      return USSEnterprise(**kwargs)
    elif ship_type == SpaceShipType.SERENITY:
       return Serenity(**kwargs)
    else:
       raise ValueError('Wrong spaceship name!')

# Step 5: Test code
factory = SpaceShipFactory()
arguments = {'position':{'x':50, 'y':100},
              'size':{'height':10, 'width':20},
              'displayName':'Terminator2000',
              'speed':{'x':5, 'y':10}}
# Create and test ships
import random
ship = factory.create_spaceship(random.choice(list(SpaceShipType)), **arguments)
print(ship.get_name())