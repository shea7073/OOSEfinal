from tkinter import *
from typing import Any, Union
import Plates





root = Tk()
root.title("Powerlifters Toolkit")

label1 = Label()
label2 = Label()
label3 = Label(text="Please enter the highest weight")
label4 = Label()
label5 = Label(text="Please the reps you completed")
label6 = Label(text="Please enter KG for plate diagram")
label7 = Label()
plate1 = Label()
plate2 = Label()
plate3 = Label()
plate4= Label()
plate5 = Label()
plate6 = Label()
plate7 = Label()
plate8 = Label()
plate9 = Label()
plate10 = Label()
plate11 = Label()
collars = Label(text="Don't forget your collars (2.5 KG)")

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


def platesCalc():

    weight = e5.get()
    weight = float(weight)
    reds = 0
    blues = 0
    yellows = 0
    greens = 0
    whites = 0
    blacks = 0
    silvers = 0
    collar = 2.5
    bar = 20
    weight = weight-collar-bar

    while weight >= 25:
        weight = weight-25
        reds += 1
    while weight >= 20 :
        weight = weight-20
        blues += 1
    while weight >= 15 :
        weight = weight-15
        yellows += 1
    while weight >= 10:
        weight = weight-10
        greens += 1
    while weight >= 5:
        weight = weight - 5
        whites += 1
    while weight >= 2.5 :
        weight = weight - 2.5
        blacks += 1
    while weight >= 1.25:
        weight = weight - 1.25
        silvers += 1

    remainder = weight

    label7.configure(text=str(remainder))

button1 = Button(text="calculate kilos to pounds", command=kilo2pound)

button2 = Button(text="calculate 1 rep max", command=algorithm)

button3 = Button(text="calculate pounds to kilos", command=pound2kilo)

button4 = Button(text="Show plates for my weight", command=platesCalc)

e1 = Entry(root)
e2 = Entry(root)
e3 = Entry(root)
e4 = Entry(root)
e5 = Entry(root)




e1.grid(row=0)
button1.grid(row=1)
button1.configure(background='red')
label1.grid(row=2)
label1.configure(background='sky blue')
label3.grid(row=3)
label3.configure(background='sky blue')
e2.grid(row=4)
e3.grid(row=5)
button2.grid(row=6)
button2.configure(background='red')
label4.grid(row=7)
label4.configure(background='sky blue')
e4.grid(row=8)
button3.grid(row=9)
button3.configure(background='red')
label2.grid(row=10)
label2.configure(background='sky blue')
label6.grid(row=11)
e5.grid(row=12)
button4.grid(row=13)
label7.grid(row=14)
label7.configure(background='sky blue')

plate1.grid(row=2,column=20)
plate2.grid(row=3,column=20)
plate3.grid(row=4,column=20)
plate4.grid(row=5,column=20)
plate5.grid(row=6,column=20)
plate6.grid(row=7,column=20)
plate7.grid(row=8,column=20)
plate8.grid(row=9,column=20)
plate9.grid(row=10,column=20)
plate10.grid(row=11,column=20)
plate11.grid(row=12,column=20)
collars.grid(row=13, column=20)

root.configure(background='sky blue')
root.geometry("600x400+400+400")


root.mainloop()
