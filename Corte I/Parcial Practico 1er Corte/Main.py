from Cl_Ticket import ticket

listTickets = []

def Menu():
    print("Ticket Management System")
    print("1. Add Ticket")
    print("2. Search Ticket")
    print("3. Modify Ticket")
    print("4. Delete Ticket")
    print("5. Exit")

def existTicket(numTicket):
    for i in listTickets:
        if i.numTicket == numTicket:
            return True
    return False

def addTicket():
    numTicket = input("Enter the Ticket Number: ")
    buyDay = input("Enter the Day of the Week (e.g., monday, tuesday): ").lower()
    if existTicket(numTicket):
        print("\nThe Ticket Number already exists.")
    else:
        nameClient = input("Enter the Client Name: ")
        cedulaClient = input("Enter the Client ID: ")
        costTicket = input("Enter the Cost of Ticket: ")
        cantTicket = input("Enter the Number of Tickets: ")
        nameMovie = input("Enter the Movie Name: ")
        newTicket = ticket(numTicket, nameClient, cedulaClient, costTicket, cantTicket, nameMovie, buyDay)
        listTickets.append(newTicket)
        print("-" * 35)
        print("Ticket added successfully.")
        print("-" * 35)
        
def searchTicket():
    numTicket = input("\nEnter the Ticket Number to search: ")
    if not existTicket(numTicket):
        print("The Ticket Number does not exist.")
    else:
        for i in listTickets:
            if i.numTicket == numTicket:
                i.ShowTicket()
                print("-" * 35)
            
def modifyTicket():
    numTicket = input("\nEnter the Ticket Number to modify: ")
    if not existTicket(numTicket):
        print("The Ticket Number does not exist.")
    else:
        for i in listTickets:
            if i.numTicket == numTicket:
                print("\nEnter new details for the ticket:")
                i.nameClient = input("Enter the Client Name: ") or i.nameClient
                i.cedulaClient = input("Enter the Client ID: ") or i.cedulaClient
                i.costTicket = int(input("Enter the Cost of Ticket: ") or i.costTicket)
                i.cantTicket = int(input("Enter the Number of Tickets: ") or i.cantTicket)
                i.nameMovie = input("Enter the Movie Name: ") or i.nameMovie
                i.buyDay = input("Enter the Day of the Week (e.g., monday, tuesday): ").lower() or i.buyDay
                print("-" * 35)
                print("Ticket modified successfully.")
                print("-" * 35)
            
def deleteTicket():
    numTicket = input("\nEnter the Ticket Number to delete: ")
    if not existTicket(numTicket):
        print("The Ticket Number does not exist.")
    else:
        for i in listTickets:
            if i.numTicket == numTicket:
                listTickets.remove(i)
                print("Ticket deleted successfully.")

def main():
    while True:
        Menu()
        choice = input("\nEnter your choice: ")
        if choice == "1":
            addTicket()
        elif choice == "2":
            searchTicket()
        elif choice == "3":
            modifyTicket()
        elif choice == "4":
            deleteTicket()
        elif choice == "5":
            print("Exiting the program.")
            break
        else:
            print("-" * 35)
            print("Invalid choice. Please try again.")
            print("-" * 35)
        
if __name__ == "__main__":
    main()