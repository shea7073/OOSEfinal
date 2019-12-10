from tkinter import *



root = Tk()


label1 = Label()
label2 = Label()
label3 = Label(text="Please enter the highest weight")
label4 = Label()

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



button1 = Button(text="calculate kilos to pounds", command=kilo2pound)

button2 = Button(text="calculate 1 rep max", command=algorithm)

button3 = Button(text="calculate pounds to kilos", command=pound2kilo)

e1 = Entry(root)
e2 = Entry(root)
e3 = Entry(root)
e4 = Entry(root)




e1.grid(row=0)
button1.grid(row=1)
label1.grid(row=2)
label3.grid(row=3)
e2.grid(row=4)
e3.grid(row=5)
button2.grid(row=6)
label4.grid(row=7)
e4.grid(row=8)
button3.grid(row=9)
label2.grid(row=10)




root.mainloop()