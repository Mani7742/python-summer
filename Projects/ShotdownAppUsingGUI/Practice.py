from tkinter import *  #--> * is used to import the whole file of tkinker so we don't have to write this command again and again
import os
def restart():
    os.system("shutdown /r /t 1")
def restart_with_time():
    os.system("shutdown /r /t 20")
def logout():
    os.system("shutdown -1")
def shutdown():
    os.system("shutdown /s /t 1")
st = Tk()
st.title("ShutDown App")
st.geometry("500x500")
st.config(bg="blue")
restart_button =  Button(st,text="Restart",font=("Arial",20,"bold"),relief=RAISED,cursor="plus",command=restart)
restart_button.place(x=150,y=20,height=50,width=200)
restart_with_time_button =  Button(st,text="Restart With Time",font=("Arial",15,"bold"),relief=RAISED,cursor="plus",command=restart_with_time)
restart_with_time_button.place(x=150,y=80,height=50,width=200)
Log_Out =  Button(st,text="Log Out",font=("Arial",15,"bold"),relief=RAISED,cursor="plus",command=logout)
Log_Out.place(x=150,y=140,height=50,width=200)
ShutDown =  Button(st,text="ShutDown",font=("Arial",15,"bold"),relief=RAISED,cursor="plus",command=shutdown)
ShutDown.place(x=150,y=200,height=50,width=200)
st.mainloop()