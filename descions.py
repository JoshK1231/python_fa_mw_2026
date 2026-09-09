"""
-----------------------------------------------------------------------
ASSIGNMENT: 3B - The Buffet Calculator (Daily Specials)
DATE: [Insert Date]
FILE: buffet.py
-----------------------------------------------------------------------
REQUIREMENTS:
1. Ask the user for their age (convert to int) and the day of the week (convert to string).
2. Calculate the base price using if/elif/else:
   - Under 1: FREE ($0.00)
   - 1 to 11: $1.00 per year of age (Example: 5 years = $5.00)
   - 12 to 64: $16.95 (Standard Adult)
   - 65 and older: $12.95 (Senior Discount)
3. Use a match/case statement to handle special daily rules based on the day entered:
   - Tuesday: Children through age 12 are half price!
   - Sunday: Drinks are free!
   - Other days: Standard buffet pricing in effect.
4. Print the final price formatted as currency and display any applicable daily special notices.
-----------------------------------------------------------------------
"""

                     
day = input("Please enter the day of the week: ")
age = input ("Please enter the your age: ")

print (f"the day is {Day}")


if age < 1:
print ("Free $0.00")
elif <= 11: 
print ("$1.00 per year of age (Example: 5 years = $5.00)")
elif<= 64:
print ("$16.95 Standard Adult")
elif age >= 65:
print ("$12.95 (Senior Discount)")
if day = Tuesday:
print("Children through age 12 are half price!")
if day = 