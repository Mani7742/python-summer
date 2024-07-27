Email = input("Enter Your Email: ")
i = 0 
j = 0
k = 0
if len(Email) >= 6:
    if Email[0].isalpha():
        if ("@" in Email) and (Email.count("@")==1):
            if (Email[-4] == ".") ^ (Email[-3]=="."):
                for i in Email:
                    if i == i.isspace():
                        k = 1
                    elif i.isalpha():
                        if i == i.upper():
                            j = 1    
                    elif i.isdigit():
                        continue
                    elif i == "_" or i == "." or i == "@":
                        continue
                    else:
                        k=1
                if k==1 or j==1 or k==1 :
                    print("Wrong Email 5")
                else:
                    print("Email is valid")
            else:
                print("Wrong Email 4")
        else:
            print("Wrong Email 3")
    else:
        print("Wrong Email 2")
else:
    print("Wrong Email 1")