# Write a python program to find the sum of all even numbers from 1 to 100 using a while loop.
sum_of_evens = 0
numbers = 1
while numbers <= 100:
    if numbers % 2 == 0:
        # sum_of_evens += numbers
        sum_of_evens = sum_of_evens + numbers
    numbers += 1
print("Sum of evens from 1 to 100:-",sum_of_evens)