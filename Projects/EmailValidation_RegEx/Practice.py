# a-z --> Lower case
# 0-9
# "." "_" once 
# "@" one time/ once
# . --> position is --> 3rd or 4th from the last
import re #--> import the RegEx Module
Email_Conditions = "^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"
User_Email = input("Enter Your Email: ")
if re.search(Email_Conditions,User_Email):
    print("Right Email")
else:
    print("Wrong Email")
# ^ --> start of the string
# [a-z] --> a-z --> Lower case
# + --> one or more
# [\._]? --> . or _ once
# [a-z 0-9]+ --> a-z or 0-9 once or more
# [@] --> @ once
# \w --> word character (equivalent to [a-zA-Z0-9_])
# [.] --> . once
# \w{2,3} --> 2 or 3 word character (equivalent to
#[a-zA-Z0-9_]{2,3})
# $ --> end of the string