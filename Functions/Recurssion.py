n = int(input("enter a number:- "))
def Show(n):
    if (n == 0):
        return
    print(n)
    Show(n-1)#--> this will perform recurssion
Show(n)