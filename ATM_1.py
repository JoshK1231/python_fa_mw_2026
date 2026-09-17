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
is_running= True
choice = 1
while choice > 0 and choice < 5:
        while choice > 0 and choice < 5: is_running = True
        print(f" 1. Show Balance")
        print(f" 2. Deposit cash")
        print(f" 3.Withdraw cash")
        print(f" 4. Transfer cash")
        print(f" 5. Exit")
try:
        choice = int(input("Please enter the number of your selection: "))
except ValueError:
        print("Input invalid. Please choose a number between 1-5")
match choice:
    case 1:
            print("your balance is :${balance:.2f}")
    case 2:
      try:
        deposit = float(input("Enter the amount you would like to deposit: $"))
        if deposit <=0:
            print("Deposit must be greater than $0.")
        else:
            balance += deposit
            print(f"You Deposited: ${deposit:.2f}")
      except ValueError:
          print("Invalid Input")
    case 3:
      try:
        withdraw = float(input("Enter the amount you would like to withdraw: $"))
        if withdraw <=0:
            print("Withdrawl's must be greater than $0.")
        elif withdraw > balance:
         print("Not enough funds to make this withdrawl.")
        else:
            balance -= withdraw
            print ("You withdrew ${withdraw:.2f}")
      except ValueError: 
          print("Invalid input")
    case 4:
      try:  
        transfer = float(input("Enter the amount you would like to transfer: $"))
        if transfer <= 0:
            print("Transfer must be greater than $0")
        elif transfer > balance:
            print("Not enough funds to transfer this amount.")
        else:
            transfer -= transfer
            print ("You transfered: ${transfer:.2f}")
      except ValueError:
          print("Invalid input")  
    case 5:
            print("Exit")
            is_running =False
