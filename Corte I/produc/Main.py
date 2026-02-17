#Ejemplo de CRUD de Productos
#Clase principal
from Products import Products

productList = [] #Empty List

def menu():
    print("Menu")
    print("")
    print("1 - Add Product")
    print("2 - Search Product")
    print("3 - Modify Product")
    print("4 - Delete Product")
    print("5 - Exit")
    print("")
    option = int(input("Please select a choice: "))
    print("")
    return option

def search():
    finded = False
    idtoSearch = input("Please enter the product id: ")
    for item in productList:
        if item.id==idtoSearch:
            item.showData()
            finded=True
            break
    if not finded:
        print("")
        print("Error!!! The Id not Exist!!!")
        print("")

def searchinList(fi):
    finded = False
    idtoSearch = fi
    for item in productList:
        if item.id==idtoSearch:
            item.showData()
            finded=True
            break
    return finded

def readProductData():
    print("Product Data:")
    print("")
    idP = input("Enter the Id: ")
    name = input("Enter the name: ")
    price = float(input("Enter the price: "))
    quantity = int(input("Enter the quantity: "))
    if not searchinList(idP):
        objProduct = Products(idP, name, price,quantity)
        productList.append(objProduct)
        objProduct.showData()
        print("")
        print("Data Loaded!!!!")
    else:
        print("")
        print("Data already exist!!!")
        print("")
    print("")
    
# def modify():
#     print("Modify Product Data:")
#     print("")
#     idP = input("Enter the Id : ")
#     for item in productList:
#         if item.id==idP:
#             item.showData()
#             print("")
#             productList.remove(item)
#             name = input("Enter the name: ")
#             price = float(input("Enter the price: "))
#             quantity = int(input("Enter the quantity: "))
#             objProduct = Products(idP, name, price,quantity)
#             productList.append(objProduct)
#             print("")
#             objProduct.showData()
#             print("")
#             print("Data Modifided!!!!")
#             finded=True
#             break
#     if not finded:
#         print("")
#         print("Error!!! The Id not Exist!!!")
#         print("")
 
# def showProducts():
#     number = 1
#     for item in productList:
#         print("Product Number #"+str(number))
#         item.showData()
#         number+=1
        
# def delete():
#     print("Delete Product Data:")
#     print("")
#     idP = input("Enter the Id : ")
#     for item in productList:
#         if item.id==idP:
#             item.showData()
#             print("")
#             productList.remove(item)
#             print("")
#             print("Data Deleted!!!!")
#             finded=True
#             break
#     if not finded:
#         print("")
#         print("Error!!! The Id not Exist!!!")
#         print("")
    
def main():
    answer = "yes"
    while answer=="yes":
        op = menu()
        if op==1: #Add Product
            readProductData()
        elif op==2: #Search Product
            search()                
        elif op==3: #Modify Product
            pass
        elif op==4: #Delete Product
            pass
        elif op==5: #Exit
            print("End of the Program!!!")
            break
        else:
            print("Error! Option not valid!")
            print("")
        answer = input("Do you wish continue? yes or no: ").lower

if __name__=="__main__":
    main()
