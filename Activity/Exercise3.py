def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Cannot divide by zero"
    return x/ y


while True:
    print("Calculator Menu:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    option = input("Enter your choice (1-5): ")
    x=int(input("Enter the first digit: "))
    y=int(input("Enter the second digit: "))

    if option == '5':
        print("Exiting calculator. Goodbye!")
        break

    elif option == "1":
        print("Answer:", add(x,y))
    elif option == "2":
        print("Answer:", subtract(x,y))
    elif option =="3":
        print("Answer: ", multiply(x,y))
    elif option =="4":
        print("Answer: ", divide(x,y))
    else:
        print("No operations are carried out!")
        break