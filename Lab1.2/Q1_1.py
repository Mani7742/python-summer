

# Develop a program that calculates the simple interest for a loan or deposit. 

# Simple Interest=P×R×T

# where:

# 𝑃
# P is the principal amount (the initial amount of money)
# 𝑅
# R is the annual interest rate (in decimal form, so 5% becomes 0.05)
# 𝑇
# T is the time the money is invested or borrowed for, in years

principal = eval(input("Enter the Principal Amount:"))
interest_rate = eval(input("Enter the Interest Rate:"))//100
start_time = int(input("Enter the Time (e.g. 2001):"))
end_time = int(input("Enter the Time (e.g. 2005):"))
year_time = start_time - end_time
simple_interest = principal * interest_rate * year_time
print(f"The Simple Interest is: {simple_interest}")