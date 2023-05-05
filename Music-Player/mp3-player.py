from tkinter import *
from tkinter import Tk
from tkinter import filedialog
from pygame import mixer
import os
import tkinter.font as font
from PIL import ImageTk, Image

root=Tk()
root.title('Music player project')
root.geometry("920x670+290+85")
root.configure(bg= "black")
root.resizable(False, False)
mixer.init()

defined_font = font.Font(family='Helvetica')

def Add_Music():
    path = filedialog.askdirectory()
    if path:
        os.chdir(path)
        songs = os.listdir(path)
 
        for song in songs:
            if song.endswith(".mp3"):
                Playlist.insert(END, song)
 
def Play_Music():
    Music_Name= Playlist.get(ACTIVE)
    print(Music_Name[0:-4])
    mixer.music.load(Playlist.get(ACTIVE))
    mixer.music.play()

#Top image
Top_Image = ImageTk.PhotoImage(Image.open("Music-Player\Front-img.jpg").resize((1000, 1000)))
Label(root, image=Top_Image, bg="#0f1a2b").pack()

 #logo
logo_Image = ImageTk.PhotoImage(Image.open("Music-Player\Mymusic_logo.jpg").resize((200, 300)))
Label(root, image=logo_Image, bg="#0f1a2b").place(x=40, y=50)

#Button
Button_Play = ImageTk.PhotoImage(Image.open("Music-Player\Remote_play.jpg").resize((40, 40)))
Button(root, image=Button_Play, bg="#0f1a2b", bd=0, command=Play_Music).place(x=115, y=420)

 
Button_Stop = ImageTk.PhotoImage(Image.open("Music-Player\Remote_stop.jpg").resize((40, 40)))
Button(root, image=Button_Stop, bg="#0f1a2b", bd=0, command=mixer.music.stop).place(x=30, y=500)


#Button
Button_Pause = ImageTk.PhotoImage(Image.open("Music-Player\Remote_pause.jpg").resize((40, 40)))
Button(root, image=Button_Pause, bg="#0f1a2b", bd=0, command=mixer.music.pause).place(x=115, y=500)
 
#Button
Button_Resume = ImageTk.PhotoImage(Image.open("Music-Player\Remote_resume.jpg").resize((40, 40)))
Button(root, image=Button_Resume, bg="#0f1a2b", bd=0, command=mixer.music.unpause).place(x=200, y=500)
   
#music
Menu = ImageTk.PhotoImage(Image.open("Music-Player\Music_logo.jpg").resize((20, 20)))
Label(root, image=Menu, bg="#0f1a2b").pack(padx=10, pady=50, side=RIGHT)
 
Frame_Music = Frame(root, bd=2, relief = RIDGE)
Frame_Music.place(x=330, y=350, width=560, height=250)
 
Button(root, text="Add Music", width=10, height=1, font=("times new roman",12,"bold"),fg="white", bg="black", command= Add_Music).place(x=330, y=300)
 
Scroll = Scrollbar(Frame_Music)
Playlist = Listbox(Frame_Music, width=100, font=("Times new roman",10), bg="black", fg="white", selectbackground="lightblue", cursor="hand2", bd=0, yscrollcommand=Scroll.set)
Scroll.config(command=Playlist.yview)
Scroll.pack(side=RIGHT, fill=Y)
Playlist.pack(side=LEFT, fill=BOTH)
 
root.mainloop()
