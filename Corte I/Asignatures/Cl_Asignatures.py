class asignatures:
    def __init__(self, name: str, credits: float):
        self.name = name
        self.credits = credits
        self.status = "Active"

    def ShowAsignature(self):
        return f"Asignature: {self.name} \nCredits: {self.credits}"