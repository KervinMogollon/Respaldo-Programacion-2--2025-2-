from Cl_Student import student

#Let's add test data to this list
listStudents = [(student("01", "Alice", 20, "Harvard", 17.5)),
                (student("02", "Bob", 22, "Cambridge", 15.7)),
                (student("03", "Charlie", 21, "Harvard", 19.8)),
                (student("04", "David", 23, "Stanford", 14.2)),
                (student("05", "Eva", 20, "Cambridge", 20.0)),
                (student("06", "Frank", 24, "Harvard", 16.9)),
                (student("07", "Grace", 22, "Stanford", 18.6)),
                (student("08", "Hannah", 21, "Cambridge", 14.1)),
                (student("09", "Ian", 23, "Harvard", 11.4)),
                (student("10", "Jane", 20, "Mit", 19.7))]

def menu():
    print("Menu:")
    print("1. Add Student")
    print("2. Search Students")
    print("3. Delete Students")
    print("4. Modify Students")
    print("5. Show Students")
    print("6. Show Students by University")
    print("7. Show Students who approved (average >= 14)")
    print("8. Show Students who failed (average < 14)")
    print("9. Show students in the note range of your selection note")
    print("10. Exit")
    choice = input("Enter your choice (1-10): ")
    return choice

def studentExists(id):
    for stu in listStudents:
        if stu.id == id:
            return False
    return True

def addStudent():
    print("Add Student:")
    id = input("Enter ID: ")
    if studentExists(id) == True:
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        university = input("Enter University: ")
        average = float(input("Enter Average: "))
        new_student = student(id, name, age, university, average)
        listStudents.append(new_student)
        print("Student added successfully.")
    else:
        print("Failed to add student. ID already exists.")
    print("")
    
def searchStudent():
    print("Search Student:")
    id = input("Enter ID to search: ")
    for student in listStudents:
        if student.id == id:
            student.showStudent()
        else:
            print("Student not found.")
    print("")
    
def deleteStudent():
    print("Delete Student:")
    id = input("Enter ID to delete: ")
    for student in listStudents:
        if student.id == id:
            listStudents.remove(student)
            print("Student deleted successfully.")
    print("")
    
def modifyStudent():
    print("Modify Student:")
    id = input("Enter ID to modify: ")
    for student in listStudents:
        if student.id == id:
            print("Enter new data:")
            student.name = input("Enter Name: ")
            student.age = int(input("Enter Age: "))
            student.university = input("Enter University: ")
            student.average = float(input("Enter Average: "))
            print("Student modified successfully.")
            break
        else:
            print("Student not found.")
    print("")
    
def showStudents():
    print("All Students:")
    for student in listStudents:
        student.showStudent()
    print("")
    
def toCamelCase(texto):
    return texto[0].upper() + texto[1:].lower()
    
def showStudentsByUniversity():
    print("Show Students by University or your selection:")
    university = toCamelCase(input("Enter University to search students: "))
    print(f"\nStudents from {university}:")
    uniStudents = [student for student in listStudents if student.university == university]
    if uniStudents:
        for student in uniStudents:
            student.showStudent()
    else:
        print("\nNo students found for this university.")
    print("")
    
def studentsApproved():
    print("Students who approved (average >= 14):")
    approvedStudents = [student for student in listStudents if student.average >= 14]
    if approvedStudents:
        for student in approvedStudents:
            student.showStudent()
    else:
        print("No students have approved.")
    print("")
    
def studentsFailed():
    print("Students who failed (average < 14):")
    failedStudents = [student for student in listStudents if student.average < 14]
    if failedStudents:
        for student in failedStudents:
            student.showStudent()
    else:
        print("No students have failed.")
    print("")
    
def studentsInRange(min_note, max_note):
    print(f"Students with average between {min_note} and {max_note}:")
    rangeStudents = [student for student in listStudents if min_note <= student.average <= max_note]
    if rangeStudents:
        for student in rangeStudents:
            student.showStudent()
    else:
        print("No students found in this range.")
    print("")
    
def main():
    answer = "yes"
    while answer == "yes":
        choice = menu()
        if choice == "1":
            addStudent()
        elif choice == "2":
            searchStudent()
        elif choice == "3":
            deleteStudent()
        elif choice == "4":
            modifyStudent()
        elif choice == "5":
            showStudents()
        elif choice == "6":
            showStudentsByUniversity()
        elif choice == "7":
            studentsApproved()
        elif choice == "8":
            studentsFailed()  
        elif choice == "9":
            min_note = float(input("Enter minimum note: "))
            max_note = float(input("Enter maximum note: "))
            studentsInRange(min_note, max_note)
        elif choice == "10":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")
        answer = input("Do you want to continue? (yes/no): ").lower()

if __name__ == "__main__":
    main()