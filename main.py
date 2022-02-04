import os
from tkinter import *
import pygame


class PhotoViewer:
    def __init__(self, master, image_files, sound_files):

        pygame.mixer.init()
        self.master = master
        self.master.title("Photo Viewer App")

        self.images = []
        self.sounds = []
        self.make_image_and_sound_arrays(image_files, sound_files)

        self.title = Label(text="Photo Album Viewer", font=("Times New Roman", 25))
        self.main_menu_label = Label(text="Main Menu", font=("Helvetica", 20))
        self.start_button = Button(master, text="Start", command=self.start_from_beginning, height=2, width=8,
                                   background="#5BB4E2")
        self.close_button = Button(master, text="Close", command=self.close, background="#C72027")
        self.previous_button = Button(master, text="Previous", command=self.previous, background="#5BB4E2",
                                      state="disabled")
        self.next_button = Button(master, text="Next", command=self.next, background="#5BB4E2")
        self.current = -1
        self.main_menu()

    def start_from_beginning(self):
        self.start(0)

    def start(self, current):
        self.current = current
        self.master.geometry("604x635")
        self.start_button.destroy()
        self.title.destroy()
        self.main_menu_label.destroy()
        self.close_button.place(relx=0.5, rely=0.975, anchor='center')
        self.previous_button.place(relx=0.2, rely=0.975, anchor='center')
        self.next_button.place(relx=0.8, rely=0.975, anchor='center')
        self.show_image(0)
        self.play_sound(0)

    def main_menu(self):
        self.title.place(relx=0.5, rely=0.2, anchor='center')
        self.main_menu_label.place(relx=0.5, rely=0.4, anchor='center')
        self.start_button.place(relx=0.5, rely=0.7, anchor='center')
        self.close_button.place(relx=0.5, rely=0.85, anchor='center')
        self.master.geometry("300x300")
        self.master.configure(bg="#F4EDD3")
        self.current = -1

    def view_gallery(self):
        # TODO
        return

    def next(self):
        self.current += 1
        self.update_buttons()
        self.show_image(self.current)
        self.play_sound(self.current)

    def previous(self):
        self.current -= 1
        self.update_buttons()
        self.show_image(self.current)
        self.play_sound(self.current)

    def update_buttons(self):
        # first image
        if self.current == 0:
            self.previous_button = Button(self.master, text="Previous", state="disabled", background="#4C98BF")
            self.previous_button.place(relx=0.2, rely=0.975, anchor='center')

        # last image
        if self.current == len(self.images) - 1:
            self.next_button = Button(self.master, text="Next", state="disabled", command=self.next,
                                      background="#5BB4E2")
            self.next_button.place(relx=0.8, rely=0.975, anchor='center')

        # any other image
        if 0 < self.current < len(self.images) - 1:
            self.next_button = Button(self.master, text="Next", command=self.next, background="#5BB4E2")
            self.next_button.place(relx=0.8, rely=0.975, anchor='center')
            self.previous_button = Button(self.master, text="Previous", command=self.previous, background="#5BB4E2")
            self.previous_button.place(relx=0.2, rely=0.975, anchor='center')

    def close(self):
        self.master.quit()

    def show_image(self, n):
        i = Label(image=self.images[n])
        i.place(relx=0.5, rely=0, anchor='n')

    def play_sound(self, n):
        pygame.mixer.music.stop()

        if self.sounds[n] is None:
            return

        pygame.mixer.music.load(self.sounds[n])
        pygame.mixer.music.play(loops=0)

    def make_image_and_sound_arrays(self, png_files, mp3_files):
        new_png_files = []
        new_mp3_files = []
        for img in png_files:
            mp3_name = img[0:-4] + '.mp3'
            new_png_files.append(PhotoImage(file='media/images/' + img))
            if mp3_name in mp3_files:
                new_mp3_files.append('media/sounds/' + mp3_name)
            else:
                new_mp3_files.append(None)
        self.images = new_png_files
        self.sounds = new_mp3_files


pics = []
tunes = []
for root, dirs, files in os.walk('media/images'):
    pics = files
for root, dirs, files in os.walk('media/sounds'):
    tunes = files

window = Tk()
PhotoViewer(window, pics, tunes)
window.mainloop()
