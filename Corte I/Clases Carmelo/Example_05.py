class student:
    def __init__(self):
        self.name = ""
        self.last_name = ""
        self.age = 0

    def showData(self):
        print()
        print("Student Data")
        print("Name:", self.name)
        print("Last Name:", self.last_name)
        print("Age:", self.age)
        print()
        
def main():
    print("Welcome to the Student Registration Program")
    print()
    objStudent = student()
    print("Please enter the student data")
    objStudent.name = input("Name: ")
    objStudent.last_name = input("Last Name: ")
    objStudent.age = int(input("Age: "))
    print()
    objStudent.showData()
    
    print("End of the Program")

if __name__ == "__main__":
    main()