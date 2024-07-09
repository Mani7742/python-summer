tuple = (1,4,9,16,25,36,49,64,81,100)
x = 36
idx = 0
while idx < len(tuple):
    if tuple[idx] == x:
        print("Found at index", idx)
        break
    else:
        print("Finding...")    
    idx = idx + 1    