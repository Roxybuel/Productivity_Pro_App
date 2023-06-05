from tkinter import *
from PIL import ImageTk, Image

# creates a window, sets the name and the size
window = Tk()
window.title("Image_Viewer")
window.geometry("600x550")

# all the images used
image_1 = ImageTk.PhotoImage(Image.open("Pro_Image1.jpg"))
image_2 = ImageTk.PhotoImage(Image.open("Pro_Image2.jpg"))
image_3 = ImageTk.PhotoImage(Image.open("Pro_Image3.jpg"))
image_4 = ImageTk.PhotoImage(Image.open("Pro_Image4.jpg"))
image_5 = ImageTk.PhotoImage(Image.open("Pro_Image5.jpg"))

# a list of all the images for the slideshow
image_list = [image_1, image_2, image_3, image_4, image_5]

# creates a label for the images
image_label = Label(image=image_1)
image_label.grid(row=0, column=0, columnspan=3)


# the command to make the buttons move to the next picture
def forward(image_number):
    global image_label
    global forward_button
    global back_button

    # to prevent the images from overlapping
    image_label.grid_forget()

    # to display the new image
    image_label = Label(image=image_list[image_number - 1])

    # to use the buttons to change the images
    forward_button = Button(window, text=">>", command=lambda: forward(image_number + 1))
    back_button = Button(window, text="<<", command=lambda: back(image_number - 1))

    # to prevent the user from clicking past the last image
    if image_number == 5:
        forward_button = Button(window, text=">>", state=DISABLED)

    # set the position of the buttons
    image_label.grid(row=0, column=0, columnspan=3)
    back_button.grid(row=1, column=0)
    forward_button.grid(row=1, column=2)


# the command to make the buttons move to the previous picture
def back(image_number):
    global image_label
    global forward_button
    global back_button

    # to prevent the images from overlapping
    image_label.grid_forget()

    # to display the new image
    image_label = Label(image=image_list[image_number - 1])

    # to use the buttons to change the images
    forward_button = Button(window, text=">>", command=lambda: forward(image_number + 1))
    back_button = Button(window, text="<<", command=lambda: back(image_number - 1))

    # to prevent the user from clicking past the last image
    if image_number == 1:
        back_button = Button(window, text="<<", state=DISABLED)
    # set the position of the buttons
    image_label.grid(row=0, column=0, columnspan=3)
    back_button.grid(row=1, column=0)
    forward_button.grid(row=1, column=2)


# creates buttons for display
back_button = Button(window, text="<<", command=back, state=DISABLED)
exit_button = Button(window, text="EXIT PROGRAM", command=window.quit)
forward_button = Button(window, text=">>", command=lambda: forward(2))

# places the buttons on specific spaces on the screen
back_button.grid(row=1, column=0)
exit_button.grid(row=1, column=1)
forward_button.grid(row=1, column=2)

window.mainloop()
