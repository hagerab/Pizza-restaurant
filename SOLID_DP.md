# SOLID Principles and Design Patterns in the Pizza Restaurant System

## SOLID Principles Overview

SOLID is a set of five principles that help to design software that is easy to maintain and extend. They are:

1. **S** - Single Responsibility Principle (SRP)
2. **O** - Open/Closed Principle (OCP)
3. **L** - Liskov Substitution Principle (LSP)
4. **I** - Interface Segregation Principle (ISP)
5. **D** - Dependency Inversion Principle (DIP)

## Design Patterns Applied

### 1. Singleton Pattern (InventoryManager)

#### Pattern Overview:
The Singleton pattern ensures that a class has only one instance and provides a global point of access to that instance.

#### Application to the System:
The `InventoryManager` class is designed as a Singleton because there should only be one instance of the inventory to manage the stock of ingredients across all pizza orders.

#### SOLID Principle Addressed:
- **Single Responsibility Principle (SRP)**: The `InventoryManager` has the single responsibility of managing the inventory.
- **Dependency Inversion Principle (DIP)**: The `InventoryManager` class provides services to higher-level modules (like the `PizzaFactory`) without depending on them.

### 2. Factory Pattern (PizzaFactory)
#### Pattern Overview:
The Factory pattern provides an interface for creating objects in a super class but allows subclasses to alter the type of objects that will be created.

#### Application to the System:
The PizzaFactory class abstracts the creation of different pizza types. Instead of directly creating pizzas in the main() function, you delegate this responsibility to the factory class.

#### SOLID Principle Addressed:
- **Open/Closed Principle (OCP)**: New pizza types can be added to the system without modifying the existing code. The PizzaFactory can easily be extended to add more pizza types.
- **Liskov Substitution Principle (LSP)**: The PizzaFactory ensures that any subclass of Pizza can be created, ensuring that all pizza objects can be substituted interchangeably.

### 3. Decorator Pattern (ToppingDecorator, Cheese, Olives, Mushrooms)
#### Pattern Overview:
The Decorator pattern allows you to dynamically add behavior to an object at runtime. It provides a flexible alternative to subclassing for extending functionality.

#### Application to the System:
The ToppingDecorator class and its subclasses (Cheese, Olives, Mushrooms) allow toppings to be added to pizzas dynamically. The decorator pattern enables additional functionality (like adding toppings) without modifying the core Pizza classes.

#### SOLID Principle Addressed:
- **Open/Closed Principle (OCP)**: New toppings can be added without modifying the existing pizza classes. You can easily add new decorators for additional toppings.
- **Interface Segregation Principle (ISP)**: The Pizza class provides a clear and minimal interface with the get_description() and get_cost() methods, ensuring that classes using the pizza don’t need to implement unnecessary methods.

### 4. Strategy Pattern (Payment Methods)
#### Pattern Overview:
The Strategy pattern allows selecting an algorithm at runtime. It defines a family of algorithms, encapsulates each one, and makes them interchangeable.

#### Application to the System:
The PaymentStrategy interface and its implementations (PayPalPayment, CreditCardPayment, Cash) allow the user to choose their preferred payment method at runtime. This makes it easy to add new payment strategies without changing the existing code.

#### SOLID Principle Addressed:
- **Open/Closed Principle (OCP)**: New payment methods can be introduced by simply creating new strategy classes without altering the existing payment methods or the client code.
- **Dependency Inversion Principle (DIP)**: The high-level modules (like the pizza ordering process) depend on the PaymentStrategy interface, not on specific payment methods.
