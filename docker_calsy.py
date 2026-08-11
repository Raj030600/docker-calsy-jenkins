# Simple Calculator (Continuous)

def calculate():
    print("\n===== Python Calculator =====")

    try:
        num1 = float(input("Enter first number: "))
        operator = input("Enter operator (+, -, *, /, %, **): ")
        num2 = float(input("Enter second number: "))

        if operator == "+":
            result = num1 + num2

        elif operator == "-":
            result = num1 - num2

        elif operator == "*":
            result = num1 * num2

        elif operator == "/":
            if num2 != 0:
                result = num1 / num2
            else:
                result = "Error! Division by zero."

        elif operator == "%":
            if num2 != 0:
                result = num1 % num2
            else:
                result = "Error! Division by zero."

        elif operator == "**":
            result = num1 ** num2

        else:
            result = "Invalid operator!"

        print("\n===== Result =====")
        print(f"{num1} {operator} {num2} = {result}")

    except ValueError:
        print("\nInvalid input! Please enter numbers only.")


# Main Menu
while True:

    print("\n==============================")
    print("      PYTHON CALCULATOR")
    print("==============================")
    print("1. New Calculation")
    print("2. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        calculate()

    elif choice == "2":
        print("\nThank you for using the calculator!")
        break

    else:
        print("\nInvalid choice! Please enter 1 or 2.")