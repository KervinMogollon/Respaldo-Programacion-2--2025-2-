class vendedor:
    def __init__(self):
        self.vendId : str
        self.nombreCompleto : str
        self.ciudad : str
        self.comision : float
        self.status = 'A'

    def showData(self):
        print("Data del Vendedor")
        print("-" * 30)
        print(f"ID: {self.vendId}")
        print(f"Nombre: {self.nombreCompleto}")
        print(f"Ciudad: {self.ciudad}")
        print(f"Comisión: {self.comision}")
        print("-" * 30)
