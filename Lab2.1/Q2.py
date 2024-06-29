
#develop a program that takes three numbers as input and prints the largest of the three numbers using if_else.

a = int(input("Enter First Number:"))
b = int(input("Enter Second Number:"))
c = int(input("Enter Third Number:"))

if a>b and a>c:
    print("The Largest Number is",a)
elif b>a and b>c:
    print("The Largest Number is",b)
else:
    print("The Largest Number is",c)    