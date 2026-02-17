print("*****Program Calculator*****")
print()

name = input("Please enter the name: ")
answer= "YES"
while answer.upper()=="YES":
    print()
    number1 = float(input("Please enter the number 1: "))
    number2 = float(input("please enter the numer 2: "))
    print("options: 1) Sum, 2) Substraction, 3) Multiplication, 4) Division")
    option = int(input("Please select a option:"))

    if option==1:
        result= str(number1+number2)
    elif option==2:
        result= str(number1-number2)
    elif option==3:
        result=str(number1*number2)
    elif option==4:
        result=str(number1/number2)
    else:
        result="Error - Invalid Option!!!"

    print(name+" the result of the operation is:",result)
    print()
    answer=input("Do you must continue: Yes or No?: ")
print()
print("*****End of The Program Calculator*****")

