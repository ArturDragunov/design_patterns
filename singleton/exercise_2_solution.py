import threading

class NumberGenerator:
    """
    This is a thread-safe Singleton class that generates a sequence of numbers.
    The sequence starts from 0 and increments by 1 with each call to getNextNumber().
    """
    _instance = None
    _lock = threading.Lock()
    _current_number = 0

    def __new__(cls):
        """
        This method controls the creation of a new instance.
        It ensures that only one instance of the class is created, even in a multithreaded environment.
        """
        with cls._lock:
            if cls._instance is None:
                cls._instance = super(NumberGenerator, cls).__new__(cls)
        return cls._instance

    def getNextNumber(self):
        """
        This method returns the next number in the sequence.
        It is thread-safe, ensuring that the number sequence remains consistent across threads.
        """
        with self._lock:
            number = self._current_number
            self._current_number += 1
        return number

# Test code to show that the thread-safe Singleton works as expected
def test_singleton_thread_safe():
    generator = NumberGenerator()
    print(f"Generated Number: {generator.getNextNumber()}")

if __name__ == "__main__":
    threads = []
    for i in range(10):
        thread = threading.Thread(target=test_singleton_thread_safe)
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()
