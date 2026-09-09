"""
-----------------------------------------------------------------------
ASSIGNMENT: 3B - The Buffet Calculator (Daily Specials)
Name:Joshua Kline
DATE: [9/8/2026]
FILE: Conditonal-logic.py
-----------------------------------------------------------------------
-----------------------------------------------------------------------
"""
Day = input ("Enter Day of the week: ").lower()
Age = int(input ("Please enter your age: "))

match Day:
    case "monday":
        child_price_per_year = 1.00
    case "tuesday":
        child_price_per_year = 0.50
    case "wednesday":
        child_price_per_year = 1.00
    case "thursday":
        child_price_per_year = 1.00
    case "friday":
        child_price_per_year = 1.00
    case "saturday":
        child_price_per_year = 1.00
    case "sunday":
        child_price_per_year= 1.00
        print("Drinks are free today!!!")

if Age < 1:
    print ("Free ($0.00)")
    price = 0.00
elif Age < 13:
    print ("Age mutiplied by price per year")
    price = Age * child_price_per_year
elif Age <65: 
    print("16.95")
elif Age >= 65:
    print("$12.95")
    price = 12.95


print(f"Your total is ${price:.2f}")







