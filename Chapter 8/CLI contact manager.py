def add_contact():
    while True:
        print("\nEnter 'q' to exit.")
        name = input("Enter name: ").strip()
        if name == "q":
            break

        number = input("Enter number: ").strip()
        if number == "q":
            break
        else:
            if name in contact:
                print(f"\nContact {name.title()} already exists\n")
            else:
                contact[name.lower()] = number
def view_contact():
    print("Stored contacts:\n")
    if contact:
        for k, v in contact.items():
            print(f"-{k.title()} : {v}")
        print("\n")
    else:
        print("\nNo contact found\n")
def delete_contact():

    remove_contact = input("Enter name to delete: ")
    remove_contact = remove_contact.lower()
    if remove_contact in contact:
        del contact[remove_contact.lower()]
        print(f"\nContact {remove_contact.title()} deleted\n")

    else:
        print("\nThis contact does not exist\n")



contact = {}
while True:



    print("Contact Manager\n")
    print("1. Add contact")
    print("2. View contact")
    print("3. Delete contact")
    print("4. Exit")


    choice= input("\nChoose an option: ")
    if choice == "1":
        add_contact()
    elif choice == "2":
        view_contact()
    elif choice == "3":
        delete_contact()
    elif choice == "4":
        break
    else:
        print("\nInvalid option\n")