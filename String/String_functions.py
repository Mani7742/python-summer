# built-in function .endswith()
# returns true if the string ends with substring
str1 = "I am on my to become a python developer"
print(str1.endswith("per"))
print(str1.endswith("Uff Allah"))

# built-in function .capitalize()---> capitalize the 1 character
str2 = "inshallah! I will beat everyone arround me and got the First Position "
print(str2.capitalize())#---> .capitalize() create a new string this will not effect the original string
print(str2)
str2 = str2.capitalize() #---> Now this will effect the original string like if we want to change the string 
print(str2)

# built-in function .replace(old,new) --> Replace all occurrence of old
str3 = "I am Studying JavaScript"
print(str3.replace("JavaScript","Python"))

# built-in function .find( word ) --> returns the 1st index of 1st occurrence
str4 = "I am human, a great human, the creation of Allah Almighty."
print(str4.find("human"))

# built-in function .count() -->counts the occurrence of substring
str5 = "I am human, a great human, the creation of Allah Almighty. I am not doing good. I have to give the answer to Allah Almighty"
print(str5.count("I"))