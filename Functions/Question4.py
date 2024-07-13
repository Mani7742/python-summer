#WAF to find the factorial of n (n is a parameter)
# With loop
n = 5
fact =1
for i in range(1,n+1):
    fact = fact*i
print("Factorial of",n,"is",fact)
#With Function
def Calc_Fact(n):
    fact = 1
    for i in range(1,n+1):
        fact = fact*i
    print("Factorial of ",n,"is",fact)
Calc_Fact(4)  