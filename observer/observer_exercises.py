#%% Exercise 1
from abc import ABC, abstractmethod


class Observer(ABC):
    @abstractmethod
    def update(self, product_name: str, new_stock: int) -> None:
        pass


class Subject(ABC):
    @abstractmethod
    def attach(self, observer: Observer) -> None:
        pass

    @abstractmethod
    def detach(self, observer: Observer) -> None:
        pass

    @abstractmethod
    def notify(self) -> None:
        pass


class StoreManager(Observer):
    def __init__(self, name: str):
        self._name = name

    def update(self, product_name: str, new_stock: int) -> None:
        # TODO: Implement the update method to display a message indicating the stock level update
        print(f'the stock level {new_stock} for the product {product_name} has gone below the threshold and {self._name} has been notified.')

# Publisher-Subject class
class Inventory(Subject):
    def __init__(self):
        self._observers = []
        self._products = {}

    def attach(self, observer: Observer) -> None:
        # TODO: Implement the attach method to add an observer
        self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        # TODO: Implement the detach method to remove an observer
        self._observers.remove(observer)

    def notify(self, product_name, new_stock) -> None:
        # TODO: Implement the notify method to notify all observers
        for observer in self._observers:
            observer.update(product_name, new_stock)

    def update_stock(self, product_name: str, new_stock: int) -> None:
        # TODO: Implement the update_stock method to update the stock level and call notify if necessary
        if product_name in self._products:
            if self._products[product_name] > new_stock:
                self.notify(product_name, new_stock)
        self._products[product_name] = new_stock


if __name__ == "__main__":
    inventory = Inventory()
    
    # Adding products to inventory
    inventory._products = {
        "Apples": 10,
        "Oranges": 25,
        "Bananas": 50,
    }
    
    manager1 = StoreManager("Alice")
    manager2 = StoreManager("Bob")
    
    # Attaching store managers
    inventory.attach(manager1)
    inventory.attach(manager2)
    
    # Updating stock levels and checking notifications
    print("Stock level update 1:")
    inventory.update_stock("Apples", 5)  # Should notify both managers
    print("\nStock level update 2:")
    inventory.update_stock("Bananas", 60)  # Should not notify as stock level increased
    
    # Detaching manager1
    inventory.detach(manager1)
    
    # Updating stock levels again
    print("\nStock level update 3:")
    inventory.update_stock("Oranges", 20)  # Should notify only manager2

#%% Exercise 2
# Subject class - Publisher
from abc import ABC, abstractmethod

class Observer(ABC):
    @abstractmethod
    def update(self, temperature, humidity, pressure):
        pass
    
class WeatherData:
    def __init__(self):
        self.temperature = None
        self.humidity = None
        self.pressure = None
        self._observers = []
    def set_measurements(self, temperature, humidity, pressure):
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure
        self.notify_observers()
    def notify_observers(self):
        for observer in self._observers:
            observer.update(self.temperature, self.humidity, self.pressure)
    def attach(self, observer:Observer):
        self._observers.append(observer)

class CurrentConditionsDisplay(Observer):
    def update(self, temperature, humidity, pressure):
        print(f'Current temperature is {temperature}, humidity is {humidity}, pressure is {pressure}')
class StatisticsDisplay(Observer):
  def update(self, temperature, humidity, pressure):
        print(f'Statistics added: temperature is {temperature}, humidity is {humidity}, pressure is {pressure}')
class ForecastDisplay(Observer):
 def update(self, temperature, humidity, pressure):
        print(f'Forecast for tomorrow: temperature is {temperature}, humidity is {humidity}, pressure is {pressure}')       

# test
weather_data = WeatherData()
current_condition = CurrentConditionsDisplay()
statistics_display = StatisticsDisplay()
forecast_display = ForecastDisplay()
weather_data.attach(current_condition) 
weather_data.attach(statistics_display) 
weather_data.attach(forecast_display)
weather_data.set_measurements(20, 80, 30)
