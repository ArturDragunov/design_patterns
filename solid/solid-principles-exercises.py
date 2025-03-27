#%% Q1 - SRP violation - single-responsibility principle. Each class has one responsibility
class PizzaShop:
    def __init__(self, name: str, city: str, zip_code: int):
        pass

    def get_name(self):
        pass

    def change_address(self, city: str, zip_code: int):
        pass
# Answer
class Address:
    def __init__(self, city: str, zip_code: int):
        self.city = city
        self.zip_code = zip_code

    def update_address(self, city: str, zip_code: int):
        self.city = city
        self.zip_code = zip_code

    def __str__(self):
        return f"{self.city}, {self.zip_code}"

class PizzaShop:
    def __init__(self, name: str, address: Address):
        self.name = name
        self.address = address

    def get_name(self):
        return self.name

    def update_address(self, city: str, zip_code: int):
        self.address.update_address(city, zip_code)

    def __str__(self):
        return f"PizzaShop: {self.name}, Address: {self.address}"

# Usage
address = Address('New York', 25070)
pizza_shop = PizzaShop('Pizza Hut', address)

print(pizza_shop)  # Output: PizzaShop: Pizza Hut, Address: New York, 25070

# Update address
pizza_shop.update_address('Los Angeles', 90001)
print(pizza_shop)  # Output: PizzaShop: Pizza Hut, Address: Los Angeles, 90001

#%% Q2 - OCP violation - Open-Close principle - You can't modify class, only extend!
class Address:
    def __init__(self, city: str, zip_code: int):
        self.city = city
        self.zip_code = zip_code

class PizzaShop:
    def __init__(self, name: str, address: Address):
        self.name = name
        self.address = address

    def get_name(self):
        return self.name

    def get_address(self):
        return self.address

class InvoiceService:
    def generate_invoice(self, shop):
        invoice = ""
        if isinstance(shop, PizzaShop):
            invoice = "format of invoice for PizzaShop"
        # Add more conditions for other shop types
        return invoice
    
# Answer
from abc import ABC, abstractmethod
class Entity(ABC):
    @abstractmethod
    def get_name(self):
        pass
    @abstractmethod
    def get_address(self):
        pass
    @abstractmethod
    def generate_invoice(self):
        pass
class Address:
    def __init__(self, city: str, zip_code: int):
        self.city = city
        self.zip_code = zip_code

class PizzaShop(Entity):
    def __init__(self, name: str, address: Address):
        self.name = name
        self.address = address

    def get_name(self):
        return self.name

    def get_address(self):
        return self.address
    
    def generate_invoice(self):
        return f"format of invoice for {self.get_name()}"
class InvoiceService:
    def generate_invoice(self, shop:Entity):
        # polymorphism - you can generate new shop types with different
        # invoice formats and it will still work
        return shop.generate_invoice()
    
#%% LSP - Subclasses must maintain the behavior
# and expectations established by the base class.
class PizzaShop:
    def home_delivery(self):
        pass

class A(PizzaShop):
    def home_delivery(self):
        return "delivery is free for all our customers"

class B(PizzaShop):
    def takeaway(self):
        raise Exception('We do not have home delivery service')
    
# Answer:
class PizzaShop:
    def home_delivery(self):
        pass
class DeliveryAvailable(PizzaShop):
    def home_delivery(self):
        return "delivery is free for all our customers"
class DeliveryNotAvailable(PizzaShop):
    def home_delivery(self):
        return "We do not have home delivery service"    
class A(DeliveryAvailable):
    pass
class B(DeliveryNotAvailable):
    pass
# Usage
shop_a = A()
shop_b = B()

print(shop_a.home_delivery())  # Output: delivery is free for all our customers
print(shop_b.home_delivery())  # Output: We do not have home delivery service

#%% ISP - Clients should not be forced to depend on interfaces they do not use. 
from abc import ABC, abstractmethod

class IPizzaShop(ABC):
    @abstractmethod
    def get_oven_baked_pizza(self):
        pass

    @abstractmethod
    def get_classical_baked_pizza(self):
        pass

    @abstractmethod
    def get_electric_oven_baked_pizza(self):
        pass

    @abstractmethod
    def get_pizza_pocket_square_baked_pizza(self):
        pass

    @abstractmethod
    def get_drinks(self):
        pass

class TraditionalPizzeria(IPizzaShop):
    def get_oven_baked_pizza(self):
        pass

    def get_classical_baked_pizza(self):
        pass

    def get_drinks(self):
        pass

    def get_electric_oven_baked_pizza(self):
        raise Exception('We don\'t do that')

    def get_pizza_pocket_square_baked_pizza(self):
        raise Exception('We don\'t do that')

class NewWavePizzeria(IPizzaShop):
    def get_electric_oven_baked_pizza(self):
        pass

    def get_pizza_pocket_square_baked_pizza(self):
        pass

    def get_drinks(self):
        pass

    def get_oven_baked_pizza(self):
        raise Exception('We don\'t do that')

    def get_classical_baked_pizza(self):
        raise Exception('We don\'t do that')
    
# Answer:
class IOvenBakedPizza(ABC):
    @abstractmethod
    def get_oven_baked_pizza(self):
        pass
class IClassicalBakedPizza(ABC):
    @abstractmethod
    def get_classical_baked_pizza(self):
        pass
class IElectricPizza(ABC):
    @abstractmethod
    def get_electric_oven_baked_pizza(self):
        pass
class IPizzaPocketSquare(ABC):
    @abstractmethod
    def get_pizza_pocket_square_baked_pizza(self):
        pass    
class IDrinks(ABC):
    @abstractmethod
    def get_drinks(self):
        pass    
class TraditionalPizzeria(IOvenBakedPizza, IClassicalBakedPizza, IDrinks):
    def get_oven_baked_pizza(self):
        pass

    def get_classical_baked_pizza(self):
        pass

    def get_drinks(self):
        pass

class NewWavePizzeria(IElectricPizza, IPizzaPocketSquare, IDrinks):
    def get_electric_oven_baked_pizza(self):
        pass

    def get_pizza_pocket_square_baked_pizza(self):
        pass

    def get_drinks(self):
        pass
    
#%% DIP -> High-level modules should not depend on low-level modules. 
# Both should depend on abstractions. 
class PizzaShop:
    def get_payment(self):
        pass

    def deliver_pizza(self):
        pass

class Customer:
    def make_payment(self):
        pass

    def receive_pizza(self):
        pass

class Delivery:
    def __init__(self, customer: Customer, pizza_shop: PizzaShop):
        self.customer = customer
        self.pizza_shop = pizza_shop

    def deliver(self):
        self.customer.make_payment()
        self.pizza_shop.get_payment()
        self.pizza_shop.deliver_pizza()
        self.customer.receive_pizza()

# Answer:
from abc import ABC, abstractmethod

class IPayment(ABC):
    @abstractmethod
    def make_payment(self):
        pass

class IOrderDelivery(ABC):
    @abstractmethod
    def deliver_order(self):
        pass
    
class IOrderReceive(ABC):
    @abstractmethod
    def receive_order(self):
        pass

class IReceivePayment(ABC):
    @abstractmethod
    def get_payment(self):
        pass
class PizzaShop(IOrderDelivery, IReceivePayment):
    def deliver_order(self):
        print("PizzaShop: Pizza delivered")

    def get_payment(self):
        print("PizzaShop: Payment received")

class Customer(IPayment, IOrderReceive):
    def make_payment(self):
        print("Customer: Payment made")

    def receive_order(self):
        print("Customer: Pizza received")
from typing import Union
class Delivery:
    def __init__(self, customer: Union[IPayment, IOrderReceive], entity: Union[IOrderDelivery, IReceivePayment]):
        self.customer = customer
        self.entity = entity

    def deliver(self):
        self.customer.make_payment()
        self.entity.get_payment()
        self.entity.deliver_order()
        self.customer.receive_order()

# Usage
customer = Customer()
pizza_shop = PizzaShop()
delivery = Delivery(customer, pizza_shop)
delivery.deliver()
