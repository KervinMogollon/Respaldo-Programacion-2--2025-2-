class Homework:
    def __init__(self, Id, description, priority, status):
        self.Id = Id
        self.description = description
        self.priority = priority
        self.status = status

    def statusName(self):
        if self.status == "1":
            return "Pending"
        elif self.status == "2":
            return "Completed"
        else:
            return "Unknown"

    def showHomework(self):
        return f"ID: {self.Id}\nDescription: {self.description}\nPriority: {self.priority}\nStatus: {self.statusName()}"