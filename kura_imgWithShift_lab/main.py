from random import randint
from tkinter import *
from tkinter import filedialog
from typing import List, Any

from PIL import Image, ImageTk

from module import *

from hammingCode import *


class App:
    def __init__(self):
        self.pixel_data=[]
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

        self.but = Button(self.frame, text="Кодирование", command=self.hamming_code)
        self.but.grid()

        self.but = Button(self.frame, text="Декодирование", command=self.hamming_decode)
        self.but.grid()

        self.root.mainloop()

    # Задание 1: вывод изображения
    def open_file(self):
        self.file_dir = filedialog.askopenfilename(title='select', filetypes=[("image", ".png"), ])
        self.image = Image.open(self.file_dir)
        self.photo = ImageTk.PhotoImage(self.image)
        self.c_image = self.canvas.create_image(0, 0, anchor='nw', image=self.photo)
        self.canvas.grid()

    # Задание 2: Побитовый шум

    def get_pixel(self):
        px = self.image.load()
        for i in range(201):
            for j in range(201):
                r = px[i, j][0]
                g = px[i, j][1]
                b = px[i, j][2]

                self.image.putpixel((i, j), randomError(r, g, b))

        self.photo = ImageTk.PhotoImage(self.image)
        self.c_image = self.canvas.create_image(0, 0, anchor='nw', image=self.photo)
        self.canvas.grid()
    # Задание 3.1 Кодирование изображения

    def hamming_code(self):
        px = self.image.load()
        for i in range(201):
            for j in range(201):
                r = encode(str(px[i, j][0]))
                g = encode(str(px[i, j][1]))
                b = encode(str(px[i, j][2]))

                self.image.putpixel((i, j), (int(r,2)%255,int(g,2)%255,int(b,2)%255))
                self.pixel_data.append([(r,g,b)])

        self.photo = ImageTk.PhotoImage(self.image)
        self.c_image = self.canvas.create_image(0, 0, anchor='nw', image=self.photo)
        self.canvas.grid()

    def hamming_decode(self):
        for i in range(201):
            for j in range(201):
                try:
                    r = decode(str(self.pixel_data[i*j][0]))
                    g = decode(str(self.pixel_data[i*j][1]))
                    b = decode(str(self.pixel_data[i*j][2]))

                    self.image.putpixel((i, j), (int(r), int(g), int(b)))
                except ValueError:
                    self.image = Image.open(self.file_dir)
                    self.photo = ImageTk.PhotoImage(self.image)
                    self.c_image = self.canvas.create_image(0, 0, anchor='nw', image=self.photo)
                    self.canvas.grid()
                    break
            break



        self.photo = ImageTk.PhotoImage(self.image)
        self.c_image = self.canvas.create_image(0, 0, anchor='nw', image=self.photo)
        self.canvas.grid()

app = App()
