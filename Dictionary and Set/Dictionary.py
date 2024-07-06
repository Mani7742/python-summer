
# -----------------------------< Mutable Datatypes >-------------------------------------
# In Python, the following datatypes are mutable:
# 1. List
# 2. Dictionary
# 3. Set
# 4. User-defined classes (unless specifically made immutable)
# Mutable datatypes can be modified after they are created.
# -------------------------------------------------------------------------------------

#-----------------------------------< Distionary (Mutable) >------------------------------
# A dictionary is a collection of key-value pairs. Each key is associated with a value.
# Dictionaries are mutable, meaning that you can change the value associated with a key.
# Key:Value----> in the form of Pairs
# Mutable Datatype Are not able to be the part of key
# Value can be mutable and immutable
# -------------------------------------------------------------------------------------

#-------------------------------------< Rules of Dictionary >----------------------------------------
#1)Mutable
#2)Unordered
#3)Key:Value----> in the form of Pairs
#4)Cannot create duplicate key
#5)Null Dictionary is created
#6) Nested Dictionary is also Created
# -------------------------------------------------------------------------------------
Dict = {
    "Name" : "HM Abdul Rehman Shakeel",
    "Age" : 20,
    "City" : "Faisalabad",
    "Country" : "Pakistan",
    "Is Married" : False,
    "Is Student" : True,
    "Marks" : [80, 90, 70, 60, 100], #----> List
    "Address" : "House No. P-379, Islam Nagar, Faisalabd",
    "Phone Number" : +923048547030,
    "Email" : "abdulrehmanshakeel003@gmail.com",
    "CGPA" : 2.90
}
print(type(Dict))
print(Dict)
print(Dict["Age"])
print(Dict["City"])
print(Dict["Is Married"])
Dict["Age"] = 23 #----> this is the example that we can change the value of Dictionary
Dict["Father's name"] = "Shakeel Ahmad"#---> We can also add the information in Dictionary jut like we do in list by using .append() Function
print(Dict["Father's name"])
print(Dict["Age"])

Student = {
    "Name" : "HM Abdul Rehman Shakeel",
    "Age" : 20,
    "City" : "Faisalabad",
    "Marks" : { #-------------------> Nested Dictionary
        "Maths" : 80,
        "Urdu" : 90,
        "English" : 70,
        "Physics" : 60,
        "Chemistry" : 100
        }
    }
print(Student)
print(Student["Marks"])

#------------------------------------------------------------------------------------------------
#-----------------------------------< Methods/Functions In Dictionary >--------------------------
#1)keys()----> It returns the keys of Dictionary
#2)values()----> It returns the values of Dictionary
#3)items()----> It returns the items of Dictionary
#4)update()----> It updates the Dictionary
#5)clear()----> It clears the Dictionary
#6)pop()----> It removes the item from Dictionary
#7)popitem()----> It removes the last item from Dictionary
#8)copy()----> It returns the copy of Dictionary
#9)get()----> It returns the value of Dictionary
#------------------------------------------------------------------------------------------------
Personal_Info = {
    "Name" : "HM Abdul Rehman Shakeel",
    "Age" : 20,
    "City" : "Faisalabad",
    "CGPA" : 2.90
}
print(len(Personal_Info))
print(Personal_Info.keys())
print(Personal_Info.values())
print(Personal_Info.items())
print(Personal_Info.update({"Age":23}))
print(Personal_Info.get("Name2")) #------> this will give us None
#print(Personal_Info["Name2"])#--->This Will give us an error
print(Personal_Info.clear())
print(Personal_Info)
print(Personal_Info.pop("Name"))

