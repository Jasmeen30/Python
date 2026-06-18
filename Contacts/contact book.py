contacts = {}
numbers = set()

n = int(input("Enter number of contacts: "))

# Add multiple contacts
for i in range(n):
    name = input("Enter name: ")
    phone = input("Enter phone number: ")

    if phone in numbers:
        print("Duplicate phone number not allowed!")
    else:
        contacts[name] = phone
        numbers.add(phone)

# Search Contact
search_name = input("\nEnter name to search: ")
if search_name in contacts:
    print("Phone Number:", contacts[search_name])
else:
    print("Contact not found.")

# Update Contact
update_name = input("\nEnter name to update: ")
if update_name in contacts:
    new_phone = input("Enter new phone number: ")

    if new_phone in numbers:
        print("Duplicate phone number detected!")
    else:
        numbers.remove(contacts[update_name])
        contacts[update_name] = new_phone
        numbers.add(new_phone)
        print("Contact updated.")
else:
    print("Contact not found.")

# Delete Contact
delete_name = input("\nEnter name to delete: ")
if delete_name in contacts:
    numbers.remove(contacts[delete_name])
    del contacts[delete_name]
    print("Contact deleted.")
else:
    print("Contact not found.")

# Display Contacts
print("\nAll Contacts:")
for name, phone in contacts.items():
    print(name, ":", phone)