from tkinter import *
import pygame

root = Tk()
root.title('mp3')
root.geometry('500x400')

pygame.mixer.init()

def play():
    pygame.mixer.music.load("resources/out/demofile.mid")
    pygame.mixer.music.play(loops=0)

my_button = Button(root, text="play", command=play)
my_button.pack(pady=20)

root.mainloop()