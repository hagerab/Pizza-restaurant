### SOLID_DP.md

markdown
# SOLID Principles and Design Patterns

## Singleton Pattern and SOLID
- **Single Responsibility Principle (SRP)**: The `InventoryManager` class has one reason to change, which is to manage inventory. No other responsibilities are placed on it.
- **Open/Closed Principle (OCP)**: The class is closed for modification but open for extension. The singleton nature does not affect its ability to extend functionality in the future regarding inventory management.

## Factory Pattern and SOLID
- **Single Responsibility Principle (SRP)**: The `PizzaFactory` has the sole responsibility of creating pizza objects.
- **Open/Closed Principle (OCP)**: The factory can be extended to support new pizza types without modifying the existing code.

## Decorator Pattern and SOLID
- **Single Responsibility Principle (SRP)**: Each topping class has one responsibility: to add its specific behavior to the pizza.
- **Open/Closed Principle (OCP)**: New toppings can be added without modifying existing classes, thus keeping the original pizza and topping implementations intact.

### Conclusion
By employing these design patterns, our pizza restaurant system adheres to SOLID principles, enhancing maintainability, extensibility, and overall code quality.
