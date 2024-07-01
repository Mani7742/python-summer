
# This is done by positive index
a = "Ammara Akhtar"
print(a[0:7]) # name of string [straing index : ending index]
print(len(a))
print(a[0:13])
print(a[0:]) # this will automatically go to the last index pyhton accecpt this---> this means [0:13]
print(a[:]) # this will automatically get the staring and ending index 
print(a[:13]) # this will automatically get the strating index

# This is done by negative indexing
# negative index starts from -1
b = "Abdul Rehman Shakeel"
print(len(b))
print(b[-1]) # this will print the last character of the string
print(b[-7:])
# -5, -4, -3, -2, -1
# apple---> [-5:-1]----> appl ---> last one is not included