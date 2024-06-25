
# Write a program that converts a decimal number to binary and prints the binary representation.

decimal_number = int(input("Enter the Decimal Value:"))

if decimal_number == 0:
    print("Binary representation is Zero")
else:
    binary_representation = ""
    while decimal_number > 0:
        binary_representation = str(decimal_number % 2) + binary_representation
        decimal_number = decimal_number // 2
        print("Binary representation is", binary_representation)
            