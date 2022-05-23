from tkinter import *
from module import *


# Функции
def new_sum():
    NewSum = Toplevel(window)
    enter_sum = Label(NewSum, text="Укажите сумматор:")
    enter_sum.grid(column=0, row=0)

    sum1 = IntVar()
    sum2 = IntVar()
    sum3 = IntVar()

    check1 = Checkbutton(NewSum, variable=sum1, onvalue="1", offvalue="")
    check2 = Checkbutton(NewSum, variable=sum2, onvalue="2", offvalue="")
    check3 = Checkbutton(NewSum, variable=sum3, onvalue="3", offvalue="")

    check1.grid(column=1, row=0)
    check2.grid(column=2, row=0)
    check3.grid(column=3, row=0)

    btn = Button(NewSum, text="Добавить", command=lambda: (add_sum(sum1, sum2, sum3)))
    btn.grid(column=0, row=1)

    def add_sum(s1, s2, s3):
        global sumators
        NewSum.destroy()
        sumators_num = (str(s1.get()) + str(s2.get()) + str(s3.get())).replace('0', '')

        if len(sumators_num) < 2:
            return 0

        sumators.append(sumators_num)
        res = sumators
        sumators_count.configure(text=res)


def coded():
    global shift_code

    txt = coded_enter.get()
    res = coding(txt, sumators)
    code_text.configure(text="Закодированое сообщение:{}".format(res))
    shift_code = res


def decode():
    res = encoding(shift_code, sumators)
    decode_text.configure(text='Дешифрованое сообщение:{}'.format(res))


# Графика

sumators = []
shift_code = ''

window = Tk()
window.title("Сверточное кодирование")
window.geometry('400x250')

lbl = Label(window, text="Добавить сумматор")
lbl.place(x=0, y=0)

btn_plus = Button(window, text="+", command=new_sum)
btn_plus.place(x=120)

sumators_lbl = Label(window, text='Сумматоры:')
sumators_lbl.place(y=25)

sumators_count = Label(window, text="{}")
sumators_count.place(x=71, y=25)

coded_text = Label(window, text="Введите сообщение:")
coded_text.place(y=50)

coded_enter = Entry(window, width=10)
coded_enter.place(x=120, y=50)

btn_enter = Button(window, text='Закодировать', command=coded)
btn_enter.place(x=187, y=45)

code_text = Label(window, text="Закодированое сообщение:")
code_text.place(y=75)

btn_decode = Button(window, text="Дешифровать", command=decode)
btn_decode.place(y=100)

decode_text = Label(window, text='Дешифрованое сообщение:')
decode_text.place(y=140)

window.mainloop()
