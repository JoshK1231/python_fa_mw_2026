"""
-----------------------------------------------------------------------
ASSIGNMENT 9A: THE SMOOTHIE SPRINT
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. Global Constants BASES and FRUITS defined as Tuples.
[ ] 3. Professional function get_price(size) returns a float.
[ ] 4. Professional function blend(size, base, fruit, scoops) for output.
[ ] 5. main() function handles try/except for scoops (int).
[ ] 6. main() calls both functions correctly.
-----------------------------------------------------------------------
"""
"""
-----------------------------------------------------------------------
ASSIGNMENT 9A: THE SMOOTHIE SPRINT
-----------------------------------------------------------------------
Name:Joshua Kline
DATE: [10/19/2026]
FILE: Smoothie_bar.py
-----------------------------------------------------------------------
"""

# GLOBAL CONSTANTS (The Pantry)
BASES = ("Water", "Apple Juice", "Orange Juice", "Milk")
FRUITS = ("Strawberry", "Banana", "Mango", "Blueberry")

# TODO: Define get_price(size)
def get_base_price(size):
    if size == "Small":
        return 3.00
    elif size == "Medium":
        return 4.00
    else:
        return 5.00
# TODO: Define blend(size, base, fruit, scoops)
def blend(size, base, fruit, scoops):
    print("n--- Blending Order ---")
    print(f"Size: {size}")
    print(f"Base: {base}")
    print(f"Fruit: {fruit}")
    print(f"Scoops: {scoops}")

# TODO: Define main() to collect input and call your logic
def main():
    print("Welcome to the Smoothie Bar")
    choice_size = input("Size (Small/Medium/Large): ").title().strip()
    choice_base = input("Select Base (Water/Apple Juice/Orange Juice/milk)")
    choice_fruit = input("Select Fruit (Strawberry/Bannana/Mango/Blueberry)")
    try:
        scoops = int(input("How many scoops of fruit?"))
    except ValueError:
        print("Invalid entry. Defaulting to 1.")
        scoops = 1
    cost = get_base_price(choice_size)
    blend(choice_size, choice_base, choice_fruit, scoops)
    print(f"Total Bill: ${cost:.2f}")
main()