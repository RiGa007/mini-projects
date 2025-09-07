operator = input("Enter the operator (+, -, *, /): ")
num1 = float(input("Enter the number: "))
num2 = float(input("Enter the number: "))


if operator == "+":
    result = num1 + num2
    print(result)
elif operator == "-":
    result = num1 - num2 
    print(result)
elif operator == "*":
    result = num1 * num2
    print(result)
elif operator == "/":
    result = num1 / num2
    print(round(result, 3))
else:
    print(f"the {operator} is not a valid operator")


