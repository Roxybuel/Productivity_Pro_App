from tkinter import *
import pygame
from PIL import ImageTk, Image
from tkinter import filedialog

# creates the window, sets the title and its size
window = Tk()
window.title("MP3_Player")
window.geometry("500x300")

# initializes pygame mixer for music
pygame.mixer.init()


# to add one song to the playlist
def add_song():
    song = filedialog.askopenfilename(initialdir='audio/', title="Choose a Song", filetypes=(("mp3 Files", "*.mp3"),))
    # to remove the directory and mp3 extension
    song = song.replace("C:/Users/Nonye.Iweanoge/OneDrive - Great Lakes Christian High School/Semester 2/Computer "
                        "Science/audio/", "")
    song = song.replace(".mp3", "")
    # to add the song to the playlist
    song_playlist.insert(END, song)


# to add more than one song to the playlist
def add_many_songs():
    songs = filedialog.askopenfilenames(initialdir='audio/', title="Choose a Song", filetypes=(("mp3 Files", "*.mp3"),))

    # to loop through the song list
    for song in songs:
        song = song.replace("C:/Users/Nonye.Iweanoge/OneDrive - Great Lakes Christian High School/Semester 2/Computer "
                            "Science/audio/", "")
        song = song.replace(".mp3", "")

        # add songs to playlist
        song_playlist.insert(END, song)


# defining the command to play the selected song
def play():
    song = song_playlist.get(ACTIVE)
    song = f'C:/Users/Nonye.Iweanoge/OneDrive - Great Lakes Christian High School/Semester 2/Computer Science/audio/{song}.mp3'
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)


def stop():
    pygame.mixer.music.stop()
    song_playlist.selection_clear(ACTIVE)


def next_song():
    next_one = song_playlist.curselection()
    # add 1 to the current song number
    next_one = next_one[0] + 1
    song = song_playlist.get(next_one)
    song = f'C:/Users/Nonye.Iweanoge/OneDrive - Great Lakes Christian High School/Semester 2/Computer Science/audio/{song}.mp3'
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)

    # move the active bar to the next song
    song_playlist.selection_clear(0, END)
    song_playlist.activate(next_one)
    song_playlist.selection_set(next_one, last=None)


def previous_song():
    next_one = song_playlist.curselection()
    # add 1 to the current song number
    next_one = next_one[0] - 1
    song = song_playlist.get(next_one)
    song = f'C:/Users/Nonye.Iweanoge/OneDrive - Great Lakes Christian High School/Semester 2/Computer Science/audio/{song}.mp3'
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)

    # move the active bar to the next song
    song_playlist.selection_clear(0, END)
    song_playlist.activate(next_one)
    song_playlist.selection_set(next_one, last=None)


# to create a global pause variable
global paused
paused = False


def pause(is_paused):
    global paused
    paused = is_paused

    if paused:
        # if the song is already paused, unpause it
        pygame.mixer.music.unpause()
        paused = False
    else:
        # to pause the song
        pygame.mixer.music.pause()
        paused = True


# to create the box to display the music selection
song_playlist = Listbox(window, bg="black", fg="blue", width=60)
song_playlist.pack(pady=20)

# to create the button's image and resize them
stop_button_image = Image.open('stop_button.png')
resize_stop_button = stop_button_image.resize((50, 50))
real_stop = ImageTk.PhotoImage(resize_stop_button)

forward_button_image = Image.open('forward_button.jpg')
resize_forward_button = forward_button_image.resize((50, 50))
real_forward = ImageTk.PhotoImage(resize_forward_button)

back_button_image = Image.open('backward_button.jpg')
resize_backward_button = back_button_image.resize((50, 50))
real_backward = ImageTk.PhotoImage(resize_backward_button)

play_button_image = Image.open('play_button.jpg')
resize_play_button = play_button_image.resize((50, 50))
real_play = ImageTk.PhotoImage(resize_play_button)

pause_button_image = Image.open('pause_button.jpg')
resize_pause_button = pause_button_image.resize((50, 50))
real_pause = ImageTk.PhotoImage(resize_pause_button)

# create frame for the buttons
control_frame = Frame(window)
control_frame.pack()

# create buttons
back_button = Button(control_frame, image=real_backward, borderwidth=0, command=previous_song)
play_button = Button(control_frame, image=real_play, borderwidth=0, command=play)
pause_button = Button(control_frame, image=real_pause, borderwidth=0, command=lambda: pause(paused))
stop_button = Button(control_frame, image=real_stop, borderwidth=0, command=stop)
forward_button = Button(control_frame, image=real_forward, borderwidth=0, command=next_song)

# place the buttons at specific spots on the screen
forward_button.grid(row=0, column=4, padx=10)
back_button.grid(row=0, column=0, padx=10)
play_button.grid(row=0, column=2, padx=10)
pause_button.grid(row=0, column=1, padx=10)
stop_button.grid(row=0, column=3, padx=10)

# to create the menu
the_menu = Menu(window)
window.config(menu=the_menu)

# to create the add song menu
add_song_menu = Menu(the_menu)
the_menu.add_cascade(label="Add Songs", menu=add_song_menu)
add_song_menu.add_command(label="Add One Song To Playlist", command=add_song)

# add many songs to playlist
add_song_menu.add_command(label="Add Many Songs To Playlist", command=add_many_songs)

window.mainloop()
