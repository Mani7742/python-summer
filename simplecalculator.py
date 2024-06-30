num1 = eval(input("Enter the First Number: "))
num2 = eval(input("Enter the Second Number: "))
opr = (input("Enter the Operator(+,-,*,/)"))
if opr == "+":
    print(num1 + num2)
elif opr == "-":
    print(num1 - num2)
elif opr == "*":
    print(num1 * num2)
elif opr == "/":
    print(num1 / num2)
else:
    print("Invalid Operator")