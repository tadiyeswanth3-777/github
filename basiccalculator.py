import math


def get_number(prompt):
    while True:
        value = input(prompt).strip()
        try:
            return float(value)
        except ValueError:
            print("Invalid number. Please enter a valid numeric value.")


def choose_operation():
    print("\nBasic and scientific calculator")
    print("Choose an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Power")
    print("6. Root")
    print("7. Modulo")
    print("8. Percentage")
    print("9. Factorial")
    print("10. Absolute value")
    print("11. Sine")
    print("12. Cosine")
    print("13. Tangent")
    print("14. Inverse sine")
    print("15. Inverse cosine")
    print("16. Inverse tangent")
    print("17. Natural logarithm (ln)")
    print("18. Base-10 logarithm")
    print("19. Exponent (e^x)")
    print("20. Square root")
    print("21. Cube")
    print("22. Cube root")
    print("23. Base-2 logarithm")
    print("24. Hypotenuse")
    print("25. Round")
    print("26. Exit")

    while True:
        choice = input("Enter the number of the operation: ").strip()
        if choice.isdigit() and 1 <= int(choice) <= 26:
            return int(choice)
        print("Invalid choice. Please enter a number between 1 and 20.")


def add():
    print("Addition")
    a = get_number("Enter the first number: ")
    b = get_number("Enter the second number: ")
    print("Result:", a + b)


def subtract():
    print("Subtraction")
    a = get_number("Enter the first number: ")
    b = get_number("Enter the second number: ")
    print("Result:", a - b)


def multiply():
    print("Multiplication")
    a = get_number("Enter the first number: ")
    b = get_number("Enter the second number: ")
    print("Result:", a * b)


def divide():
    print("Division")
    a = get_number("Enter the dividend: ")
    b = get_number("Enter the divisor: ")
    if b == 0:
        print("Cannot divide by zero.")
    else:
        print("Result:", a / b)


def power():
    print("Power")
    base = get_number("Enter the base: ")
    exponent = get_number("Enter the exponent: ")
    print("Result:", base ** exponent)


def root():
    print("Root")
    value = get_number("Enter the value: ")
    degree = get_number("Enter the root degree (2 for square root): ")
    if degree == 0:
        print("Root degree cannot be zero.")
        return

    if value < 0:
        if degree != int(degree) or int(degree) % 2 == 0:
            print("Cannot compute an even or non-integer root of a negative number using real numbers.")
            return
        degree = int(degree)
        result = -((-value) ** (1 / degree))
    else:
        result = value ** (1 / degree)

    print("Result:", result)


def modulo():
    print("Modulo")
    a = get_number("Enter the first number: ")
    b = get_number("Enter the second number: ")
    if b == 0:
        print("Cannot use modulo with divisor zero.")
    else:
        print("Result:", a % b)


def percentage():
    print("Percentage")
    value = get_number("Enter the value: ")
    total = get_number("Enter the total or base value: ")
    if total == 0:
        print("Cannot calculate percentage with a total of zero.")
    else:
        print("Result:", (value / total) * 100, "%")


def factorial():
    print("Factorial")
    n = get_number("Enter a non-negative integer: ")
    if n < 0 or n != int(n):
        print("Factorial requires a non-negative integer.")
    else:
        print("Result:", math.factorial(int(n)))


def absolute_value():
    print("Absolute value")
    a = get_number("Enter a number: ")
    print("Result:", abs(a))


def sine():
    print("Sine")
    angle = get_number("Enter the angle in degrees: ")
    print("Result:", math.sin(math.radians(angle)))


def cosine():
    print("Cosine")
    angle = get_number("Enter the angle in degrees: ")
    print("Result:", math.cos(math.radians(angle)))


def tangent():
    print("Tangent")
    angle = get_number("Enter the angle in degrees: ")
    radians = math.radians(angle)
    cos_value = math.cos(radians)
    if math.isclose(cos_value, 0.0, abs_tol=1e-12):
        print("Tangent is undefined at this angle.")
    else:
        print("Result:", math.tan(radians))


def inverse_sine():
    print("Inverse sine")
    value = get_number("Enter a value between -1 and 1: ")
    if -1 <= value <= 1:
        print("Result:", math.degrees(math.asin(value)))
    else:
        print("Value must be between -1 and 1.")


def inverse_cosine():
    print("Inverse cosine")
    value = get_number("Enter a value between -1 and 1: ")
    if -1 <= value <= 1:
        print("Result:", math.degrees(math.acos(value)))
    else:
        print("Value must be between -1 and 1.")


def inverse_tangent():
    print("Inverse tangent")
    value = get_number("Enter a number: ")
    print("Result:", math.degrees(math.atan(value)))


def natural_log():
    print("Natural logarithm")
    value = get_number("Enter a positive number: ")
    if value <= 0:
        print("Natural log requires a positive number.")
    else:
        print("Result:", math.log(value))


def log_base_10():
    print("Base-10 logarithm")
    value = get_number("Enter a positive number: ")
    if value <= 0:
        print("Base-10 log requires a positive number.")
    else:
        print("Result:", math.log10(value))


def log_base_2():
    print("Base-2 logarithm")
    value = get_number("Enter a positive number: ")
    if value <= 0:
        print("Base-2 log requires a positive number.")
    else:
        print("Result:", math.log2(value))


def square_root():
    print("Square root")
    value = get_number("Enter a non-negative number: ")
    if value < 0:
        print("Square root requires a non-negative number.")
    else:
        print("Result:", math.sqrt(value))


def cube():
    print("Cube")
    value = get_number("Enter a number: ")
    print("Result:", value ** 3)


def cube_root():
    print("Cube root")
    value = get_number("Enter a number: ")
    result = math.copysign(abs(value) ** (1 / 3), value)
    print("Result:", result)


def hypotenuse():
    print("Hypotenuse")
    a = get_number("Enter side a: ")
    b = get_number("Enter side b: ")
    print("Result:", math.hypot(a, b))


def round_number():
    print("Round")
    value = get_number("Enter a number: ")
    digits = get_number("Enter number of decimal places (0 for integer): ")
    if digits != int(digits):
        print("Number of decimal places must be an integer.")
    else:
        print("Result:", round(value, int(digits)))


def exponent():
    print("Exponent")
    value = get_number("Enter a number: ")
    print("Result:", math.exp(value))


def main():
    while True:
        operation = choose_operation()
        if operation == 1:
            add()
        elif operation == 2:
            subtract()
        elif operation == 3:
            multiply()
        elif operation == 4:
            divide()
        elif operation == 5:
            power()
        elif operation == 6:
            root()
        elif operation == 7:
            modulo()
        elif operation == 8:
            percentage()
        elif operation == 9:
            factorial()
        elif operation == 10:
            absolute_value()
        elif operation == 11:
            sine()
        elif operation == 12:
            cosine()
        elif operation == 13:
            tangent()
        elif operation == 14:
            inverse_sine()
        elif operation == 15:
            inverse_cosine()
        elif operation == 16:
            inverse_tangent()
        elif operation == 17:
            natural_log()
        elif operation == 18:
            log_base_10()
        elif operation == 19:
            exponent()
        elif operation == 20:
            square_root()
        elif operation == 21:
            cube()
        elif operation == 22:
            cube_root()
        elif operation == 23:
            log_base_2()
        elif operation == 24:
            hypotenuse()
        elif operation == 25:
            round_number()
        else:
            print("Goodbye!")
            break

        print("\nOperation completed.")


if __name__ == "__main__":
    main()
