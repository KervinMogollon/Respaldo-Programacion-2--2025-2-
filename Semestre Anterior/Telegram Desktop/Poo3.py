from product import Product

def LoadData(obj, listX):
    print()
    print("Please enter the Product Data:")
    print()
    obj.id = input("Id: ")
    obj.name = input("Name: ")
    obj.quantity = int(input("Quantity: "))
    obj.price = float(input("Price: "))
    listX.append(obj)
    print("Loaded Data!!!!")
    print()

def ShowList(listX):
    print()
    print("Printing My List Data:")
    print()
    for x in listX:
        print("---------------------------------------------")
        print(x.ShowData())
        print()
        print("---------------------------------------------")

def main():
    myListX=[]
    answer="yes"
    while answer=="yes":
        objProduct =  Product()
        print()
        LoadData(objProduct, myListX)
        answer=input("Would you like to include another worker?: ")
        print()
    print("--------------------------------------------------------")
    print()
    ShowList(myListX)

if __name__=='__main__':
    main()