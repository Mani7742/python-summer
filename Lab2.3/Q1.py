#Write a C++ program that takes a number from 1 to 7 and prints the corresponding day of the week using a 
#switch statement.

# Python does not have the switch case however you can achieve the same things with other methods

day_number = int(input("Enter a Number 1 to 7:"))

switcher = {
    1: "Monday",
    2: "Tuesday",
    3: "Wednesday",
    4: "Thursday",
    5: "Friday",
    6: "Saturday",
    7: "Sunday"
}

day_of_Week = switcher.get(day_number, "invalid Day Number")
print(day_of_Week)