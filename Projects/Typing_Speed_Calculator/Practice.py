from time import *
import random as r

def mistake(Paratest,usertest):
    error=0
    for i in range(len(Paratest)):
        try:
            if Paratest[i]!=usertest[i]:
                error+=1
        except:
            error+=1
    return error

def speed_time(time_s,time_e,userinput):
    time_delay = time_e - time_s
    time_R = round(time_delay,2)
    speed = len(userinput)/time_delay
    return round(speed)

if __name__ == "__main__":
    while True:
        ch = input("Ready to Test: yes/no")
        if ch == "yes":
            test =["Ya Allah mari madad kr","Ay Allah ma theek say kuch bhe nahe kr pa raha","Mujha himat dy"]
            test1=r.choice(test)
            print("   ***** Typing Speed *****")
            print(test1)
            print()
            print()
            time_1 = time()
            testinput = input("Enter: ")
            time_2 = time()
            print("Speed:",speed_time(time_1,time_2,testinput),"w/sec")
            print("Error:",mistake(test,testinput))
        elif ch == "no":
            print("Thank you")
            break
        else:
            print("Invalid Input")