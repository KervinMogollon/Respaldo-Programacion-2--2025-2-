class Contact:
    def __init__(self, id, name, phoneNumber, email):
        self.id = id
        self.name = name
        self.phoneNumber = phoneNumber
        self.email = email
        
    def showContact(self):
        return f"ID: {self.id}, Name: {self.name}, Phone: {self.phoneNumber}, Email: {self.email}"
        