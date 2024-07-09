#Create a Python program that calculates the factorial of a given positive integer using a while loop. 
number = int(input("Enter a Number:-"))
if number < 0:
    print("Sorry, factorial does not exist for negative numbers")
else:
    factorial = 1
    i = 1
    while (i<=number):
        factorial = factorial * i
        i = i + 1
    print("The factorial of",number,"is",factorial)
        