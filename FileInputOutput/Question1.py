# with open("sample.txt","r") as f:
#     data = f.read()
# # f.write("Hi Everyone\nWe are Learning python\nusing apnacollage\ni like programming in python")

# new_data = data.replace("python", "Java")
# print(new_data)

# word = "Learning"
# with open("sample.txt","r") as f:
#     # f.write("Hi Everyone\nWe are Learning python\nusing apnacollage\ni Like programming in python")
#     data = f.read()
#     if (data.find(word) != -1):
#         print("Found")
#     else:
#         print("Not Found")    


# with open("sample.txt","r") as f:
#     f.write("Hi Everyone\nWe are Learning python\nusing apnacollage\ni Like programming in python")
def check_for_line():
    word = "Learning"
    data = True
    line_no = 1
    with open("sample.txt","r") as f:
        while data:
            data = f.readline()
            if(word in data):
                print("Found in line no. ",line_no)
                return
            line_no = line_no + 1    
    return -1
print(check_for_line())