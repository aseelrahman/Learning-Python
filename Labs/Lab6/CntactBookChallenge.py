# Create empty dictionaries to start.
new_contact1 = dict();
new_contact2 = dict();

# NOTE: We can create an empty dictionary with culy braces
new_contact3 = {};

# Get the information for each contact below from the end user.
new_contact1['full_name'] = input("Enter full name for contact 1: ")
new_contact1['phone'] = input("Enter phone number for contact 1: ")
new_contact1['email'] = input("Enter email address for contact 1: ")
print()

new_contact2['full_name'] = input("Enter full name for contact 2: ")
new_contact2['phone'] = input("Enter phone number for contact 2: ")
new_contact2['email'] = input("Enter email address for contact 2: ")
print()

new_contact3['full_name'] = input("Enter full name for contact 3: ")
new_contact3['phone'] = input("Enter phone number for contact 3: ")
new_contact3['email'] = input("Enter email address for contact 3: ")
print()

# Create a List with the contacts.
contacts = [
    new_contact1,
    new_contact2,
    new_contact3
]


'''
Iterate over items in the contacts List.
NOTE: We will discuss loops at a later time. For now, type everythign you see 
below including ALL indentations.
'''

print("Contact Directory: ")
# Output 1
contact_id = 1
for contact in contacts:
    # Below we are accessing the keys by their name:
    print(f"{contact_id} {contact['full_name']:<15s}{contact['phone']:<15s}{contact['email']:<15s}")

    contact_id = contact_id + 1
print()

# Update a contact section
contact_index_to_update = int(input("Which contact do you want to update? "))

# Remember the index is off by one from the natural count, so we need to minus 1.
contact_index_to_update = contact_index_to_update -1

print(f"\nUpdating contact: {contacts[contact_index_to_update]['full_name']}\n")

contacts[contact_index_to_update]['full_name'] = input(f"Enter new full name: ")
contacts[contact_index_to_update]['phone'] = input(f"Enter new phone number: ")
contacts[contact_index_to_update]['email'] = input(f"Enter new email address: ")
print()

#Output 2
print("Contact Directory: ")
contact_id = 1
for contact in contacts:
    print(f"{contact_id} {contact['full_name']:<15s}{contact['phone']:<15s}{contact['email']:<15s}")

    contact_id = contact_id + 1
print()

contact_index_to_delete = int(input("Which contact do you want to delete? "))
contact_index_to_delete = contact_index_to_delete - 1
print()

#Remove the contact form the list.
del contacts[contact_index_to_delete]

# Output 3
print("Contact Directory: ")
contact_id = 1
for contact in contacts:
    print(f"{contact_id} {contact['full_name']:<15s}{contact['phone']:<15s}{contact['email']:<15s}")

    contact_id = contact_id + 1
print()