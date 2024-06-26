# Create a program that determines whether a given year is a leap year or not using if-else statements. 


# With Function

def is_leap_year(year):
    if (year % 400 == 0) and (year % 100 ==0):
        return True
    elif (year % 4 == 0) and (year % 100 != 0):
        return True
    else:
        return False

year = int(input("Enter A Year: "))

if is_leap_year(year):
    print("It is a leap year")
else:
    print("It is not a leap year")



# Without Function

year = int(input("Enter A Year: "))
if (year % 400 == 0) and (year % 100 ==0):
        print(f"{year} is a leap year")
elif (year % 4 == 0) and (year % 100 != 0):
        print(f"{year} is a leap year")
else:
        print(f"{year} is not a leap year")

    