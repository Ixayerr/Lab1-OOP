import math


def task_integer10():
    try:
        number = int(input("Enter a three-digit number: "))
        if number < 100 or number > 999:
            raise ValueError("The number must be three digits!")
        last_digit = number % 10
        middle_digit = (number // 10) % 10
        print(f"Last digit: {last_digit}, Middle digit: {middle_digit}")
    except ValueError as e:
        print(e)
        input("Press enter to exit...")


def task_math_expression():
    try:
        x = float(input("Enter x (x ≠ 0): "))
        if x == 0:
            raise ValueError("x cannot be zero!")
        numerator = 5 * (3 ** x) * math.sqrt(math.exp(x)) * abs(math.sin(math.radians(27) + x))
        denominator = math.log(2, 5) * abs(x)
        y = numerator / denominator
        print(f"y = {y}")
    except ValueError as e:
        print(f"Error: {e}")
        input("Press enter to exit...")


def task_boolean12():
    try:
        A = int(input("Enter A: "))
        B = int(input("Enter B: "))
        C = int(input("Enter C: "))
        result = A > 0 and B > 0 and C > 0
        print(f"All numbers are positive: {result}")
    except ValueError:
        print("All inputs must be integers.")
        input("Press enter to exit...")


def main():
    print("Choose a task to run:")
    print("1. Integer Task (Task 1)")
    print("2. Mathematical Expression Task (Task 2)")
    print("3. Boolean Task (Task 3)")

    choice = input("Enter your choice (1, 2, or 3): ")

    if choice == '1':
        task_integer10()
    elif choice == '2':
        task_math_expression()
    elif choice == '3':
        task_boolean12()
    else:
        print("Invalid choice.")


if __name__ == "__main__":
    main()
