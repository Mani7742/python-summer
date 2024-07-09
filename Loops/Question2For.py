list = [1,4,9,16,25,36,49,64,81,100]
x = 25
idx = 0
for val in list:
    if val == x:
        print("X is found at idx",idx)
        break
    idx = idx + 1