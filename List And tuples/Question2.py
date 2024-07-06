
#WAP to check if a list contains a palindrome or not
list1 = [1,23,1]
copy_list1 = list1.copy()
copy_list1.reverse()
if(list1 == copy_list1):
    print("it is a Palindrome")
else:
    print("it is not a Palindrome")