"""
-----------------------------------------------------------------------
ASSIGNMENT 5A: INPUT VALIDATION
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. All 5 inputs have 'while' loop validation.
[ ] 3. The more tickets loop uses .upper() and correct Boolean logic.
[ ] 4. Include a try and except statement around the entire program. Should have one defined
       exception (probably value error) and a generic exception
[ ] 5. Have pinned a variable in the WATCH window and took a screenshot.
-----------------------------------------------------------------------
"""

fname = ""
while not fname:
    fname = input("Please enter your first name: ")
fname = fname.strip()
lname = ""
while not lname:
    lname = input("Please enter your last name: ")
    lname = lname.strip

    age = -1
    while age < 0:
        age = int(input("please enter your age: (whole years, round down) "))
    if age >= 21:
        print("The customer can order alcoholic beverages")
    elif age < 21:
        print("Customer cannot order alcohol")

phone_number = ""
phone_number = int(input("please enter your phone number: "))

tickets = -1
while tickets > 
