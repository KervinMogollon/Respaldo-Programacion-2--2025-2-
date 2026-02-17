class Products:

    def __init__(self):
        self.product_id : str
        self.product_name :str
        self.description : str
        self.price : float
        self.stock : int
        self.category : str
        self.status = 'A'
    
    def showData(self):
        print("Product Data:")
        print()
        print(f'Id: {self.product_id}')
        print(f'Name: {self.product_name}')
        print(f'Description: {self.description}')
        print(f'Price: str({self.price})')
        print(f'Stock: str({self.stock})')
        print(f'Category: {self.category}')
        print()