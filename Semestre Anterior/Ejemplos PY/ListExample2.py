print("***************************************")
listX = []
print("Welcome to the program List")
print()
print("Enter an item or * to finish")
answer = "Yes"
while answer!="*":
    element = input("Please include the item to be included in the list:")
    answer = element
    if element !="*":
        listX.append(element)
        print("The element has been included!!!")
print("List Elements:")
print(listX)
print("***************************************")