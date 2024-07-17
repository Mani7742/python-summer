
# Static methods don't use self parameter (Work at class level)
#Self is used for objects

class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks

    def get_Average(self): # Non-Static Method
        sum = 0
        for val in self.marks:
            sum = sum + val
        print("Hi",self.name,"Your Average Score is ", sum/3)

    
    @staticmethod # decorator
    def hello():
        print("Hello Bhai Jan")


s1 = Student("Ammara",[98,84,89])   
s1.get_Average()
s1.hello()