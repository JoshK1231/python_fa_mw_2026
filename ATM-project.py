"""
-----------------------------------------------------------------------
ASSIGNMENT REQUIREMENTS
-----------------------------------------------------------------------
[ ] 1. Header Docstring included with assignment info.
[ ] 2. ATM runs in a "while True" loop to remain awake.
[ ] 3. Main menu uses match-case logic for selections.
[ ] 4. Inputs are validated (e.g., .isdigit()) to prevent crashes (include try except)
[ ] 5. Logic prevents overdrafts and negative deposits.
[ ] 6. All currency is formatted to two decimal places (:.2f).
[ ] 7. Upload to GitHub and paste the link below.
-----------------------------------------------------------------------
"""

balance = 1000.00
deposit = 1
withdraw = 1
new_balance = balance + deposit - withdraw
choice = 1
while choice > 0 and choice < 5:
    print(f" 1. Show Balance")
    print(f" 2. Deposit cash")
    print(f" 3.Withdraw cash")
    print(f" 4. Transfer cash")
    print(f" 5. Exit")
    choice = int(input("Please enter the number of your selection: "))
    match choice:
        case 1:
            print("your balance is :${balance}")
        case 2:
            input("Enter the amount you would like to deposit:")
        case 3:
            input("Enter the amount you would like to withdraw:")
        case 4:
            input("Enter the amount you would like to transfer:")
        case 5:
            print("Exit")
