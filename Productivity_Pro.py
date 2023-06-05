import subprocess
from tkinter import ttk, Tk

window = Tk()
window.title("Productivity_Pro")
window.geometry("500x550")
window.configure(background='#2b5ec4')

style = ttk.Style()
style.configure('TButton', foreground="#0066cc")


def open_mp3_player():
    subprocess.Popen(['python', 'MP3_Player.py'])


def open_todo_list():
    subprocess.Popen(['python', 'Todo_List.py'])


def open_image_viewer():
    subprocess.Popen(['python', 'Image_Viewer.py'])


def open_alarm_clock():
    subprocess.Popen(['python', 'Alarm_Clock.py'])


Alarm_button = ttk.Button(window, text="Open Alarm Clock App", command=open_alarm_clock)
Alarm_button.pack(padx=10, pady=50)

Image_Button = ttk.Button(window, text="Open Image Viewer App", command=open_image_viewer)
Image_Button.pack(padx=10, pady=50)

Todo_Button = ttk.Button(window, text="Open Todo List App", command=open_todo_list)
Todo_Button.pack(padx=10, pady=50)

MP3_Button = ttk.Button(window, text="Open MP3 Player App", command=open_mp3_player)
MP3_Button.pack(padx=10, pady=50)

window.mainloop()
