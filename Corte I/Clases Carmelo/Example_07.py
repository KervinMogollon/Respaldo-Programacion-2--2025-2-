class student:
    def __init__(self):
        self.name = ""
        self.lastName = ""
        self.age = 0

    def showData(self):
        print()
        print("Student Data")
        """print("Name:", self.name)
        print("Last Name:", self.last_name)
        print("Age:", self.age)"""
        print(f"Name: {self.name}\nLast Name: {self.lastName}\nAge: {self.age}")
        print()
        
def main():
    print("Welcome to the Student Registration Program")
    print()
    objStudent = student()
    answer = "Yes"
    while answer == "Yes":
        print("Please enter the student data")
        objStudent.name = input("Name: ")
        objStudent.lastName = input("Last Name: ")
        objStudent.age = int(input("Age: "))
        print()
        objStudent.showData()
        print()
        answer = input("Do you want to enter another student? (Yes/No): ")
    print("End of the Program")

if __name__ == "__main__":
    main()