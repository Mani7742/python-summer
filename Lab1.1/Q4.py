

#Develop a program that swaps the values of two integer variables without using a third variable.

a = 5
b = 10

print(f"Before Swap: a = {a}, b = {b}")

a = a+b # 5+10=15
b = a-b # 15-10=5
a = a-b # 15-5=10

print(f"After Swap: a = {a}, b = {b}")