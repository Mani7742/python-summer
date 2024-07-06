# array in other languages but in python it is called list
# list can store different types of values(integer, float, string etc)
# list is mutable in pyhton but strings are immutable

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

#----------------------------------< Tuple(Immutable) >----------------------------------
# Tuple is a collection which is ordered and unchangeable. In Python tuples are written with round
# brackets.
# Tuples are unchangeable, meaning that we cannot change, add or remove items after the
# tuple has been created.

tuple1 = (1,4,6,3,2,9,5)
print(tuple1)
print(tuple1[0])
print(tuple1[1])
#tuple[3] = 10 ---> this thing is not allow in python beacuse tuples are immutable datatype
tuple2 = (1,) #---> this thing is valid
print(type(tuple2))
tuple3 = (1) #---> this thing is also valid but python thinks that it is an integer value
print(type(tuple3))

# Functions in Tuple
# 1. count() - returns the number of times a specified value occurs in a tuple
tuple4 = (1,24,4,5,6,23,5,6,7,6)
print(tuple4.count(6))
# 2. index() - searches the tuple for a specified value and returns the position of where
# it was found
tuple5 = (1,2,3,4,5,6,6,7,)
print(tuple5.index(3))