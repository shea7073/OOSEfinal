from tkinter import *



root = Tk()

def kilo2pound():
    a = e1.get()
    a = float(a)
    a = a*2.2046226218
    print(a)

def pound2kilo():
    b = e4.get()
    b = float(b)
    b = b/2.2046226218
    label = Label(text=b)

button1 = Button(text="calculate kilos to pounds", command=kilo2pound,)
button2 = Button(text="calculate wilks score")
button3 = Button(text="calculate 1 rep max")
button4 = Button(text="calculate pounds to kilos", command=pound2kilo)


e1 = Entry(root)
e2 = Entry(root)
e3 = Entry(root)
e4 = Entry(root)

e1.grid(row=0)
button1.grid(row=1)
e2.grid(row=2)
button2.grid(row=3)
e3.grid(row=4)
button3.grid(row=5)
e4.grid(row=6)
button4.grid(row=7)

root.mainloop()