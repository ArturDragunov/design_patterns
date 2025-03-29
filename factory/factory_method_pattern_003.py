import pygame
import random
from abc import ABC, abstractmethod
from enum import Enum, auto

# Enum allows to for loop (for item in ShapeType) or call as list(ShapeType)
# An Enum (Enumeration) in Python is a set of named constants that makes code more readable and type-safe. It's like a specialized collection where:
# Each member has both a name and value (CIRCLE = 1, RECTANGLE = 2)
# Members can be accessed by name (ShapeType.CIRCLE)
# The entire set can be iterated through or listed (list(ShapeType))
# Comparisons use meaningful names instead of magic strings/numbers
class ShapeType(Enum):
    # auto(): Automatically assigns sequential values to enum members
    CIRCLE = auto() # gets 1
    RECTANGLE = auto() # gets 2
    # alternatively you could write
    # CIRCLE = "Circle"

# Base abstract class for shapes
class Shape(ABC):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @abstractmethod
    def draw(self, surface):
        pass

# Circle class inheriting from Shape
class Circle(Shape):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.radius = random.randint(10, 50)
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    # Draw circle on the given surface
    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (self.x, self.y), self.radius)

# Rectangle class inheriting from Shape
class Rectangle(Shape):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.width = random.randint(10, 100)
        self.height = random.randint(10, 100)
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    # Draw rectangle on the given surface
    def draw(self, surface):
        pygame.draw.rect(surface, self.color, (self.x, self.y, self.width, self.height))

# ShapeFactory class for creating shape instances
class ShapeFactory:
    @staticmethod
    def create_shape(context):
        # we use enumerator instead of hard-coded shapes
        if context.shape_type == ShapeType.CIRCLE:
            return Circle(context.x, context.y)
        elif context.shape_type == ShapeType.RECTANGLE:
            return Rectangle(context.x, context.y)
        else:
            raise ValueError("Invalid shape type")

# ShapeContext class to hold factory parameters
class ShapeContext:
    def __init__(self, shape_type, x, y):
        self.shape_type = shape_type
        self.x = x
        self.y = y

# Main function to set up and run the game loop
def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Random Shapes")
    clock = pygame.time.Clock()

    shape_factory = ShapeFactory()
    shapes = []  # List to store created shapes
    running = True

    # Main game loop
    while running:
        # Process events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            # Create a random shape on mouse click
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                # instead of hard-coded ["Circle", "Rectangle"], we pull types from ShapeType
                # so, we don't need to change this line of code even if we change our shapes
                shape_type = random.choice(list(ShapeType)) 
                context = ShapeContext(shape_type, x, y)
                shape = shape_factory.create_shape(context)
                shapes.append(shape)

        # Clear the screen
        screen.fill((255, 255, 255))

        # Draw all the shapes
        for shape in shapes:
            shape.draw(screen)

        # Update the display
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
