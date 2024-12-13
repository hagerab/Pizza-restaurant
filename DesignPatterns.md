# Design Patterns in Pizza Restaurant Ordering System

## Singleton Pattern
### Description
The Singleton pattern ensures that a class has only one instance and provides a global point of access to that instance. In our pizza restaurant system, this pattern is applied to the `InventoryManager` class.

### Application
Before applying the Singleton pattern, the `InventoryManager` could have been instantiated multiple times, leading to inconsistent inventory states. By implementing the Singleton pattern, we ensure that there is only one instance of `InventoryManager` throughout the application.

### Improvement in Maintainability and Extensibility
By limiting the inventory manager to a single instance, we prevent potential bugs related to inventory management. This also simplifies the codebase, making it easier to maintain and extend, as all parts of the system reference the same `InventoryManager` instance.

## Factory Pattern
### Description
The Factory pattern provides a way to create objects without specifying the exact class of the object that will be created. In our case, the PizzaFactory class is responsible for creating pizza objects based on the user's choice.

### Application
Before implementing the Factory pattern, the logic for creating pizza instances was scattered across the code. The PizzaFactory centralizes this logic, making it easier to manage and extend.

### Improvement in Maintainability and Extensibility
The Factory pattern simplifies the addition of new pizza types in the future. If a new pizza type is introduced, we just need to modify the PizzaFactory without altering other parts of the code.

## Decorator Pattern
### Description
The Decorator pattern allows behavior to be added to individual objects, either statically or dynamically, without affecting the behavior of other objects from the same class. In our system, we use it to add toppings to pizzas.

### Application
Without the Decorator pattern, adding toppings would require creating new classes for each combination of pizza and topping, leading to a combinatorial explosion of classes. The Decorator pattern allows us to wrap existing pizza objects with topping decorators dynamically.

### Improvement in Maintainability and Extensibility
Adding new toppings is straightforward. We can create a new decorator class for each topping without modifying the existing pizza classes. This keeps our code clean and manageable.

## Overengineering
Overengineering occurs when a system is designed with unnecessary complexity, often leading to wasted resources and effort. In our pizza restaurant system, an example of overengineering would be creating an extensive hierarchy of classes for every possible pizza topping instead of using the Decorator pattern.

```
class CheesePizzaWithOlivesAndMushrooms(Pizza):
    def get_description(self) -> str:
        return "Cheese Pizza, Olives, Mushrooms"
    
    def get_cost(self) -> float:
        return 7.2  # Hardcoded price
```

