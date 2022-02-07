import os
from functools import partial
from tkinter import *

import pygame


class PhotoViewer:
    def __init__(self, master, image_files, sound_files, small_images):
        self.music_player = pygame.mixer
        self.master = master
        self.gallery_buttons, self.images, self.sounds, self.small_images = [], [], [], []
        self.images, self.sounds, self.small_images = self.__make_image_and_sound_arrays(image_files, sound_files,
                                                                                         small_images)
        self.title = Label()
        self.main_menu_label = Label()
        self.start_button = Button()
        self.gallery_button = Button()
        self.main_menu_button = Button()
        self.close_button = Button()
        self.previous_button = Button()
        self.next_button = Button()
        self.current_image = Label()
        self.current = -1
        self.__create_everything()
        self.__main_menu()

    def __start_from_beginning(self):
        self.__start(0)

    def __start(self, current):
        self.__destroy_everything()
        self.__create_everything()
        self.current = current
        self.master.geometry("604x635")
        self.main_menu_button.place(relx=0.8, rely=0.975, anchor='e')
        self.close_button.place(relx=1, rely=0.975, anchor='e')
        self.gallery_button.place(relx=0.6, rely=0.975, anchor='e')
        self.__update_buttons()
        self.__show_image(self.current)
        self.__play_sound(self.current)

    def __main_menu(self):
        self.music_player.music.stop()
        self.__destroy_everything()
        self.__create_everything()
        self.master.geometry("300x300")
        self.title.place(relx=0.5, rely=0.2, anchor='center')
        self.main_menu_label.place(relx=0.5, rely=0.4, anchor='center')
        self.start_button.place(relx=0.3, rely=0.7, anchor='center')
        self.gallery_button.place(relx=0.7, rely=0.7, anchor='center')
        self.close_button.place(relx=0.5, rely=0.85, anchor='center')
        self.master.configure(bg="#F4EDD3")
        self.current = -1

    def __view_gallery(self):
        self.music_player.music.stop()
        self.__destroy_everything()
        self.__create_everything()
        self.close_button.place(relx=0.85, rely=0.975, anchor='center')
        self.main_menu_button.place(relx=0.8, rely=0.975, anchor='e')
        self.master.geometry("604x635")
        for i in range(len(self.gallery_buttons)):
            self.gallery_buttons[i].place(relx=self.__get_x(i), rely=self.__get_y(i) / 600, anchor='sw')

        # TODO add scroll bar if more than 9 images... looks like it is not possible
        # It seems that I cannot have a clickable images with a scroll bar.
        # I can make a scroll bar of Tkinter.Text() objects which would be images, but not clickable.
        # Or I can make a scroll bar with Tkinter.ListBox() items which would be clickable, but not images.
        # can't find any other solution

        # scrollbar = Scrollbar(self.master)
        # scrollbar.pack(side=RIGHT, fill=Y)
        # mylist = Listbox(root, yscrollcommand=scrollbar.set)
        # for line in range(100):
        #     mylist.insert(END, "This is line number " + str(line))
        #
        # mylist.pack(side=LEFT, fill=BOTH)
        # scrollbar.config(command=mylist.yview)

    def __next(self):
        self.current += 1
        self.current_image.destroy()
        self.__update_buttons()
        self.__show_image(self.current)
        self.__play_sound(self.current)

    def __previous(self):
        self.current -= 1
        self.current_image.destroy()
        self.__update_buttons()
        self.__show_image(self.current)
        self.__play_sound(self.current)

    def __update_buttons(self):
        # first image
        if self.current == 0:
            self.previous_button.destroy()
            self.next_button.destroy()
            self.previous_button = Button(self.master, text="Previous", state="disabled", background="#4C98BF",
                                          height=2, width=10)
            self.previous_button.place(relx=0.0, rely=0.975, anchor='w')
            self.next_button = Button(self.master, text="Next", command=self.__next, background="#5BB4E2", height=2,
                                      width=10)
            self.next_button.place(relx=0.15, rely=0.975, anchor='w')

        # last image
        if self.current == len(self.images) - 1:
            self.previous_button.destroy()
            self.next_button.destroy()
            self.next_button = Button(self.master, text="Next", state="disabled",
                                      background="#5BB4E2", height=2, width=10)
            self.next_button.place(relx=0.15, rely=0.975, anchor='w')
            self.previous_button = Button(self.master, text="Previous", command=self.__previous, background="#5BB4E2",
                                          height=2, width=10)
            self.previous_button.place(relx=0.0, rely=0.975, anchor='w')

        # any other image
        if 0 < self.current < len(self.images) - 1:
            self.previous_button.destroy()
            self.next_button.destroy()
            self.next_button = Button(self.master, text="Next", command=self.__next, background="#5BB4E2", height=2,
                                      width=10)
            self.next_button.place(relx=0.15, rely=0.975, anchor='w')
            self.previous_button = Button(self.master, text="Previous", command=self.__previous, background="#5BB4E2",
                                          height=2, width=10)
            self.previous_button.place(relx=0, rely=0.975, anchor='w')

    def __close(self):
        self.master.quit()

    def __show_image(self, n):
        self.current_image = Label(image=self.images[n])
        self.current_image.place(relx=0.5, rely=0, anchor='n')

    def __play_sound(self, n):
        self.music_player.music.stop()

        if self.sounds[n] is None:
            return

        self.music_player.music.load(self.sounds[n])
        self.music_player.music.play(loops=0)

    @staticmethod
    def __get_y(n):
        res = 190
        for i in range(1, n + 1):
            if i % 3 == 0:
                res += 190
        return res

    @staticmethod
    def __get_x(n):
        x = 604 / 3
        return x * (n % 3) / 604

    @staticmethod
    def __make_image_and_sound_arrays(png_files, mp3_files, small_img):
        new_png_files = []
        new_mp3_files = []
        new_small_images = []
        for img in small_img:
            new_small_images.append(PhotoImage(file='media/smol/' + img))
        for img in png_files:
            mp3_name = img[0:-4] + '.mp3'
            new_png_files.append(PhotoImage(file='media/images/' + img))
            if mp3_name in mp3_files:
                new_mp3_files.append('media/sounds/' + mp3_name)
            else:
                new_mp3_files.append(None)
        return new_png_files, new_mp3_files, new_small_images

    def __destroy_everything(self):
        self.gallery_button.destroy()
        self.main_menu_button.destroy()
        self.previous_button.destroy()
        self.next_button.destroy()
        self.close_button.destroy()
        self.start_button.destroy()
        self.title.destroy()
        self.main_menu_label.destroy()
        self.current_image.destroy()
        for i in self.gallery_buttons:
            i.destroy()
            self.gallery_buttons = []

    def __create_everything(self):
        self.master.title("Photo Viewer App")
        self.music_player.init()
        self.start_button = Button(self.master, text="Slideshow", command=self.__start_from_beginning, height=2,
                                   width=8,
                                   background="#5BB4E2")
        self.gallery_button = Button(self.master, text="Gallery", command=self.__view_gallery, height=2, width=8,
                                     background="#FFD966")
        self.main_menu_button = Button(self.master, text="Main Menu", command=self.__main_menu, height=2, width=8,
                                       background="#C90076")
        self.close_button = Button(self.master, text="Close", command=self.__close, background="#C72027")
        self.previous_button = Button(self.master, text="Previous", command=self.__previous, background="#5BB4E2",
                                      state="disabled", height=5, width=10)
        self.next_button = Button(self.master, text="Next", command=self.__next, background="#5BB4E2", height=5,
                                  width=10)
        self.title = Label(text="Photo Album Viewer", font=("Times New Roman", 25))
        self.main_menu_label = Label(text="Main Menu", font=("Helvetica", 20))
        for i in range(len(self.small_images)):
            img_button = Button(self.master, image=self.small_images[i], command=partial(
                self.__start, i))
            self.gallery_buttons.append(img_button)


pics = []
tunes = []
smol_pics = []
for root, dirs, files in os.walk('media/images'):
    pics = files
for root, dirs, files in os.walk('media/sounds'):
    tunes = files
for root, dirs, files in os.walk('media/smol'):
    smol_pics = files

window = Tk()
PhotoViewer(window, pics, tunes, smol_pics)
window.mainloop()
