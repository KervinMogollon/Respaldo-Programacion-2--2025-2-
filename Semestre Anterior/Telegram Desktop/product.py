class Product:

    def __init__(self):
        self.id = ""
        self.name=""
        self.quantity=0
        self.price=0.0
        self.statusW = 'A'

    def ShowData(self): #ShowData es un metodo usado para mostrar los datos del producto
        return f'Product Data:\n Id: {self.id}\n Name: {self.name}\n Quantity: {self.quantity}\n Price: {self.price}\n'