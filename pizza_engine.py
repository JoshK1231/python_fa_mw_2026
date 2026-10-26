"""
-----------------------------------------------------------------------
ASSIGNMENT 10A: THE RESILIENT PIZZA ENGINE
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. Global constant TOPPINGS defined as a Tuple in ALL_CAPS.
[ ] 3. Function 'make_pizza' defines 4 specific parameters.
[ ] 4. 'make_pizza' uses a DEFAULT value for is_delivery.
[ ] 5. main() displays the Global Pantry list to the user.
[ ] 6. main() calls the function using KEYWORD ARGUMENTS.
-----------------------------------------------------------------------
"""
"""
-----------------------------------------------------------------------
Name:Joshua Kline
DATE: [10/26/2026]
FILE: pizza_engine.py
-----------------------------------------------------------------------
"""
#GLOBAL CONSTANTS
TOPPINGS = ("Cheese","Pepporoni","Sausage","Bacon")
SIZE = ("8 inch", "10 inch", "12 inch")
def make_pizza(customer, size, topping, is_delivery=False):
    print(f"\n--- OFFICIAL TICKET: {customer.upper()} ---")
    print(f"Customer: {customer}")
    print(f"Size: {size}")
    print(f"Toppings: {topping}")
    print(f"Delivery: {is_delivery}")
def main():
    user = input ("Customer Name: ").title()
    print(f"Options: {TOPPINGS}") # Accessing Global Scope
    choice_topping = input("Select Toppings: ")
    delivery = input("Delivery? (yes/no): ").lower
    try:
        choice_size = int(input("Enter size: "))
    except ValueError:
        print("Invalid input. Defaulting to 10 inches")
        size=10
    #KEYWORD HANDOFF
    make_pizza(customer=user, size=choice_size, topping=choice_topping, is_delivery=delivery)
main()
