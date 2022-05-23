from tkinter import *
from tkinter import messagebox
from module import *


def click():
    res = txt.get()
    m = int(txt1.get())
    if '/' in res:
        res_new=with_mod(res,m)
        temp = int(without_mod(res_new))
        if temp >= m:
            otvet = temp % m
        else:
            messagebox.showinfo('Ошибка', " MOD больше выражения")

    else:
        temp = int(without_mod(res))
        if temp>=m:
            otvet=temp%m
        else:
            messagebox.showinfo('Ошибка', " MOD больше выражения")


    lbl1.configure(text="Ответ: " + str(otvet))



window = Tk()
window.geometry('400x250')

lbl = Label(window, text="Введите пример:")
lbl.grid(column=0, row=0)

txt = Entry(window, width=10)
txt.grid(column=1, row=0)
txt.focus()

lbl = Label(window, text="Mod:")
lbl.grid(column=0, row=1)

txt1 = Entry(window, width=10)
txt1.grid(column=1, row=1)

btn = Button(window, text='Посчитать', command=click,padx=5)
btn.grid(column=2, row=1)

lbl1 = Label(window, text="Ответ:")
lbl1.grid(column=0, row=2)

window.mainloop()
