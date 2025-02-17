def math(operation, a,b):
    if operation == "1":
        return a + b
    elif operation == "2":
        return a - b
    elif operation == "3":
        return a * b
    elif operation == "4":
        return a / b
    else:
        return "Invalid operation"


def main():
    print("operations")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    inputoperation, inputa, inputb = input("Enter operation, a, b: ").split()
    mathResult = math(inputoperation, int(inputa), int(inputb))
    print(mathResult)

if __name__ == "__main__":
    main()