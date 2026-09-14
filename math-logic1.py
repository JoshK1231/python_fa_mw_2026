"""
-----------------------------------------------------------------------
ASSIGNMENT REQUIREMENTS
-----------------------------------------------------------------------
ASSIGNMENT: 4A: Boolean Logic
Name:Joshua Kline
DATE: [9/14/2026]
FILE: math-logic.py
-----------------------------------------------------------------------
"""
#---"CHARACTERS"---
player = "Randy"
enemy = "Stan"

# --- "VOCAB FOR CHARACTERS ACTION"---

ACTION_ATTACK_SPELL = 1
ACTION_SWING_SWORD = 2
ACTION_DEFEND = 3
ACTION_MOVE = 4
ACTION_USE_ITEM = 5
ACTION_FLEE_FIGHT = 6

print (f"{player} attacks {enemy}")
print (f"{player} defends")
print (f"{player} uses and item")
print (f"{player} moves")
#---"USER INPUT"---
print("Decide what {player} does on his turn")
choice_1 = int(input( "first action (pick 1-6): "))
choice_2 = int(input("Second action (pick1-6): "))

#---"LOGIC"---
#OR
if choice_1 == ACTION_ATTACK_SPELL or ACTION_SWING_SWORD:
    print(f"\{player} attacks {enemy}")
    print(f"{enemy} takes damage")
    #AND
if choice_1 == ACTION_MOVE and choice_2 == ACTION_DEFEND:
    print(f"\n{player} moves and defends")
    print(f"{enemy} will deal reduced damage vs {player} next turn")
if choice_1 == ACTION_ATTACK_SPELL and choice_2== ACTION_MOVE:
    print(f"n\ {player} uses and attack spell and moves out of the way")
    print(f"{enemy} takes damage")
if choice_1 == ACTION_SWING_SWORD and choice_2==ACTION_MOVE:
    print(f"n\{player} swings his sword and moves out of the way")
    print(f"{enemy} takes damage")

#ELSE/ELIF
elif choice_1 == 4:
    print(f"\n {player} flees from the fight")
elif choice_1 == ACTION_USE_ITEM:
    print(f"\n {player} uses an item. He can take no further action this turn")
elif not (choice_1 < 1 and choice_1 > 6):
    print (f"\n this action is not valid")
elif not (choice_2 < 1 and choice_2 > 6):
    print (f"\n this action is not valid")
else :
    print (f"\n this action is not valid")