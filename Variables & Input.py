"""
-----------------------------------------------------------------------
ASSIGNMENT REQUIREMENTS
-----------------------------------------------------------------------
[ ] 1. Header Docstring included (Copy and paste THIS comment from opening to closing quotes).
[ ] 2. Program asks for at least 5 different inputs (variables).
[ ] 3. Output uses F-Strings to combine text and variables.
[ ] 4. Output uses at least one escape sequence (\n or \t).
[ ] 5. Code contains comments explaining the steps.
[ ] 6. Program runs without errors.
-----------------------------------------------------------------------
"""

# ℹ️ information only
# 🆘 HELP!


# ℹ️ Delcare variables
# name = "" # ℹ️ intializes variable.
# light_source = ""
# size= ""
# feeling= ""
# color= ""
# Progam is displaying entered name,light_source,size,feeling, and color in My little Sunishine


# ℹ️ Get user input and assign to variables
name = input("Please enter a persons name: ")
light_source = input("Please enter a source of light: ")
size = input("Please enter a size: ")
feeling = input("Please enter a feeling: ")
color = input("Please enter a color: ")

# ℹ️ output
print("Mad lib for You are my Sunshine \n\n")
print(f"{name} is my {light_source}")
print(f"My {size} {light_source}")
print(f"{name} makes me {feeling} when times are {color}")
