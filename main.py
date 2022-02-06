import os
from tkinter import *

import PIL.ImageShow
import pygame
from PIL import Image, ImageTk, _tkinter_finder


class PhotoViewer:
    def __init__(self, master, image_files, sound_files):

        pygame.mixer.init()
        self.master = master
        self.master.title("Photo Viewer App")

        self.images, self.sounds = self.__make_image_and_sound_arrays(image_files, sound_files)
        print(self.images)
        self.title = Label(text="Photo Album Viewer", font=("Times New Roman", 25))
        self.main_menu_label = Label(text="Main Menu", font=("Helvetica", 20))
        self.start_button = Button(master, text="Start", command=self.__start_from_beginning, height=2, width=8,
                                   background="#5BB4E2")
        self.close_button = Button(master, text="Close", command=self.__close, background="#C72027")
        self.previous_button = Button(master, text="Previous", command=self.__previous, background="#5BB4E2",
                                      state="disabled")
        self.next_button = Button(master, text="Next", command=self.__next, background="#5BB4E2")
        self.current = -1
        self.__main_menu()
        # self.__view_gallery()

    def __start_from_beginning(self):
        self.__start(0)

    def __start(self, current):
        self.current = current
        self.master.geometry("604x635")
        self.start_button.destroy()
        self.title.destroy()
        self.main_menu_label.destroy()
        self.close_button.place(relx=0.5, rely=0.975, anchor='center')
        self.previous_button.place(relx=0.2, rely=0.975, anchor='center')
        self.next_button.place(relx=0.8, rely=0.975, anchor='center')
        self.__show_image(0)
        self.__play_sound(0)

    def __main_menu(self):
        self.title.place(relx=0.5, rely=0.2, anchor='center')
        self.main_menu_label.place(relx=0.5, rely=0.4, anchor='center')
        self.start_button.place(relx=0.5, rely=0.7, anchor='center')
        self.close_button.place(relx=0.5, rely=0.85, anchor='center')
        self.master.geometry("300x300")
        self.master.configure(bg="#F4EDD3")
        self.current = -1

    def __view_gallery(self):
        # TODO
        image = ImageTk.getimage(self.images[1])
        image = image.resize((450, 350), Image.ANTIALIAS)
        my_img = ImageTk.PhotoImage(image)
        my_img = Label(image=my_img)
        i = Label(image=my_img)
        i.place(relx=0.5, rely=0, anchor='n')
        return

    def __next(self):
        self.current += 1
        self.__update_buttons()
        self.__show_image(self.current)
        self.__play_sound(self.current)

    def __previous(self):
        self.current -= 1
        self.__update_buttons()
        self.__show_image(self.current)
        self.__play_sound(self.current)

    def __update_buttons(self):
        # first image
        if self.current == 0:
            self.previous_button = Button(self.master, text="Previous", state="disabled", background="#4C98BF")
            self.previous_button.place(relx=0.2, rely=0.975, anchor='center')

        # last image
        if self.current == len(self.images) - 1:
            self.next_button = Button(self.master, text="Next", state="disabled", command=self.__next,
                                      background="#5BB4E2")
            self.next_button.place(relx=0.8, rely=0.975, anchor='center')

        # any other image
        if 0 < self.current < len(self.images) - 1:
            self.next_button = Button(self.master, text="Next", command=self.__next, background="#5BB4E2")
            self.next_button.place(relx=0.8, rely=0.975, anchor='center')
            self.previous_button = Button(self.master, text="Previous", command=self.__previous, background="#5BB4E2")
            self.previous_button.place(relx=0.2, rely=0.975, anchor='center')

    def __close(self):
        self.master.quit()

    def __show_image(self, n):
        i = Label(image=self.images[n])
        i.place(relx=0.5, rely=0, anchor='n')

    def __play_sound(self, n):
        pygame.mixer.music.stop()

        if self.sounds[n] is None:
            return

        pygame.mixer.music.load(self.sounds[n])
        pygame.mixer.music.play(loops=0)

    @staticmethod
    def __make_image_and_sound_arrays(png_files, mp3_files):
        new_png_files = []
        new_mp3_files = []
        for img in png_files:
            mp3_name = img[0:-4] + '.mp3'
            new_png_files.append(PhotoImage(file='media/images/' + img))
            if mp3_name in mp3_files:
                new_mp3_files.append('media/sounds/' + mp3_name)
            else:
                new_mp3_files.append(None)
        return new_png_files, new_mp3_files

    def __get_small_images(self, x, y):

        return


pics = []
tunes = []
for root, dirs, files in os.walk('media/images'):
    pics = files
for root, dirs, files in os.walk('media/sounds'):
    tunes = files

window = Tk()
PhotoViewer(window, pics, tunes)
window.mainloop()
