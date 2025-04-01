# Refactor the code for strategy pattern
# BEFORE:
def calculate_shipping_cost(weight, carrier):
    cost = 0
    if carrier == "FedEx":
        cost = weight * 2.5
    elif carrier == "UPS":
        cost = weight * 3
    elif carrier == "DHL":
        cost = weight * 4
    return cost

print("Select a carrier for shipping:")
print("1. FedEx")
print("2. UPS")
print("3. DHL")

choice = int(input("Enter the number corresponding to your choice: "))
weight = float(input("Enter the weight of the package (in pounds): "))

if choice == 1:
    carrier = "FedEx"
elif choice == 2:
    carrier = "UPS"
elif choice == 3:
    carrier = "DHL"
else:
    print("Invalid choice!")
    exit(1)

shipping_cost = calculate_shipping_cost(weight, carrier)
print(f"The shipping cost for {carrier} is ${shipping_cost:.2f}")

#AFTER:
from abc import ABC, abstractmethod

# Step 1: Create the ShippingStrategy interface
class ShippingStrategy(ABC):
    @abstractmethod
    def calculate_cost(self, weight: float) -> float:
        pass

# Step 2: Implement the concrete shipping strategies
# TODO: Implement FedExStrategy, UPSStrategy, and DHLStrategy classes
class FedExStrategy(ShippingStrategy):
    # TODO: Implement the calculate_cost method for FedEx
    def calculate_cost(self, weight):
        return weight*2.5

class UPSStrategy(ShippingStrategy):
    # TODO: Implement the calculate_cost method for UPS
    def calculate_cost(self, weight):
        return weight*3

class DHLStrategy(ShippingStrategy):
    # TODO: Implement the calculate_cost method for DHL
    def calculate_cost(self, weight):
        return weight*4

class AmazonDelivery(ShippingStrategy):
    # TODO: Implement the calculate_cost method for Amazon
    def calculate_cost(self, weight):
        return weight*3.25


# Step 3: Implement the ShippingCalculator class
class ShippingCalculator:
    def __init__(self, strategy: ShippingStrategy):
        # TODO: Initialize the calculator with the given strategy
        self.strategy = strategy

    def set_strategy(self, strategy: ShippingStrategy):
        # TODO: Allow changing the strategy at runtime
        self.strategy = strategy

    def calculate(self, weight: float) -> float:
        # TODO: Calculate and return the shipping cost using the current strategy
        return self.strategy.calculate_cost(weight)

# Step 4: Test your implementation
if __name__ == "__main__":
    # TODO: Display menu of shipping options (including Amazon Delivery)
    print("Select a carrier for shipping:")
    print("1. FedEx")
    print("2. UPS")
    print("3. DHL")
    print("4. Amazon Delivery")

    # TODO: Get user input for carrier choice and package weight
    choice = int(input("Enter the number corresponding to your choice: "))
    weight = float(input("Enter the weight of the package (in pounds): "))
    
    # TODO: Create the appropriate strategy based on user choice
    if choice == 1:
        strategy = FedExStrategy()
        carrier_name = "FedEx"
    elif choice == 2:
        strategy = UPSStrategy()
        carrier_name = "UPS"
    elif choice == 3:
        strategy = DHLStrategy()
        carrier_name = "DHL"
    elif choice == 4:
        strategy = AmazonDelivery()
        carrier_name = "Amazon Delivery"        
    else:
        print("Invalid choice!")
        exit(1)

    # TODO: Create a shipping calculator with the chosen strategy
    calculator = ShippingCalculator(strategy)

    # TODO: Calculate and display the shipping cost
    cost = calculator.calculate(weight)
    print(f"The shipping cost for {carrier_name} is ${cost:.2f}")