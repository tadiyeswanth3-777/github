num1 = int(input("give 1st number: "))
num2 = int(input("give 2nd number: "))
operator = input("give operator (+, -, *, /): ").strip()

if operator == "+":
    print(f"Addition of two numbers is {num1 + num2}")
elif operator == "-":
    print(f"Subtraction of two numbers is {num1 - num2}")
elif operator == "*":
    print(f"Multiplication of two numbers is {num1 * num2}")
elif operator == "/":
    if num2 != 0:
        print(f"Division of two numbers is {num1 / num2}")
    else:
        print("Cannot divide by zero")
else:
    print("Incorrect operator")

