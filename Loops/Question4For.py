# n = int(input("Enter a Number To calculate the factorial: "))
# fact = 1
# if n < 0:
#     print("Sorry, factorial does not exist for negative numbers")
# elif n == 0:
#     print("The factorial of 0 is 1")
# else:
#     for i in range(1,n+1):
#         fact = fact*i
#         print("The factorial of",n,"is",fact)

n = 5
fact = 1
for i in range(1,n+1):
    fact = fact*i
    print("The factorial of",fact)