"""
-----------------------------------------------------------------------
ASSIGNMENT REQUIREMENTS
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. Task 1: While Loop (The Nagging Kid)
       - Repeats "Are we there yet?" until user types "yes".
       - Uses a boolean variable to control the loop.
[ ] 3. Task 2: For Loop (99 Bottles of Beer)
       - Counts backwards from 99 to 1.
       - Prints "[number] bottles of beer on the wall!"
[ ] 4. Upload to GitHub and paste the link below.
-----------------------------------------------------------------------
"""
# WHILE LOOPS
score = 0
total = 0
count = 0

while score >= 0:
    print("Enter each test score, enter -1 when done.")
    score = float(input("Enter the test score, enter -1 when done"))
    if score > 0:
    total += score
    count += 1
else:
    print ("Entry completed")
    average = total / count

    print (f"The average test score waas: (average)")

# FOR LOOPS
    for x in range(1,10):
        print(x)
    
    for y in range (10,0, -1):
        print(y)
 for day in ("Sunday" , "Monday" , "Tuesday" , "Wednesday" , "Thursday" , "Friday" , "Saturday")

 eat=false 
 while not eat:
    feed= input("Cane we eat now??? (yes/no)").lower()
