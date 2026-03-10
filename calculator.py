num1 = float(input("Enter first number: "))
num2 = float(input("enter second number:"))
operator = input("enter operator(+,-,*,/):")
if operator == "+":
    result = num1+ num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error: Division by zero is not allowed."
else:
    result = "Error: Invalid operator."
print(result)
    