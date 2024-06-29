# Create a program that determines the day of the week (e.g., Sunday, Monday) based on a user-provided 
# number (1 for Sunday, 2 for Monday, etc.) using if-else-if.

# Without using the functions

day_number = int(input("Enter a day Number (e.g. Sunday = 1, Monday = 2...) :"))
if day_number == 1:
    day_of_week = "Sunday"
elif day_number == 2:
    day_of_week = "Monday"
elif day_number ==3:
    day_of_week = "Tuesday"
elif day_number == 4:
    day_of_week = "Wednesday"
elif day_number == 5:
    day_of_week = "Thursday"
elif day_number == 6:
    day_of_week = "Friday"
elif day_number == 7:
    day_of_week = "Saturday"
else:
    day_of_week = "Invalid day number (Enter B/T 1 to 7)"

print(f"The day of week is: {day_of_week}")