# Contact Book Application

contacts = []


def is_valid_phone(phone):
    return phone.isdigit() and len(phone) == 10


def display_contact(contact):
    print("Name   :", contact["Name"])
    print("Phone  :", contact["Phone"])
    print("Email  :", contact["Email"])
    print("Address:", contact["Address"])


while True:
    print("\n===== CONTACT BOOK =====")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        name = input("Enter Name: ")
        phone = input("Enter Phone Number: ")

        if not is_valid_phone(phone):
            print("Invalid phone number! Please enter 10 digits only.")
            continue

        duplicate = False
        for contact in contacts:
            if contact["Phone"] == phone:
                duplicate = True
                break

        if duplicate:
            print("This phone number already exists.")
            continue

        email = input("Enter Email: ")
        address = input("Enter Address: ")

        contact = {
            "Name": name,
            "Phone": phone,
            "Email": email,
            "Address": address
        }

        contacts.append(contact)
        print("Contact Added Successfully!")

    elif choice == "2":
        if not contacts:
            print("No Contacts Available.")
        else:
            print("\n===== CONTACT LIST =====")
            for index, contact in enumerate(contacts, start=1):
                print(f"\nContact {index}")
                display_contact(contact)

    elif choice == "3":
        search_value = input("Enter name or phone number to search: ").lower()

        found = False

        for contact in contacts:
            if contact["Name"].lower() == search_value or contact["Phone"] == search_value:
                print("\nContact Found")
                display_contact(contact)
                found = True

        if not found:
            print("Contact Not Found.")

    elif choice == "4":
        search_value = input("Enter name or phone number to update: ").lower()

        found = False

        for contact in contacts:
            if contact["Name"].lower() == search_value or contact["Phone"] == search_value:
                print("\nCurrent Contact Details:")
                display_contact(contact)

                new_name = input("Enter New Name: ")
                new_phone = input("Enter New Phone Number: ")

                if not is_valid_phone(new_phone):
                    print("Invalid phone number! Please enter 10 digits only.")
                    found = True
                    break

                duplicate = False
                for other_contact in contacts:
                    if other_contact != contact and other_contact["Phone"] == new_phone:
                        duplicate = True
                        break

                if duplicate:
                    print("This phone number already exists.")
                    found = True
                    break

                new_email = input("Enter New Email: ")
                new_address = input("Enter New Address: ")

                contact["Name"] = new_name
                contact["Phone"] = new_phone
                contact["Email"] = new_email
                contact["Address"] = new_address

                print("Contact Updated Successfully!")
                found = True
                break

        if not found:
            print("Contact Not Found.")

    elif choice == "5":
        if not contacts:
            print("No Contacts Available.")
        else:
            print("\n===== CONTACT LIST =====")
            for index, contact in enumerate(contacts, start=1):
                print(f"{index}. {contact['Name']} - {contact['Phone']}")

            try:
                delete_index = int(input("Enter contact number to delete: "))

                if 1 <= delete_index <= len(contacts):
                    removed_contact = contacts.pop(delete_index - 1)
                    print(f"{removed_contact['Name']} has been deleted successfully.")
                else:
                    print("Invalid contact number!")

            except ValueError:
                print("Please enter a valid number.")

    elif choice == "6":
        print("Exiting Contact Book...")
        break

    else:
        print("Invalid Choice! Please select between 1 and 6.")