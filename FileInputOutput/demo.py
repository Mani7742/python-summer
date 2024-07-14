#----------------------------------< File Input/Output in Python >-----------------------------------------
# Characters and their Meanings
# \n - means new line   
# \t - means tab
# \r - means carriage return
# \b - means backspace
# \f - means form feed
# \v - means vertical tab
# \a - means alert (beep)
# \ooo - means octal value
# \xhh - means hexadecimal value
#----------------------------------< File Input/Output in Python >-----------------------------------------
# "r" means reading a File
# "w" means writing a File
# "a" means appending a File
# "r+" means reading and writing a File
# "x" create a new file and open it for writing
# "b" binary mode
# "t" text mode
# "+" open a disk file updating (reading and writing)
#------------------------------------------------------------------------------------------------------

#------------------------------------------< Reading a File >-------------------------------------------------

# f = open("Allah.txt", "r")
# # data = f.read()
# # data = f.read(5) #---> only read the first five characters
# Line1 = f.readline()
# print(Line1)
# Line2 = f.readline()
# print(Line2)
# f.close()

#----------------------------------------< Writing in a File >---------------------------------------------

# "a" --> append --> write at the end
# "w" ---> for writing
# f = open("Allah.txt", "w") #--> rewrite
# f = open("Allah.txt","a") #--> for append
# data = f.write("\n Allah maaf kara")
# f.close()

#------------------------------------------< For Reading And Writing >--------------------------------------
# f = open("Allah.txt", "w+") ---> trancate
# f = open("Allah.txt", "r+") #--> no trancate
# # data = f.write("\n Ab kya Karo Allah, Mari Help karo mara Allah")
# data = f.read()
# print(data)

#------------------------------------------< with syntax >-------------------------------------------------
# as is used to give the alias to a file--> file is one but having the two names
# with will automatically close the file for us we do not need to close the file separately
# with open("Allah.txt","r") as f:
#     data = f.read()
#     print(data)

#---------------------------------------------< Creating a new file >----------------------------
# f = open("Allah.txt","+a")

#-------------------------------------------< Deleting a file >--------------------------------------------
# import os
# os.remove("Allah.txt") #--> for deleting a file


