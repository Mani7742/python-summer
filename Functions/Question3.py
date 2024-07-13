# WAF to print the element of a list in a single line (list is a parameter)
l = [1,2,3,4,5,6,7,8,9,0]
print(l)
def print_list(list):
    for i in list:
        print(i,end=" ")
print_list(l)
