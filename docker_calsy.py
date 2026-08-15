# Simple Calculator (Continuous)
import sys

if "--test" in sys.argv:
    print("===== Docker Calculator Test Mode =====")

    tests = [
        (2, "+", 2, 4),
        (10, "-", 4, 6),
        (5, "*", 3, 15),
        (10, "/", 2, 5),
        (10, "%", 3, 1),
        (2, "**", 3, 8),
    ]

    failed = 0

    for a, operator, b, expected in tests:

        if operator == "+":
            result = a + b
        elif operator == "-":
            result = a - b
        elif operator == "*":
            result = a * b
        elif operator == "/":
            result = a / b
        elif operator == "%":
            result = a % b
        elif operator == "**":
            result = a ** b

        if result == expected:
            print(f"PASS: {a} {operator} {b} = {result}")
        else:
            print(f"FAIL: {a} {operator} {b} = {result}, expected {expected}")
            failed += 1

    print()
    print(f"Passed: {len(tests) - failed}")
    print(f"Failed: {failed}")

    if failed == 0:
        print("All Docker tests passed!")
        sys.exit(0)
    else:
        print("Docker tests failed!")
        sys.exit(1)
        
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