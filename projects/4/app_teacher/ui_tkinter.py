from tkinter import *

value = 0


def calc():
    global value

    print(f'chk_value: {chk_value.get()}')
    print(f'entr_value: {entr_value.get()}')

    if chk_value.get():
        str1 = entr_value.get()
        if str(str1).isdigit():
            value += int(str1)
            lbl.config(text=value)
        else:
            lbl.config(text="Вы ввели некорректное значение!")
    print('press')


window = Tk()
window.title("Welcome to LikeGeeks app")
window.geometry('350x200')

lbl = Label(window, text="Hello")
lbl.grid(column=0, row=0)

btn = Button(window, text="Click Me", command=calc)  # тут нужна ссылка на функцию (имя функции)
btn.grid(column=0, row=1)

entr_value = StringVar(value='1')
entr = Entry(textvariable=entr_value, )
entr.grid(column=1, row=0)

chk_value = IntVar()
chk = Checkbutton(text="Добавлять/не добавлять", variable=chk_value)
chk.grid(column=1, row=1)

window.mainloop()
