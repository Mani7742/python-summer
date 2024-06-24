
#Create a program that converts a given number of minutes into hours and minutes.

total_minutues = int(input("Enter the number of minutes:"))

hours = total_minutues //60
minutes = total_minutues % 60
print(f"{total_minutues} minutes is equal to {hours} hours and {minutes} minutes")