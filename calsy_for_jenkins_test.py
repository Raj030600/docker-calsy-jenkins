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


# Automated tests for Jenkins
def run_tests():
    print("\n===== Running Calculator Tests =====")

    test_cases = [
        (2, "+", 2, 4),
        (10, "-", 4, 6),
        (5, "*", 3, 15),
        (10, "/", 2, 5),
        (10, "%", 3, 6),
        (2, "**", 3, 8)
    ]

    passed = 0
    failed = 0

    for num1, operator, num2, expected in test_cases:

        if operator == "+":
            result = num1 + num2
        elif operator == "-":
            result = num1 - num2
        elif operator == "*":
            result = num1 * num2
        elif operator == "/":
            result = num1 / num2
        elif operator == "%":
            result = num1 % num2
        elif operator == "**":
            result = num1 ** num2

        if result == expected:
            print(f"PASS: {num1} {operator} {num2} = {result}")
            passed += 1
        else:
            print(
                f"FAIL: {num1} {operator} {num2} "
                f"= {result}, expected {expected}"
            )
            failed += 1

    print("\n===== Test Summary =====")
    print(f"Passed: {passed}")
    print(f"Failed: {failed}")

    if failed == 0:
        print("All tests passed!")
        return 0
    else:
        print("Some tests failed!")
        return 1


# Main Menu / Jenkins Test Mode

import sys

if len(sys.argv) > 1 and sys.argv[1] == "--test":
    exit_code = run_tests()
    sys.exit(exit_code)

while True:

    print("\n==============================")
    print("      PYTHON CALCULATOR")
    print("==============================")
    print("1. New Calculation")
    print("2. Exit")
    print("3. Run Tests")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        calculate()

    elif choice == "2":
        print("\nThank you for using the calculator!")
        break

    elif choice == "3":
        run_tests()

    else:
        print("\nInvalid choice! Please enter 1, 2 or 3.")