import random
from tkinter import *
from random import *

f = 0
cl = ["blue",'red','cyan','grey','pink','purple']

def button_1():
    global f
    f+=1
    if f == 1:
      canvas.delete("all")
      f = 0
    else:
        pass
    h = randint(1,3)
    if h == 1:
        p = cl[randint(0, 5)]

        B.config(text=p+" polygon")
        canvas.create_polygon(randint(0, 500), randint(0, 500), randint(0, 500), randint(0, 500),randint(0, 500),randint(0, 500), fill = p,outline="black")
    elif h == 2:
        p = cl[randint(0, 5)]
        B.config(text=p+" rectangle")
        canvas.create_rectangle(randint(0, 500),randint(0, 500),randint(0, 500),randint(0, 500),fill = p )
    else:
        p = cl[randint(0, 5)]
        canvas.create_oval(randint(0, 500),randint(0, 500),randint(0, 500),randint(0, 500), fill = p)
        B.config(text=p+" oval")



root=Tk()
root.title('Приложение')
root.geometry('500x575')

canvas = Canvas(root, width=500, height=500)
canvas.pack()

A = Button(root, text='Сгенерировать', width=11, height=2, bg='white', command=button_1)
A.pack()

B = Label(root, text="", font="Calibri 18")
B.pack()

root.mainloop()