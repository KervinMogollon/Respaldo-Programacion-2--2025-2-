import datetime as dt


class Student:
    def __init__(self):
        self.StudCi : str
        self.StudName : str
        self.StudAddress : str
        self.StudPhone : str
        self.StudBirthDate : dt.datetime
        self.StudRegisteredDate : dt.datetime
        self.StudCareer : str
        self.status = 'A'
        
    def showData(self):
        if self.status != 'A':
            print("-" * 30)
            print(f"CI: {self.StudCi}")
            print(f"Nombre: {self.StudName}")
            print(f"Dirección: {self.StudAddress}")
            print(f"Teléfono: {self.StudPhone}")
            print(f"Fecha de Nacimiento: {self.StudBirthDate}")
            print(f"Fecha de Registro: {self.StudRegisteredDate}")
            print(f"Carrera: {self.StudCareer}")
            print("-" * 30)
        