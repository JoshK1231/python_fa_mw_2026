# Name check
# Rules - cant be empty
# less than 30 charatcers
fname = ""
while not fname:
    fname = input("Please enter your first name: ")
    print(f"before: fname")
    fn_length = len(fname)
    print(f"length before: {fn_length}")
    fname = fname.strip()
    print(f"first name after {fname}")
    fn_legnth = len(fname)
    print(f"length after: {fn_legnth}")
try:
    fname = ""
    while not fname:
        fname = input("Please enter your first name: ")
        fname = fname.strip()

        age = -1
        while age < 0:
            age = int(
                input("please enter your child's age: (whole years, round down) ")
            )

except ValueError:
    print("I'm sorry, that is not a valid value")
except Exception as e:
    print(f"Error: {e}")
