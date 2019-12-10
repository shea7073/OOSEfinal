from tkinter import *


root = Tk()
root.title('Weight Lifting Converter')
root.geometry('400x400')

label1 = Label()
label2 = Label()
label3 = Label(text="Weight Lifted")
label4 = Label()
label15 = Label(text="Reps Completed")


def kilo2pound():
    a = e1.get()
    a = float(a)
    a = a*2.2046226218
    label1.configure(text=str(a))


def pound2kilo():
    b = e4.get()
    b = float(b)
    b = b/2.2046226218
    label2.configure(text=str(b))


def algorithm():

    weight = e2.get()
    weight = float(weight)
    reps = e3.get()
    reps = float(reps)

    if weight <= 0 or reps <= 0:
        print("Error")

    else:
        orm = weight * (1 + (reps / 40))
        label4.configure(text=str(orm))


button1 = Button(text="Calculate Kilograms to Pounds", command=kilo2pound)

button2 = Button(text="Calculate 1 rep max", command=algorithm)

button3 = Button(text="Calculate Pounds to Kilos", command=pound2kilo)

e1 = Entry(root)
e2 = Entry(root)
e3 = Entry(root)
e4 = Entry(root)


e1.grid(row=0)
button1.grid(row=1)
label1.grid(row=2)
label3.grid(row=3)
e2.grid(row=4)
label15.grid(row=5)
e3.grid(row=6)
button2.grid(row=7)
label4.grid(row=8)
e4.grid(row=9)
button3.grid(row=10)
label2.grid(row=11)


root.mainloop()
