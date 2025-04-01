# BEFORE:

def process_text(text, operation):
    if operation == "uppercase":
        return text.upper()
    elif operation == "lowercase":
        return text.lower()
    elif operation == "capitalize":
        return text.capitalize()
    else:
        return text

input_text = "This is an example text."
operation = "uppercase"

output_text = process_text(input_text, operation)
print(output_text)

# AFTER:
from abc import ABC, abstractmethod

# Step 1: Create the TextProcessingStrategy interface
class TextProcessingStrategy(ABC):
    @abstractmethod
    def process(self, text: str) -> str:
        pass

# Step 2: Implement the concrete text processing strategies
# TODO: Implement UppercaseStrategy, LowercaseStrategy, and CapitalizeStrategy classes
class UppercaseStrategy(TextProcessingStrategy):
    # TODO: Implement the process method to convert text to uppercase
    def process(self,text:str):
        return text.upper()

class LowercaseStrategy(TextProcessingStrategy):
    # TODO: Implement the process method to convert text to lowercase
    def process(self,text:str):
        return text.lower()

class CapitalizeStrategy(TextProcessingStrategy):
    # TODO: Implement the process method to capitalize text
    def process(self,text:str):
        return text.capitalize()

# Step 3: Implement the TextProcessor class
class TextProcessor:
    def __init__(self, strategy: TextProcessingStrategy):
        # TODO: Initialize the processor with the given strategy
        self.strategy = strategy

    def set_strategy(self, strategy: TextProcessingStrategy):
        # TODO: Allow changing the strategy at runtime
        self.strategy = strategy

    def process_text(self, text: str) -> str:
        # TODO: Process and return the text using the current strategy
        return self.strategy.process(text)

# Step 4: Test your implementation
if __name__ == "__main__":
    # TODO: Display menu of text processing options
    print("Select processing strategy:")
    print("1. Upper-casing")
    print("2. Lower-casing")
    print("3. Capitalize")
    # TODO: Get user input for text and processing choice
    choice = int(input("Enter the number corresponding to your choice: "))
    text = str(input("Enter text to process: "))
    
    # TODO: Create the appropriate strategy based on user choice
    if choice == 1:
        strategy = UppercaseStrategy()
    elif choice == 2:
        strategy = LowercaseStrategy()
    elif choice == 3:
        strategy = CapitalizeStrategy()
    else:
        print("Invalid choice!")
        exit(1)
    # TODO: Create a text processor with the chosen strategy
    text_processor = TextProcessor(strategy)    
    # TODO: Process and display the transformed text
    print(text_processor.process_text(text))