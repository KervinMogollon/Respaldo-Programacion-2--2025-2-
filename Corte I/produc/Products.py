class Products:
    def __init__(self, idP, name, price, quantity):
        self.id = idP
        self.name=name
        self.price = price
        self.quantity = quantity

    def showData(self):
        print("")
        print("*********Product Data*********")
        print("")
        print(f"Id: {self.id} \n Name: {self.name}\n Price: {str(self.price)}\n Quantity: {str(self.quantity)}")
        print("")
        print("*******************************")
        print("")