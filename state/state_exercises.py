#%% Exercise 1
from abc import ABC, abstractmethod
 
# Step 1: Define the abstract base class TicketState
# This class provides a blueprint for all the possible states a ticket can have.
class TicketState(ABC):
 
    # Method to assign a ticket; to be implemented by each concrete state class
    @abstractmethod
    def assign(self, ticket):
        pass
 
    # Method to resolve a ticket; to be implemented by each concrete state class
    @abstractmethod
    def resolve(self, ticket):
        pass
 
    # Method to close a ticket; to be implemented by each concrete state class
    @abstractmethod
    def close(self, ticket):
        pass
 
# Step 2: Implement the concrete state classes
# Each class represents a specific state and its behavior.
 
class NewState(TicketState):
 
    # Transition from New to Assigned state
    def assign(self, ticket):
        ticket.state = AssignedState()
        print("Ticket has been assigned.")
 
    # Print an error since a New ticket cannot be directly resolved
    def resolve(self, ticket):
        print("Cannot resolve a new ticket. Assign it first.")
 
    # Transition from New to Closed state
    def close(self, ticket):
        ticket.state = ClosedState()
        print("Ticket has been closed.")
 
class AssignedState(TicketState):
 
    # Print a message since the ticket is already in an Assigned state
    def assign(self, ticket):
        print("Ticket is already assigned.")
 
    # Transition from Assigned to Resolved state
    def resolve(self, ticket):
        ticket.state = ResolvedState()
        print("Ticket has been resolved.")
 
    # Transition from Assigned to Closed state
    def close(self, ticket):
        ticket.state = ClosedState()
        print("Ticket has been closed.")
 
class ResolvedState(TicketState):
 
    # Print an error since a Resolved ticket cannot be reassigned
    def assign(self, ticket):
        print("Cannot assign a resolved ticket.")
 
    # Print a message since the ticket is already in a Resolved state
    def resolve(self, ticket):
        print("Ticket is already resolved.")
 
    # Transition from Resolved to Closed state
    def close(self, ticket):
        ticket.state = ClosedState()
        print("Ticket has been closed.")
 
class ClosedState(TicketState):
 
    # Print an error since a Closed ticket cannot be reassigned
    def assign(self, ticket):
        print("Cannot assign a closed ticket.")
 
    # Print an error since a Closed ticket cannot be resolved
    def resolve(self, ticket):
        print("Cannot resolve a closed ticket.")
 
    # Print a message since the ticket is already in a Closed state
    def close(self, ticket):
        print("Ticket is already closed.")
 
# Step 3: Implement the Ticket class
# This class represents a ticket which can transition through various states.
class Ticket:
 
    def __init__(self):
        # Initializing the ticket's state to NewState
        self.state = NewState()
 
    # Delegate the assign action to the current state of the ticket
    def assign(self):
        self.state.assign(self)
 
    # Delegate the resolve action to the current state of the ticket
    def resolve(self):
        self.state.resolve(self)
 
    # Delegate the close action to the current state of the ticket
    def close(self):
        self.state.close(self)
 
# Step 4: Test the behavior of the ticket and its state transitions
def main():
    ticket = Ticket()
 
    # Test the valid state transitions
    ticket.assign()
    ticket.resolve()
    ticket.close()
 
    # Test some potentially invalid transitions
    ticket.assign()
    ticket.resolve()
 
main()