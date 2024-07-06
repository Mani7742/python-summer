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
# ------------------------------< List (Mutable) >------------------------------------------------
student1183 = ["HM Abdul Rehman Shakeel", "22-NTU-CS-1183", 23, "FSD"]
print(student1183[0]) #---> by using index
print(len(student1183)) #---> getting the lenthn of the list
print(type(student1183)) #---> getting the type 
print(student1183)
student1183[0] = "Ammara Akhtar"
print(student1183) #---> changing the value of the list
#list slicing is also possible in list similar to string slicing
# list_name[staring index: ending in index] basically ending index in not included
print(student1183[0:3]) #---> list slicing
#---> Nagative index in also included
print(student1183[-1]) #---> getting the last element of the list
# Functions in list
# 1. append() : add an element at the end of the list
#---- Means last ma kisi cheez ko jor dana
list = [7,5,1,3,2,8,6,4,9]
list.append(10)
print(list)
# 2. insert() : add an element at the specified position of the list
#---- Means kisi cheez ko kisi index par jor dana
list.insert(0,11)
# 3. remove() : remove the specified element from the list
list.remove(9)
# 4. pop() : remove the last element from the list
list2 = [1,2,3,4,5]
list2.pop()
print(list2)
# 5. clear() : remove all the elements from the list
list3 = [1,2,3,4,5]
list3.clear()
print(list3)
# 6. sort() : sort the list 
# in ascending order
list.sort()
#list.sort(reverse=True)
print(list)
# 7. reverse() : reverse the list
# in decending order
list.reverse()
print(list)
# 8. index() : returns the index of the specified element in the list
# if the element is not present in the list then it will return an error
print(list.index(3))
# 9. count() : returns the number of elements with the specified value in the list
print(list.count(3)) #---> 3 kitni bar repeat ho raha hy ya bataye ga es function ma
# 10. extend() : add all the elements of a list to the specified list
list4 = [1,2,3,4,5]
list5 = [6,7,8,9,10]
list4.extend(list5)
print(list4)
# 11. copy() : returns a copy of the specified list
list2.copy()
print(list2)

