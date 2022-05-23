from random import randint
from tkinter import *
from tkinter import filedialog

from PIL import Image, ImageTk


class App:
    def __init__(self):
        self.file_dir = None

        self.root = Tk()

        self.frame = Frame(self.root)
        self.frame.grid()

        self.image = Image.open("null.png")
        self.photo = ImageTk.PhotoImage(self.image)

        self.but = Button(self.frame, text="Открыть", command=self.open_file)
        self.but.grid()

        self.canvas = Canvas(self.root, height=200, width=200)
        self.c_image = self.canvas.create_image(0, 0, anchor='nw', image=self.photo)
        self.canvas.grid()

        self.but = Button(self.frame, text="Шум", command=self.get_pixel)
        self.but.grid()

        self.root.mainloop()

    def open_file(self):
        self.file_dir = filedialog.askopenfilename(title='select', filetypes=[("image", ".png"), ])
        self.image = Image.open(self.file_dir)
        self.photo = ImageTk.PhotoImage(self.image)
        self.c_image = self.canvas.create_image(0, 0, anchor='nw', image=self.photo)
        self.canvas.grid()

    def get_pixel(self):
        for i in range(201):
            for j in range(201):
                self.image.putpixel((i, j), (randint(0, 255), randint(0, 255), randint(0, 255)))

        self.photo = ImageTk.PhotoImage(self.image)
        self.c_image = self.canvas.create_image(0, 0, anchor='nw', image=self.photo)
        self.canvas.grid()


app = App()
