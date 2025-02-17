def add():
    """Addition of two numbers"""


def subtract():
    """Subtraction of two numbers"""


def devide():
    """Devide two numbers"""


def multiply():
    """Multiply two numbers"""


def operationsSelection():
    """Select the operation to perform and provide inputs
    The function will call the respective function based on the operation selected and pass the inputs to the function.
    """
    print("Select operation and provide two numbers separated by space.")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Devide")
    print("4. Multiply")

    operation, a, b = input(
        "Enter the operation and two numbers separated by space: "
    ).split()
    a = float(a)
    b = float(b)

    if operation == "1":
        add()
    elif operation == "2":
        subtract()
    elif operation == "3":
        devide()
    elif operation == "4":
        multiply()
    else:
        print("Invalid operation selected.")


def main():
    """Main function to run the program"""
    operationsSelection()


if __name__ == "__main__":
    main()
