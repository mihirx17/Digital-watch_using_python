from tkinter import *
from time import strftime
app_window = Tk()
app_window.title("Digital Clock")
app_window.geometry("420x150")
app_window.configure(background="Black")
def time():
    time_funtion=strftime("%H:%M:%S")
    time1.configure(text=time_funtion)
    time1.after(1000,time)

time1=Label(app_window,font=("Green London",90),background="black",foreground="#CD2626")
time1.pack()
time()
mainloop()
