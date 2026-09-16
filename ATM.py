print(f" 1.Create new contact")
print(f" 2. Search contacts")
print(f" 3. update contact")
print(f" 4. Delete contact")
print(f" 5. Quit")
# get user choice

choice = 1
while choice > 0 and choice < 4:
    choice = int(
        input("Please enter the number of your selection: ")
    )  # Create new contacts
    match choice:

        case 1:
            print("Create")
        case 2:
            print("Search")

        case 3:
            print("Update")
        case 4:
            print("Delete")
        case 5:
            print("Good bye")
