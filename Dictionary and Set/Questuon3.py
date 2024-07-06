dict = {}
Math = eval(input("Enter the marks of 1st subject: "))
Physics = eval(input("Enter the marks of 2nd subject: "))
Computer = eval(input("Enter the marks of 3rd subject: "))
dict.update({"Math":Math})
dict.update({"Physics":Physics})
dict.update({"Computer":Computer})
print(dict)