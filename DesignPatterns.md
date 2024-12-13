# Design Patterns in Pizza Restaurant Ordering System

## Singleton Pattern
### Definition:
The Singleton pattern ensures that a class has only one instance, providing a global point of access to it.

### Usage in System:
The `InventoryManager` is a Singleton to ensure there’s only one point of control for managing the inventory.


## Factory Pattern
### Definition:
A method for creating objects in a super class, but allowing subclasses to alter the type of objects created.

### Usage in System:
The `PizzaFactory` class abstracts the creation of pizza objects. This makes the code more maintainable and scalable.

## Decorator Pattern
### Definition:
The Decorator pattern allows for the addition of behavior to an object at runtime.

### Usage in System:
The `ToppingDecorator` class and its subclasses enable the dynamic addition of toppings to pizzas.

## Strategy Pattern
### Definition:
The Strategy pattern defines a family of algorithms and makes them interchangeable.

### Usage in System:
The `PaymentStrategy` interface and its implementations allow customers to choose between different payment methods.

## Overengineering
Overengineering occurs when a system is designed with unnecessary complexity, often leading to wasted resources and effort.In our pizza restaurant system, an example of overengineering would be creating an extensive hierarchy of classes for every possible pizza topping instead of using the Decorator pattern.

```
class CheesePizzaWithOlivesAndMushrooms(Pizza):
    def get_description(self) -> str:
        return "Cheese Pizza, Olives, Mushrooms"
    
    def get_cost(self) -> float:
        return 7.2  # Hardcoded price
```

