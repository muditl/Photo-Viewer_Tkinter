from tkinter import *


class PhotoViewer:
    def __init__(self, root):
        self.root = root
        self.root.title("Photo Viewer App")
        self.root.geometry("300x300")
        self.root.configure(bg="#F4EDD3")

        img1 = PhotoImage(file='images/image1.png')
        img2 = PhotoImage(file='images/image2.png')
        img3 = PhotoImage(file='images/image3.png')
        img4 = PhotoImage(file='images/image4.png')
        self.images = [img1, img2, img3, img4]

        self.title = Label(text="Photo Album Viewer", font=("Times New Roman", 25))
        self.title.place(relx=0.5, rely=0.2, anchor='center')

        self.main_menu_label = Label(text="Main Menu", font=("Helvetica", 20))
        self.main_menu_label.place(relx=0.5, rely=0.4, anchor='center')

        self.start_button = Button(root, text="Start", command=self.start_from_beginning, height=2, width=8,
                                   background="#5BB4E2")
        self.start_button.place(relx=0.5, rely=0.7, anchor='center')

        self.close_button = Button(root, text="Close", command=self.close, background="#C72027")
        self.close_button.place(relx=0.5, rely=0.85, anchor='center')

        self.previous_button = Button(root, text="Previous", command=self.previous, background="#5BB4E2",
                                      state="disabled")
        self.next_button = Button(root, text="Next", command=self.next, background="#5BB4E2")

        self.current = -1

    def start_from_beginning(self):
        self.start(0)

    def start(self, current):
        self.current = current
        self.root.geometry("604x650")
        self.start_button.destroy()
        self.title.destroy()
        self.main_menu_label.destroy()
        self.close_button.place(relx=0.5, rely=0.975, anchor='center')
        self.previous_button.place(relx=0.2, rely=0.975, anchor='center')
        self.next_button.place(relx=0.8, rely=0.975, anchor='center')
        self.show_image(0)

    def next(self):
        self.current += 1
        if self.current == 3:
            self.next_button = Button(self.root, text="Next", state="disabled", background="#4C98BF")
            self.next_button.place(relx=0.8, rely=0.975, anchor='center')
        self.previous_button = Button(self.root, text="Previous", command=self.previous, background="#5BB4E2")
        self.previous_button.place(relx=0.2, rely=0.975, anchor='center')
        self.show_image(self.current)

    def previous(self):
        self.current -= 1
        if self.current == 0:
            self.previous_button = Button(self.root, text="Previous", state="disabled", background="#4C98BF")
            self.previous_button.place(relx=0.2, rely=0.975, anchor='center')
        self.next_button = Button(self.root, text="Next", command=self.next, background="#5BB4E2")
        self.next_button.place(relx=0.8, rely=0.975, anchor='center')
        self.show_image(self.current)

    def close(self):
        self.root.quit()

    def show_image(self, n):
        i = Label(image=self.images[n])
        i.place(relx=0, rely=0, anchor='nw')


master = Tk()
PhotoViewer(master)
master.mainloop()
