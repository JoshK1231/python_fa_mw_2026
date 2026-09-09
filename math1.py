#--- 1. GET INPUT
gross_income = float(input("Enter Monthly Gross income: $"))
rent = float(input("Enter Monthly Rent/Housing expense: $"))
Utilities = float(input("Monthly Utilities expense: $"))
Hobbies = float(input("Monthly hobbie expense: $"))
Gas = float(input("Monthly Gas expense: $"))
Dining_Out = float(input("Monthly Dining expense: $"))

# 2. CALCULATIONS
total_expenses = rent + Utilities + Hobbies + Gas + Dining_Out
net_income = gross_income * .8
remaining_balance = net_income - total_expenses
percentage_spent = total_expenses / gross_income

# 3. FORMATTED OUTPUT
print(f"You spent a toal of {total_expenses:,.2f} ")
print(f"That was {total_expenses / net_income: .2%} of your net income")