from tkinter import *
from tkinter.font import Font

window = Tk()
window.title("Todo_List")
window.geometry("500x500")

# to define the font of items in the list
font = Font(font=("Times", 30))

# to create the frame
frame = Frame(window)
frame.pack()

# to create a listbox
list_box = Listbox(frame,
                   font=font,
                   width=25,
                   height=5,
                   bg='SystemButtonFace',
                   bd=0,
                   fg="#464646",
                   highlightthickness=0,  # to remove the line around the list
                   selectbackground="#5591be",
                   activestyle="none",
                   )
list_box.pack(side=LEFT, fill=BOTH)

# a random list to display on the screen
Stuff = ["Walk the dog", "Learn how to code", "Eat dinner", "Plan world domination"]
for item in Stuff:
    list_box.insert(END, item)

# to create a scrollbar for our listbox
scroll_bar = Scrollbar(frame)
scroll_bar.pack(side=RIGHT, fill=BOTH)

# to add the scrollbar to the frame
list_box.config(yscrollcommand=scroll_bar.set)
scroll_bar.config(command=list_box.yview)

# to create an entry box to add items to the list
entry_box = Entry(window, font="Helvetica")
entry_box.pack(pady=20)

# to create a button frame
button_frame = Frame(window)
button_frame.pack(pady=20)


# defining functions to make the buttons work
def delete_item():
    list_box.delete(ANCHOR)  # deletes whatever item is chosen


def add_item():
    list_box.insert(END, entry_box.get())
    entry_box.delete(0, END)


def cross_off_item():
    list_box.itemconfig(
        list_box.curselection(),
        fg="#dedede")
    #  to get rid of the selection bar
    list_box.selection_clear(0, END)


def uncross_item():
    list_box.itemconfig(
        list_box.curselection(),
        fg="#464646")  # to return it to the original colour
    #  to get rid of the selection bar
    list_box.selection_clear(0, END)


# creating buttons for the user
delete_button = Button(button_frame, text="Delete Item", command=delete_item)
add_button = Button(button_frame, text="Add Item", command=add_item)
cross_off_button = Button(button_frame, text="Cross Off Item", command=cross_off_item)
uncross_button = Button(button_frame, text="Uncross Item", command=uncross_item)

delete_button.grid(row=0, column=0)
add_button.grid(row=0, column=1, padx=20)
cross_off_button.grid(row=0, column=2)
uncross_button.grid(row=0, column=3, padx=20)

window.mainloop()
