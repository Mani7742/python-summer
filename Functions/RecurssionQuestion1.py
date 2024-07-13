n = int(input("Enter a Number to Calculate the Factorial:- "))
def Calc_Fact(n):
    if (n == 0 or n == 1):
        return 1
    else:
        return n * Calc_Fact(n-1)
print(Calc_Fact(n)) 