def main():

    print("***************************************")
    listX = []
    print("Welcome to the program List")
    print()
    oper=0
    while oper!=4:
        oper = int(input("Operations: 1) Add, 2) Remove, 3)View List, 4)Exit: "))
        match oper:
            case 1:
                element = input("Please include the item to be included in the list:")
                listX.append(element)
                print("The element has been included!!!")
            case 2:
                print()
                element = input("Please enter the element to be remove of the list:")
                listX.remove(element)
                print("The element has been removed!!")
            case 3:
                ViewList(listX)
            case 4:
                break
            case _:
                print("Invalid Option!!!")

def ViewList(listW):
    print("Elements of the List:")
    for x in listW:
        print(x)
        print()
    print()
    print("End Of Elemts!!!")

main()