from tkinter import *
import time

# this creates the tkinter window, sets the size and gives it a name
window = Tk()
window.geometry("600x400")
window.title("Alarm_Clock")

# this creates a label
alarm_label = Label(window, text="", font=("Times", 50), fg="blue", bg="black")
alarm_label.pack(pady=20)

alarm_label2 = Label(window, text="", font=("Times", 15))
alarm_label2.pack(pady=10)


def clock():
    hour = time.strftime("%I")
    minute = time.strftime("%M")
    second = time.strftime("%S")
    day = time.strftime("%A")
    time_of_day = time.strftime("%p")
    time_zone = time.strftime("%Z")

    alarm_label.config(text=hour + ":" + minute + ":" + second + " " + time_of_day)
    alarm_label.after(1000, clock)

    alarm_label2.config(text=time_zone + "" + '\n' + day)


clock()
window.mainloop()
