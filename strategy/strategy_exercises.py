#%% Exercise 1
from abc import ABC, abstractmethod

# Step 1: Create the DiscountStrategy interface
class DiscountStrategy(ABC):

    @abstractmethod
    def apply_discount(self, total: float) -> float:
        pass

# Step 2: Implement the discount strategies
# TODO: Implement NoDiscount, PercentageDiscount, and FixedAmountDiscount classes
class NoDiscount(DiscountStrategy):
    def apply_discount(self, total:float):
        return total
class PercentageDiscount(DiscountStrategy):
    def __init__(self, percentage):
        self.percentage = percentage
    def apply_discount(self, total):
        return total - total*self.percentage/100
        
class FixedAmountDiscount(DiscountStrategy):
    def __init__(self, fixed_amount):
        self.fixed_amount = fixed_amount
    def apply_discount(self, total):
        return total - self.fixed_amount    
# Step 3: Implement the ShoppingCart class
class ShoppingCart:

    def __init__(self, discount_strategy: DiscountStrategy):
        # TODO: Initialize the shopping cart with the given discount_strategy and an empty items dictionary
        self.discount_strategy = discount_strategy
        self.items = {}
    def add_item(self, item: str, price: float):
        # TODO: Add the item with its price to the items dictionary
        self.items[item] = price
    def remove_item(self, item: str):
        # TODO: Remove the item from the items dictionary if it exists
        self.items.pop(item)
    def get_total(self) -> float:
        # TODO: Calculate and return the total price of the items in the cart
        return sum(self.items.values())
    def get_total_after_discount(self) -> float:
        # TODO: Calculate and return the total price of the items in the cart after applying the discount
        return self.discount_strategy.apply_discount(self.get_total())
# Step 4: Test your implementation
if __name__ == "__main__":
    # TODO: Create a shopping cart with a discount strategy
    cart = ShoppingCart(PercentageDiscount(10))

    # TODO: Add a few items
    cart.add_item("Item 1", 10.0)
    cart.add_item("Item 2", 20.0)
    cart.add_item("Item 3", 30.0)

    # TODO: Calculate and print the total price before discount
    print("Total before discount:", cart.get_total())

    # TODO: Calculate and print the total price after applying the discount
    print("Total after discount:", cart.get_total_after_discount())
    
    
    # TODO: Create a shopping cart with a discount strategy
    cart = ShoppingCart(FixedAmountDiscount(15))

    # TODO: Add a few items
    cart.add_item("Item 1", 10.0)
    cart.add_item("Item 2", 20.0)
    cart.add_item("Item 3", 30.0)

    # TODO: Calculate and print the total price before discount
    print("Total before discount:", cart.get_total())

    # TODO: Calculate and print the total price after applying the discount
    print("Total after discount:", cart.get_total_after_discount())
    
    
    # TODO: Create a shopping cart with a discount strategy
    cart = ShoppingCart(NoDiscount())

    # TODO: Add a few items
    cart.add_item("Item 1", 10.0)
    cart.add_item("Item 2", 20.0)
    cart.add_item("Item 3", 30.0)

    # TODO: Calculate and print the total price before discount
    print("Total before discount:", cart.get_total())

    # TODO: Calculate and print the total price after applying the discount
    print("Total after discount:", cart.get_total_after_discount())

#%% Exercise 2
from abc import ABC, abstractmethod
from typing import List, Dict, Any
import csv
import json
import xml.etree.ElementTree as ET
# Step 1: Create the FileParser interface
class FileParser(ABC):

    @abstractmethod
    def parse_file(self, file_path: str) -> List[Dict[str, Any]]:
        pass

# Step 2: Implement the file parsers
# TODO: Implement CSVParser, JSONParser, and XMLParser classes
class CSVParser(FileParser):
  def parse_file(self, file_path: str) -> List[Dict[str, Any]]:
    result = []
    with open(file_path, 'r', newline='') as csvfile:
      reader = csv.DictReader(csvfile)
      for row in reader:
        result.append(dict(row))
    return result

class JSONParser(FileParser):
  def parse_file(self, file_path: str) -> List[Dict[str, Any]]:
    with open(file_path, 'r') as jsonfile:
      return json.load(jsonfile)

class XMLParser(FileParser):
  def parse_file(self, file_path: str) -> List[Dict[str, Any]]:
    result = []
    tree = ET.parse(file_path)
    root = tree.getroot()
    
    for child in root:
      item = {}
      for key, value in child.attrib.items():
        item[key] = value
      result.append(item)
    
    return result   
# Step 3: Implement the FileReader class
class FileReader:

    def __init__(self, file_parser: FileParser):
        # TODO: Initialize the file reader with the given file_parser
        self.file_parser = file_parser

    def read_file(self, file_path: str) -> List[Dict[str, Any]]:
        # TODO: Read the file at the given file_path and return a list of dictionaries using the specified file parser
        return self.file_parser.parse_file(file_path)
# Step 4: Test your implementation
if __name__ == "__main__":
    # TODO: Create a file reader with a CSVParser
    reader = FileReader(CSVParser())

    # TODO: Read a sample CSV file and print the list of dictionaries
    data = reader.read_file("sample.csv")
    print(data)
