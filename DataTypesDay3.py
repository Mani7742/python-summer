

# -----------------------------< Mutable Datatypes >-------------------------------------
# In Python, the following datatypes are mutable:
# 1. List
# 2. Dictionary
# 3. Set
# 4. User-defined classes (unless specifically made immutable)
# Mutable datatypes can be modified after they are created.
# -------------------------------------------------------------------------------------

# ------------------------------< Immutable Datatypes >----------------------------------
# In Python, the following datatypes are immutable:
# 1. Integers
# 2. Floats
# 3. Complex numbers
# 4. Strings
# 5. Tuples
# 6. Boolean
# Immutable datatypes cannot be modified after they are created.
# -------------------------------------------------------------------------------------



# -----------------------------< Numaric Datatypes >--------------------------------------

# 1----> Complex Numbers
a = 10j
print(a, type(a)) #type() function is used to know about the DATATYPE of a variable
# 2----> Integers
a = 5
print(a, type(a))
# 3----> Floats
a = 5.5
print(a, type(a))


#-----------------------------------< Sequence Type >-----------------------------------

# 1----> String
s = "Hello"
print(s, type(s))
s = 'Chal bhai'
print(s, type(s)) # triple quotation is used when we want to print exactly the way we write it in the editor
s = '''
kam
kr 
bohat
ho gya hy ab
'''
print(s, type(s))

# 2---->List
# Mutable
l = [1, 2.2, 'hello']
l[1]=4.4 #-------> changed the value from 2.2 to 4.4
print(l, type(l))

# 3---->Tuple
# faster than list
# Immutable 
t = (1, 2.2, 'hello')
# t[1]=4.4 #-------> this will give an error because tuple is immutable
print(t, type(t))


# ------------------------------------------< Dictionary >---------------------------------------------

# mutable
# key is unique you cannot use repeated keys in dictionary
# dict={Value:Key}
d = {
    'Course_name' : 'Python'
    ,'Duration' : '3 months'
}
print(d['Course_name'])
print(d, type(d))

# -----------------------------------------< Set >-----------------------------------------------------

#Only Unique Values
#Unordered
#Immutable -------> cannot be changed -----> According to Wscube tech
s = {10,20,10,40,50,20}
print(s, type(s)) #-------> Remove the repeated values