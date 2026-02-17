from Cl_Contact import Contact

listContacts = []

def existsContact(id):
    for contact in listContacts:
        if contact.id == id:
            return True
    return False

def addContact():
    id = input("Enter contact ID: ")
    if existsContact(id):
        print("Contact with this ID already exists.")
    else:
        name = input("Enter contact name: ")
        phoneNumber = input("Enter contact phone number: ")
        email = input("Enter contact email: ")
        newContact = Contact(id, name, phoneNumber, email)
        listContacts.append(newContact)
        print("Contact added successfully.")

def showContacts():
    if not listContacts:
        print("No contacts to show.")
    else:
        for contact in listContacts:
            print(contact.showContact())
            print("--------------------")

def searchContact():
    while True:
        print("Search Contact Menu:")
        print("1. Search by Name")
        print("2. Search by Phone Number")
        print("3. Return to Main Menu")
        choice = input("Enter your choice: ")
        if choice == "1":
            name = input("Enter name to search: ")
            found = False
            for contact in listContacts:
                if contact.name == name:
                    print("Contact found:")
                    print(contact.showContact())
                    found = True
                    break
            if not found:
                print("Contact not found.")
        elif choice == "2":
            phone = input("Enter phone number to search: ")
            found = False
            for contact in listContacts:
                if contact.phoneNumber == phone:
                    print("Contact found:")
                    print(contact.showContact())
                    found = True
                    break
            if not found:
                print("Contact not found.")
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")

def modifyContact():
    id = input("Enter the ID of the contact to modify: ")
    if existsContact(id):
        for contact in listContacts:
            if contact.id == id:
                print("Current details:", contact.showContact())
                contact.name = input("Enter new name (leave blank to keep current): ") or contact.name
                contact.phoneNumber = input("Enter new phone number (leave blank to keep current): ") or contact.phoneNumber
                contact.email = input("Enter new email (leave blank to keep current): ") or contact.email
                print("Contact updated successfully.")
    else:
      print("Contact with this ID not found.")
    
def deleteContact():
    id = input("Enter the ID of the contact to delete: ")
    if not existsContact(id):
        print("Contact with this ID does not exist.")
    else:
        for contact in listContacts:
            if contact.id == id:
                listContacts.remove(contact)
                print("Contact deleted successfully.")
        
def main():
    while True:
        print("Main Menu:")
        print("1. Add Contact")
        print("2. Show Contacts")
        print("3. Search Contact")
        print("4. Modify Contact")
        print("5. Delete Contact")
        print("6. Exit")
        choice = input("Select an option (1-6): ")
        if choice == "1":
            addContact()
        elif choice == "2":
            showContacts()
        elif choice == "3":
            searchContact()
        elif choice == "4":
            modifyContact()
        elif choice == "5":
            deleteContact()
        elif choice == "6":
            print("Exiting the program.")
            break
        else:
            print("Invalid option. Please try again.")
            
if __name__ == "__main__":
    main()