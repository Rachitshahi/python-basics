# -----------------------------
# Simple CLI Phone-Book Manager
# -----------------------------

# Pre-populated phone-book dictionary
phone_book = {
    "Alice": "123-456-7890",
    "Bob":   "987-654-3210"
}

# ---------- CRUD OPERATIONS ----------

def add_contact(book: dict) -> None:
    """Add a new contact to the phone book."""
    name   = input("Enter name: ")
    number = input("Enter phone number: ")
    book[name] = number          # Insert / overwrite entry
    print(f"{name} added to phone book.")


def lookup_contact(book: dict) -> None:
    """Look up and display the phone number of a contact."""
    name = input("Enter name to look up: ")
    number = book.get(name, "Contact not found.")   # Safe lookup
    print(f"{name}'s number: {number}")


def update_contact(book: dict) -> None:
    """Update an existing contact’s phone number."""
    name = input("Enter name to update: ")
    if name in book:
        new_number = input("Enter new phone number: ")
        book[name] = new_number   # Modify entry in-place
        print(f"{name}'s number updated.")
    else:
        print(f"{name} not found in phone book.")


def delete_contact(book: dict) -> None:
    """Delete a contact from the phone book."""
    name = input("Enter name to delete: ")
    if name in book:
        del book[name]            # Remove entry
        print(f"{name} deleted from phone book.")
    else:
        print(f"{name} not found in phone book.")


def display_all(book: dict) -> None:
    """Print every contact in the phone book."""
    print("\n--- Phone Book ---")
    if book:
        for name, number in book.items():
            print(f"{name}: {number}")
    else:
        print("Phone book is empty.")
    print("------------------")

# ---------- MAIN MENU LOOP ----------

while True:
    # Display menu options
    print("\nPhone Book Options:")
    print("1. Add Contact")
    print("2. Look Up Contact")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. Display All")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    # Dispatch to the appropriate function
    if choice == '1':
        add_contact(phone_book)
    elif choice == '2':
        lookup_contact(phone_book)
    elif choice == '3':
        update_contact(phone_book)
    elif choice == '4':
        delete_contact(phone_book)
    elif choice == '5':
        display_all(phone_book)
    elif choice == '6':
        print("Exiting Phone Book.")
        break                     # Terminate the loop and program
    else:
        print("Invalid choice. Please try again.")
