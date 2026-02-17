def menu():
    print("Menu")
    print("1 - sum")
    print("2 - subtract")
    print("3 - multiply")
    print("4 - divide")
    answer = int(input("Choose an option: "))
    return answer

print("*****Welcome to the program Calculator*****")
print()
name = input("Please, enter your name: ")

option = menu()

numbre1 = float(input("Enter the first number: "))
numbre2 = float(input("Enter the second number: "))

if option == 1:
    result = numbre1 + numbre2
elif option == 2:
    result = numbre1 - numbre2
elif option == 3:
    result = numbre1 * numbre2
elif option == 4:
    if numbre2 != 0:
        result = numbre1 / numbre2
    else:
        result = "Error: Division by zero"
else:
    result = "Invalid option"
    
print(name + ", the result is: " + str(result))

    
print("****End of the program Calculator****")