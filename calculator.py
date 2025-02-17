def add(a,b):
    """Addition of two numbers"""
    return a+b

def subtract(a,b):
    """Subtraction of two numbers"""
    return a-b

def divide(a,b):
    """Divide two numbers"""
    return a/b

def multiply(a,b):
    """Multiply two numbers"""
    return a*b

def operationselection():
    """Select the operation to perform and provide inputs
    The function will call the respective function based on the operation selected and pass the inputs to the function.
    """
    print("Select operation and provide two numbers separated by space.")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Divide")
    print("4. Multiply")

    operation, a, b = input("Enter the operation and two numbers separated by space: ").split()
    a = float(a)
    b = float(b)

    if operation == "1":
        print(add(a,b))
    elif operation == "2":
        print(subtract(a,b))
    elif operation == "3":
        print(divide(a,b))
    elif operation == "4":
        print(multiply(a,b))
    else:
        print("Invalid operation selected.")


def main():
    """Main function to run the program"""
    operationselection()


if __name__ == "__main__":
    main()
