# ============================================================
#  CONTACT MANAGER CLI
#  Chapter 8 Level — Functions only, no classes, no files yet
#  Every concept here is from Python Crash Course Chapter 1–8
# ============================================================

# This list stores all contacts.
# Each contact is a dictionary: {"name": ..., "phone": ..., "email": ...}
# You learned lists in Ch 4, dictionaries in Ch 6.
contacts = []


# ── FUNCTION 1 ───────────────────────────────────────────────
# add_contact() — asks user for details and adds to the list
# Concept: functions with no parameters (Ch 8)
def add_contact():
    print("\n--- ADD CONTACT ---")
    name  = input("Enter name  : ").strip()
    phone = input("Enter phone : ").strip()
    email = input("Enter email : ").strip()

    # Build a dictionary for this contact (Ch 6)
    contact = {
        "name" : name,
        "phone": phone,
        "email": email,
    }

    # Append the dictionary into our contacts list (Ch 4)
    contacts.append(contact)
    print(f"\n✅ '{name}' has been added.")


# ── FUNCTION 2 ───────────────────────────────────────────────
# view_contacts() — prints every contact neatly
# Concept: looping over a list (Ch 4), f-strings (Ch 2)
def view_contacts():
    print("\n--- ALL CONTACTS ---")

    # If the list is empty, tell the user
    if len(contacts) == 0:
        print("No contacts yet. Add one first.")
        return  # exit the function early (Ch 8)

    # Loop through the list and print each contact
    for index, contact in enumerate(contacts, start=1):
        print(f"\n[{index}] Name  : {contact['name']}")
        print(f"    Phone : {contact['phone']}")
        print(f"    Email : {contact['email']}")

    print(f"\nTotal contacts: {len(contacts)}")


# ── FUNCTION 3 ───────────────────────────────────────────────
# search_contact() — finds contacts whose name matches a keyword
# Concept: functions with a parameter (Ch 8), string methods (Ch 2)
def search_contact(keyword):
    print(f"\n--- SEARCH RESULTS FOR '{keyword}' ---")

    # Build a new list of matches (Ch 4 — list operations)
    results = []
    for contact in contacts:
        # .lower() makes the search case-insensitive
        if keyword.lower() in contact["name"].lower():
            results.append(contact)

    if len(results) == 0:
        print("No contacts found.")
    else:
        for index, contact in enumerate(results, start=1):
            print(f"\n[{index}] Name  : {contact['name']}")
            print(f"    Phone : {contact['phone']}")
            print(f"    Email : {contact['email']}")


# ── FUNCTION 4 ───────────────────────────────────────────────
# delete_contact() — removes a contact by name
# Concept: functions, list .remove(), looping (Ch 4, Ch 8)
def delete_contact():
    print("\n--- DELETE CONTACT ---")

    if len(contacts) == 0:
        print("No contacts to delete.")
        return

    view_contacts()  # show the list first so user knows what to delete
    name_to_delete = input("\nEnter the exact name to delete: ").strip()

    # Search for the contact in the list
    contact_found = None
    for contact in contacts:
        if contact["name"].lower() == name_to_delete.lower():
            contact_found = contact
            break  # stop searching once found

    if contact_found:
        contacts.remove(contact_found)
        print(f"\n✅ '{name_to_delete}' has been deleted.")
    else:
        print(f"\n❌ No contact named '{name_to_delete}' was found.")


# ── FUNCTION 5 ───────────────────────────────────────────────
# show_menu() — prints the options menu
# Concept: simple function, print statements (Ch 8)
def show_menu():
    print("\n============================")
    print("    CONTACT MANAGER")
    print("============================")
    print("1 — Add a contact")
    print("2 — View all contacts")
    print("3 — Search contacts")
    print("4 — Delete a contact")
    print("5 — Quit")
    print("============================")


# ── MAIN PROGRAM LOOP ────────────────────────────────────────
# This is the engine of the app.
# It shows the menu, takes input, and calls the right function.
# Concept: while loop (Ch 7), if/elif/else (Ch 5), input() (Ch 7)

def main():
    print("Welcome to Contact Manager!")

    while True:  # keep running until user chooses Quit
        show_menu()
        choice = input("Choose an option (1–5): ").strip()

        if choice == "1":
            add_contact()

        elif choice == "2":
            view_contacts()

        elif choice == "3":
            keyword = input("Enter name to search: ").strip()
            search_contact(keyword)

        elif choice == "4":
            delete_contact()

        elif choice == "5":
            print("\nGoodbye! 👋")
            break  # exit the while loop and end the program

        else:
            print("\n⚠️  Invalid choice. Please enter a number from 1 to 5.")


# ── ENTRY POINT ──────────────────────────────────────────────
# This line means: only run main() if we run THIS file directly.
# You will learn why this matters more in Ch 9 and beyond.
if __name__ == "__main__":
    main()