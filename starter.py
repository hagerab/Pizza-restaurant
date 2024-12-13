from abc import ABC, abstractmethod

# Singleton Inventory Manager
class InventoryManager:
    _instance = None
    _inventory = {
        "Margherita": 10,
        "Pepperoni": 10,
        "Cheese": 15,
        "Olives": 10,
        "Mushrooms": 12,
    }

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

    def check_and_decrement(self, item: str) -> bool:
        if self._inventory.get(item, 0) > 0:
            self._inventory[item] -= 1
            return True
        return False

    def get_inventory(self):
        return self._inventory


# Abstract Pizza Class
class Pizza(ABC):
    @abstractmethod
    def get_description(self) -> str:
        pass

    @abstractmethod
    def get_cost(self) -> float:
        pass


# Base Pizzas
class Margherita(Pizza):
    def get_description(self) -> str:
        return "Margherita Pizza"

    def get_cost(self) -> float:
        return 5.0


class Pepperoni(Pizza):
    def get_description(self) -> str:
        return "Pepperoni Pizza"

    def get_cost(self) -> float:
        return 6.0


# Decorator for Toppings
class ToppingDecorator(Pizza):
    def __init__(self, pizza: Pizza):
        self._pizza = pizza

    @abstractmethod
    def get_description(self) -> str:
        pass

    @abstractmethod
    def get_cost(self) -> float:
        pass


class Cheese(ToppingDecorator):
    def get_description(self) -> str:
        return self._pizza.get_description() + ", Cheese"

    def get_cost(self) -> float:
        return self._pizza.get_cost() + 1.0


class Olives(ToppingDecorator):
    def get_description(self) -> str:
        return self._pizza.get_description() + ", Olives"

    def get_cost(self) -> float:
        return self._pizza.get_cost() + 0.5


class Mushrooms(ToppingDecorator):
    def get_description(self) -> str:
        return self._pizza.get_description() + ", Mushrooms"

    def get_cost(self) -> float:
        return self._pizza.get_cost() + 0.7


# Pizza Factory
class PizzaFactory:
    @staticmethod
    def create_pizza(choice: str, inventory: InventoryManager) -> Pizza:
        if choice == "1" and inventory.check_and_decrement("Margherita"):
            return Margherita()
        elif choice == "2" and inventory.check_and_decrement("Pepperoni"):
            return Pepperoni()
        else:
            print("Pizza unavailable or out of stock!")
            return None


# Payment Strategies
class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount: float) -> None:
        pass


class PayPalPayment(PaymentStrategy):
    def pay(self, amount: float) -> None:
        print(f"Paid ${amount:.2f} using PayPal.")


class CreditCardPayment(PaymentStrategy):
    def pay(self, amount: float) -> None:
        print(f"Paid ${amount:.2f} using Credit Card.")

class Cash(PaymentStrategy):
    def pay(self, amount: float) -> None:
        print(f"Paid ${amount:.2f} using Cash.")



# Main Function
def main():
    inventory_manager = InventoryManager()

    print("Welcome to the Pizza Restaurant!")

    while True:
        # Choose Pizza
        print("\nChoose your base pizza:")
        print("1. Margherita ($5.0)")
        print("2. Pepperoni ($6.0)")
        print("0 => Exit")
        pizza_choice = input("Enter the number of your choice: ")

        if pizza_choice == "0":
            break

        # Create Pizza
        pizza = PizzaFactory.create_pizza(pizza_choice, inventory_manager)
        if not pizza:
            continue

        # Add Toppings
        while True:
            print("\nAvailable toppings:")
            print("1. Cheese ($1.0)")
            print("2. Olives ($0.5)")
            print("3. Mushrooms ($0.7)")
            print("4. Finish order")
            topping_choice = input("Enter the number of your choice: ")

            if topping_choice == "1" and inventory_manager.check_and_decrement("Cheese"):
                pizza = Cheese(pizza)
            elif topping_choice == "2" and inventory_manager.check_and_decrement("Olives"):
                pizza = Olives(pizza)
            elif topping_choice == "3" and inventory_manager.check_and_decrement("Mushrooms"):
                pizza = Mushrooms(pizza)
            elif topping_choice == "4":
                break
            else:
                print("Topping unavailable or out of stock!")

        # Display Final Pizza
        print("\nYour order:")
        print(f"Description: {pizza.get_description()}")
        print(f"Total cost: ${pizza.get_cost():.2f}")

        # Choose Payment Method
        print("\nChoose payment method:")
        print("1. PayPal")
        print("2. Credit Card")
        print("3. Cash")

        payment_choice = input("Enter the number of your choice: ")
        if payment_choice == "1":
            payment = PayPalPayment()
        elif payment_choice == "2":
            payment = CreditCardPayment()
        elif payment_choice == "3":
            payment = Cash()
        else:
            print("Invalid payment method!")
            continue

        # Process Payment
        payment.pay(pizza.get_cost())

        # Show Remaining Inventory
        print("\nRemaining Inventory:")
        print(inventory_manager.get_inventory())


if __name__ == "__main__":
    main()
