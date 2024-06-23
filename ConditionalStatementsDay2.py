# -----------------------------------< if statement >------------------------------------------------
a = int(input("Enter the value:"))
if a%2==0:
    print("The number",a,"is even")

# -----------------------------------< if else statement >--------------------------------------------
b = int(input("Enter the value:"))
if b%2==0:
    print("The number",b,"is even")
else:
    print("The number",b,"is odd")

# -----------------------------------< elif statement >-----------------------------------------------
c = int(input("Enter the value:"))
if c>=60:
    print("You Got the First Division")
elif c>=45:
    print("You Got the Second Division")
elif c>=35:
    print("You Got the Third Division")
else:
    print("You are Fail")