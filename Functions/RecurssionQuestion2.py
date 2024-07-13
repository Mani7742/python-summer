
l = [1,2,3,4,5,6,7,8,9,0]
def print_list(list,idx = 0):
    if(idx == len(list)):
        return
    print(list[idx])
    print_list(list,idx+1)
print_list(l)    