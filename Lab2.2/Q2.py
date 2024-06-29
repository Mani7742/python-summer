# Develop a program that checks if a given character is a vowel, consonant, or another character (e.g., symbol) 
# using if-else-if.

# in and not in is membership operators

char = input("Enter a Single Character form abd/ABC: ")

if len(char) != 1:
    print("Please enter a single character")
else:
    if char in "aeiouAEIOU":
        print("Vowel")
    elif char in "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNP":
        print("Consonant")
    else:
        print("Special Character")