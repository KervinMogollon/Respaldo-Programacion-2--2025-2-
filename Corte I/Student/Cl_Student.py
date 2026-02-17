class student:
    def __init__(self, id, name, age, university, average):
        self.id = id
        self.name = name
        self.age = age
        self.university = self.toCamelCase(university)
        self.average = average
        self.status = "A"
      
    def toCamelCase(self, texto):
        return texto[0].upper() + texto[1:].lower()
      
    def showStudent(self):
        print("\nStudent Information:\n")
        print(f"ID: {self.id}. \nName: {self.name}. \nAge: {self.age}. \nUniversity: {self.university}. \nAverage: {self.average}.")
        print("********************************\n")