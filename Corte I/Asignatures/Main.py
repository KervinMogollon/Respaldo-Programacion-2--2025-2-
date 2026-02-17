from Cl_Asignatures import asignatures

listAsignatures = [asignatures("Mathematics", 85), 
                   asignatures("History", 55), 
                   asignatures("Biology", 70),
                   asignatures("Art", 40),
                   asignatures("Physics", 90),
                   asignatures("Chemistry", 30),
                   asignatures("Literature", 75),
                   asignatures("Physical Education", 95),
                   asignatures("Music", 50),
                   asignatures("Geography", 65),
                   asignatures("Computer Science", 80)]

def menu():
    print("1. Add Asignature")
    print("2. Show Asignatures")
    print("3. Modify Asignature")
    print("4. Delete Asignature")
    print("5. Asignatures Approved")
    print("6. Asignatures Not Approved")
    print("7. Exit")
    
def asignatureExist(name):
    for asignature in listAsignatures:
        if asignature.name == name:
            return True
    return False

def correctCreditsInput():
    correctAnswer = "incorrect"
    while correctAnswer == "incorrect":
        credits = float(input("Enter the credits of the asignature: "))
        if credits < 0 or credits > 100:
            print("Invalid credits. Please enter a value between 0 and 100.")
        else:
            correctAnswer = "correct"
            return credits

def addAsignature():
    name = input("Enter the name of the asignature: ")
    
    if asignatureExist(name):
        print("Asignature already exists.")
    else:
        credits = correctCreditsInput()
        newAsignature = asignatures(name, credits)
        listAsignatures.append(newAsignature)
        print("Asignature added successfully.")
        
def showAsignatures():
    if not listAsignatures:
        print("No asignatures to show.")
    else:
        for asignature in listAsignatures:
            if asignature.status == "Active":
                print(asignature.ShowAsignature())
                print("--------------------")
            
def modifyAsignature():
    name = input("Enter the name of the asignature to modify: ")
    if not asignatureExist(name):
        print("Asignature does not exist.")
    else:
        for asignature in listAsignatures:
            if asignature.name == name:
                newName = input("Enter the new name of the asignature: ")
                if newName != name and asignatureExist(newName):
                    print("Another asignature with this name already exists.")
                else:
                    asignature.name = newName
                    asignature.credits = correctCreditsInput()
                    print("Asignature modified successfully.")
                break
            
def deleteAsignature():
    name = input("Enter the name of the asignature to delete: ")
    if not asignatureExist(name):
        print("Asignature does not exist.")
    else:
        for asignature in listAsignatures:
            if asignature.name == name:
                asignature.status = "Inactive"
                break
        print("Asignature deleted successfully.")

def showApprovedAsignatures():
    approved = [a for a in listAsignatures if a.credits >= 60]
    if not approved:
        print("No approved asignatures.")
    else:
        print("The Approved Asignatures:")
        for asignature in approved:
            print(f"{asignature.name}\n")
            print("--------------------")

def showNotApprovedAsignatures():
    not_approved = [a for a in listAsignatures if a.credits < 60]
    if not not_approved:
        print("No not approved asignatures.")
    else:
        print("The Not Approved Asignatures:")
        for asignature in not_approved:
            print(f"{asignature.name}\n")
            print("--------------------")

def main():
    while True:
        menu()
        choice = input("Select an option (1-7): ")
        if choice == "1":
            addAsignature()
        elif choice == "2":
            showAsignatures()
        elif choice == "3":
            modifyAsignature()
        elif choice == "4":
            deleteAsignature()
        elif choice == "5":
            showApprovedAsignatures()
        elif choice == "6":
            showNotApprovedAsignatures()
        elif choice == "7":
            print("Exiting the program.")
            break
        else:
            print("Invalid option. Please try again.")
            
if __name__ == "__main__":
    main()