operation = input("Enter the symbol of desired arithmetic operation: ")
first_number = int(input("Enter your first number: "))
second_number = int(input("Enter your second number: "))

if (operation == "+"):
    print(first_number + second_number)
elif (operation == "-"):
    print(first_number - second_number)
elif (operation == "*"):
    print(first_number * second_number)
elif (operation == "/"):
    print(first_number / second_number)
else:
    print("The symbol you have entered is invalid.")
