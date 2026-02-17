from Cl_Homework import Homework

listHomeworks = [(Homework("01", "Tarea de Calculo", "High", "1")),
                 (Homework("02", "Tarea de Calculo", "High", "1")),
                 (Homework("03", "Tarea de Algebra", "Low", "1")),
                 (Homework("04", "Tarea de Sistemas", "High", "2")),
                 (Homework("05", "Tarea de Programacion", "Middel", "2"))]

def menu():
    print("Menu:")
    print("1. Add Homework")
    print("2. Show Homeworks")
    print("3. Search Homework")
    print("4. Modify Homework")
    print("5. Delete Homework")
    print("6. Exit")

def existHomework(Id):
    for hw in listHomeworks:
        if hw.Id == Id:
            return True
    return False

def addHomework():
    Id = input("Enter Homework ID: ")
    if existHomework(Id):
        print("Homework with this ID already exists.")
    else:
        description = input("Enter Description: ")
        priority = input("Enter Priority: ")
        status = input("Enter Status (1: Pending, 2: Completed): ")
        new_hw = Homework(Id, description, priority, status)
        listHomeworks.append(new_hw)
        print("Homework added successfully.")
        
def showHomeworks():
    if not listHomeworks:
        print("No homeworks to show.")
    else:
        for hw in listHomeworks:
            print(hw.showHomework())
            print("*" * 35)

def searchHomework():
    answer = input("Search by (1) ID or (2) Description? ")
    if answer == "1":
        found = False
        Id = input("Enter Homework ID: ")
        for hw in listHomeworks:
            if hw.Id == Id:
                print(hw.showHomework())
                print("*" * 35)
                found = True
                break
        if not found:
            print("Homework Id not found.")
    elif answer == "2":
        found = False
        description = input("Enter Description: ")
        for hw in listHomeworks:
            if hw.description == description:
                print(hw.showHomework())
                print("*" * 35)
                found = True
        if not found:
            print("No homework with that description found.")
    else:
        print("Invalid option.")
        
def modifyHomework():
    Id = input("Enter Homework ID to modify: ")
    for hw in listHomeworks:
        if hw.Id == Id:
            print("Current details:")
            print(hw.showHomework())
            hw.description = input("Enter new Description: ") or hw.description
            hw.priority = input("Enter new Priority: ") or hw.priority
            hw.status = input("Enter new Status (1: Pending, 2: Completed): ") or hw.status
            print("Homework updated successfully.")
            return
    print("Homework Id not found.")

def deleteHomework():
    id = input("Enter Homework ID to delete: ")
    if not existHomework(id):
           print("Homework with this ID does not exist.")
    else:
        for hk in listHomeworks:
            if hk.Id == id:
                listHomeworks.remove(hk)
                print("Homework deleted successfully.")
        
def main():
    while True:
        menu()
        choice = input("Select an option (1-6): ")
        if choice == "1":
            addHomework()
        elif choice == "2":
            showHomeworks()
        elif choice == "3":
            searchHomework()
        elif choice == "4":
            modifyHomework()
        elif choice == "5":
            deleteHomework()
        elif choice == "6":
            break
        else:
            print("invalid option")
            
if __name__ == "__main__":
    main()
        