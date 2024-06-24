

#Create a program that converts temperature from Fahrenheit to Celsius and vice versa. 

print("1. Convert Fahrnheit to Celsius")
print("2. Convert Celsius to Fahrnheit")


choice = input("Enter Your Choice(1 or 2)")

if choice == '1':
    fahrenheit = eval(input("Enter temperature in Fahrenheit: "))
    celsius = (fahrenheit - 32) * 5.0/9.0
    print(f"{fahrenheit} degrees Fahrenheit is equal to {celsius} degrees Celsius")
elif choice == '2':
    celsius = eval(input("Enter temperature in Celsius: "))
    fahrenheit = (celsius * 9.0/5.0) + 32
    print(f"{celsius} degrees Celsius is equal to {fahrenheit} degrees Fahrenheit")
else:
    print("Invalid choice. Please enter 1 or 2")


# print(f"{celsius} degrees Celsius is equal to {fahrenheit:.2f} degrees Fahrenheit")
# F-String Explanation
# f"":

# The f prefix before the string indicates that it is an f-string, a feature introduced in Python 3.6 for string formatting. It allows you to embed expressions inside string literals, using curly braces {}.
# {celsius}:

# The expression inside the curly braces {celsius} is a placeholder that will be replaced with the value of the variable celsius when the string is printed. This variable should hold a numerical value representing a temperature in Celsius.
# is equal to:

# This is a plain text string that will be included as-is in the output. It provides context to the numerical values being printed.
# {fahrenheit:.2f}:

# Similar to {celsius}, this is a placeholder for the variable fahrenheit.
# The :.2f part is a format specifier that tells Python to format the fahrenheit value as a floating-point number with 2 decimal places.
# : indicates the start of the format specification.
# .2 specifies that the number should be rounded to 2 decimal places.
# f indicates that the number is a floating-point value.