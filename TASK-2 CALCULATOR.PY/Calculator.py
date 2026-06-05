# Calculator Application with History

History = []

while True:
    print("\n===== Calculator =====")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. View History")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    # Exit
    if choice == '6':
        print("Calculator Closed.")
        break

    # View History
    elif choice == '5':
        print("\n===== Calculation History =====")

        if History:
            for i, (num1, num2, operation, result) in enumerate(History, start=1):
                print(f"{i}. {num1} {operation} {num2} = {result}")
        else:
            print("No calculations performed yet.")

    # Calculator Operations
    elif choice in ['1', '2', '3', '4']:
        try:
            n1 = float(input("Enter First Number: "))
            n2 = float(input("Enter Second Number: "))

            if choice == '1':
                result = n1 + n2
                print("Result of Addition =", result)
                History.append((n1, n2, "+", result))

            elif choice == '2':
                result = n1 - n2
                print("Result of Subtraction =", result)
                History.append((n1, n2, "-", result))

            elif choice == '3':
                result = n1 * n2
                print("Result of Multiplication =", result)
                History.append((n1, n2, "*", result))

            elif choice == '4':
                if n2 == 0:
                    print("Error! Division by zero is not allowed.")
                else:
                    result = n1 / n2
                    print("Result of Division =", result)
                    History.append((n1, n2, "/", result))

        except ValueError:
            print("Please enter valid numbers.")

    else:
        print("Invalid Choice! Please select between 1 and 6.")