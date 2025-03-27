from abc import ABCMeta, abstractmethod
import threading
import logging

# This is a metaclass for creating singleton classes. Singleton classes allow only one instance.
class SingletonMeta(type):
    _instances = {}  # Dictionary to hold the instance reference for each class.
    _lock = threading.Lock()  # A lock to ensure thread-safe singleton instantiation.

    def __call__(cls, *args, **kwargs):
        # Acquire the lock to make sure that only one thread can enter this block at a time.
        with cls._lock:
            # Check if the instance already exists for the class.
            if cls not in cls._instances:
                # If not, create the instance and store it in the _instances dictionary.
                cls._instances[cls] = super().__call__(*args, **kwargs)
        # Return the instance.
        return cls._instances[cls]

# This metaclass combines the features of SingletonMeta and ABCMeta.
# ABCMeta is an abstract meta class
class SingletonABCMeta(ABCMeta, SingletonMeta):
    def __new__(cls, name, bases, namespace):
        # Create a new class using the combined metaclasses.
        return super().__new__(cls, name, bases, namespace)

# BaseLogger is an abstract class with the SingletonABCMeta metaclass -> because SingletonABCMeta relies on ABCMeta
class BaseLogger(metaclass=SingletonABCMeta):
    # These methods are abstract, meaning subclasses must implement these methods.
    @abstractmethod
    def debug(cls, message: str):
        pass

    @abstractmethod
    def info(cls, message: str):
        pass

    @abstractmethod
    def warning(cls, message: str):
        pass

    @abstractmethod
    def error(cls, message: str):
        pass

    @abstractmethod
    def critical(cls, message: str):
        pass

# MyLogger is a concrete implementation of BaseLogger.
class MyLogger(BaseLogger):
    def __init__(self):
        print('<Logger init> initializing logger...')
        # Create a logger object with the specified name.
        self._logger = logging.getLogger('my_logger')
        # Set the logging level to DEBUG.
        self._logger.setLevel(logging.DEBUG)

        # Create a file handler to log messages to a file.
        file_handler = logging.FileHandler('my_log_file.log')
        # Set the file handler logging level to DEBUG.
        file_handler.setLevel(logging.DEBUG)

        # Create a console handler to log messages to the console.
        console_handler = logging.StreamHandler()
        # Set the console handler logging level to INFO.
        console_handler.setLevel(logging.INFO)

        # Define the log message format.
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        # Set the formatter for both the file and console handlers.
        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)

        # Add the file and console handlers to the logger.
        self._logger.addHandler(file_handler)
        self._logger.addHandler(console_handler)

    # Implementations of the abstract methods in BaseLogger.
    def debug(self, message: str):
        self._logger.debug(message)

    def info(self, message: str):
        self._logger.info(message)

    def warning(self, message: str):
        self._logger.warning(message)

    def error(self, message: str):
        self._logger.error(message)

    def critical(self, message: str):
        self._logger.critical(message)


# Create an instance of MyLogger.
logger = MyLogger()
# Log different types of messages.
logger.debug('This is a debug message')
logger.info('This is an info message')
logger.warning('This is a warning message')
logger.error('This is an error message')
logger.critical('This is a critical message')
