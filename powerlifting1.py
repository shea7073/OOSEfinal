from tkinter import *
from typing import Any, Union
import Plates

#Sean Shea, Dan Kotlinski, Harsh Shastri



root = Tk()
root.title("Powerlifters Toolkit")

label1 = Label()
label2 = Label()
label3 = Label(text="Please enter the highest weight")
label4 = Label()
label5 = Label(text="Please the reps you completed")
label6 = Label(text="Please enter KG for plate diagram")
label7 = Label()
label8 = Label(text="Please enter your gender, bodyweight, and weight lifted in KG")
label9 = Label()
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
collars = Label(text="Don't forget your collars (2.5 KG EACH)")

def calcWilks():

    gender = e6.get()
    gender = str(gender)
    bodyweight = e7.get()
    bodyweight = float(bodyweight)
    weightLifted = e8.get()
    weightLifted = float(weightLifted)

    if gender == "male":
        a = -216.0475144
        b = 16.2606339
        c = -0.002388645
        d = -0.00113732
        e = 7.01863E-06
        f = -1.291E-08
        score = weightLifted * 500.000000 / (a + b * bodyweight + c * bodyweight ** 2.00000 + d * bodyweight ** 3.00000 + e * bodyweight ** 4.00000 + f * bodyweight ** 5.000000)
        label9.configure(text=str(score))


    elif gender == "female":
        a = 594.31747775582
        b = -27.23842536447
        c = 0.82112226871
        d = -0.00930733913
        e = 4.731582E-05
        f = -9.054E-08
        score = weightLifted * 500 / (a + b * bodyweight + c * bodyweight ** 2 + d * bodyweight ** 3 + e * bodyweight ** 4 + f * bodyweight ** 5)
        label9.configure(text=str(score))



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

    reds = 0
    blues = 0
    yellows = 0
    greens = 0
    whites = 0
    blacks = 0
    silvers = 0
    collar = 2.5*2
    array = [0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00]
    numPlates = 0
    bar = 20
    weight = e5.get()
    weight = float(weight)
    weight = weight-collar-bar
    weight = weight/2

    while weight >= 25:
        weight = weight-25
        reds += 1
        numPlates += 1
        array[numPlates-1] = 25
    while weight >= 20 :
        weight = weight-20
        blues += 1
        numPlates += 1
        array[numPlates-1] = 20
    while weight >= 15:
        weight = weight-15
        yellows += 1
        numPlates += 1
        array[numPlates - 1] = 15
    while weight >= 10:
        weight = weight-10
        greens += 1
        numPlates += 1
        array[numPlates - 1] = 10
    while weight >= 5:
        weight = weight - 5
        whites += 1
        numPlates += 1
        array[numPlates - 1] = 5
    while weight >= 2.5 :
        weight = weight - 2.5
        blacks += 1
        numPlates += 1
        array[numPlates - 1] = 2.5
    while weight >= 1.25:
        weight = weight - 1.25
        silvers += 1
        numPlates += 1
        array[numPlates - 1] = 1.25

    remainder = weight

    label7.configure(text=str(remainder))

    for i in array :
        plate1.configure(text=str(array[0]))
        plate2.configure(text=str(array[1]))
        plate3.configure(text=str(array[2]))
        plate4.configure(text=str(array[3]))
        plate5.configure(text=str(array[4]))
        plate6.configure(text=str(array[5]))
        plate7.configure(text=str(array[6]))
        plate8.configure(text=str(array[7]))
        plate9.configure(text=str(array[8]))
        plate10.configure(text=str(array[9]))
        plate11.configure(text=str(array[10]))

    if array[0] == 25:
        plate1.configure(background='red')
    elif array[0] == 20:
        plate1.configure(background='blue')
    elif array[0] == 15:
        plate1.configure(background='yellow')
    elif array[0] == 10:
        plate1.configure(background='green')
    elif array[0] == 5:
        plate1.configure(background='white')
    elif array[0] == 2.5:
        plate1.configure(background='black',foreground='white')
    elif array[0] == 1.25:
        plate1.configure(background='grey')
    else:
        print("error")

    if array[1] == 25:
        plate2.configure(background='red')
    elif array[1] == 20:
        plate2.configure(background='blue')
    elif array[1] == 15:
        plate2.configure(background='yellow')
    elif array[1] == 10:
        plate2.configure(background='green')
    elif array[1] == 5:
        plate2.configure(background='white')
    elif array[1] == 2.5:
        plate2.configure(background='black',foreground='white')
    elif array[1] == 1.25:
        plate2.configure(background='grey')
    else:
        print("error")

    if array[2] == 25:
        plate3.configure(background='red')
    elif array[2] == 20:
        plate3.configure(background='blue')
    elif array[2] == 15:
        plate3.configure(background='yellow')
    elif array[2] == 10:
        plate3.configure(background='green')
    elif array[2] == 5:
        plate3.configure(background='white')
    elif array[2] == 2.5:
        plate3.configure(background='black',foreground='white')
    elif array[2] == 1.25:
        plate3.configure(background='grey')
    else:
        print("error")

    if array[3] == 25:
        plate4.configure(background='red')
    elif array[3] == 20:
        plate4.configure(background='blue')
    elif array[3] == 15:
        plate4.configure(background='yellow')
    elif array[3] == 10:
        plate4.configure(background='green')
    elif array[3] == 5:
        plate4.configure(background='white')
    elif array[3] == 2.5:
        plate4.configure(background='black',foreground='white')
    elif array[3] == 1.25:
        plate4.configure(background='grey')
    else:
        print("error")

    if array[4] == 25:
        plate5.configure(background='red')
    elif array[4] == 20:
        plate5.configure(background='blue')
    elif array[4] == 15:
        plate5.configure(background='yellow')
    elif array[4] == 10:
        plate5.configure(background='green')
    elif array[4] == 5:
        plate5.configure(background='white')
    elif array[4] == 2.5:
        plate5.configure(background='black',foreground='white')
    elif array[4] == 1.25:
        plate5.configure(background='grey')
    else:
        print("error")

    if array[5] == 25:
        plate6.configure(background='red')
    elif array[5] == 20:
        plate6.configure(background='blue')
    elif array[5] == 15:
        plate6.configure(background='yellow')
    elif array[5] == 10:
        plate6.configure(background='green')
    elif array[5] == 5:
        plate6.configure(background='white')
    elif array[5] == 2.5:
        plate6.configure(background='black',foreground='white')
    elif array[5] == 1.25:
        plate6.configure(background='grey')
    else:
        print("error")

    if array[6] == 25:
        plate7.configure(background='red')
    elif array[6] == 20:
        plate7.configure(background='blue')
    elif array[6] == 15:
        plate7.configure(background='yellow')
    elif array[6] == 10:
        plate7.configure(background='green')
    elif array[6] == 5:
        plate7.configure(background='white')
    elif array[6] == 2.5:
        plate7.configure(background='black',foreground='white')
    elif array[6] == 1.25:
        plate7.configure(background='grey')
    else:
        print("error")

    if array[7] == 25:
        plate8.configure(background='red')
    elif array[7] == 20:
        plate8.configure(background='blue')
    elif array[7] == 15:
        plate8.configure(background='yellow')
    elif array[7] == 10:
        plate8.configure(background='green')
    elif array[7] == 5:
        plate8.configure(background='white')
    elif array[7] == 2.5:
        plate8.configure(background='black',foreground='white')
    elif array[7] == 1.25:
        plate8.configure(background='grey')
    else:
        print("error")

    if array[8] == 25:
        plate9.configure(background='red')
    elif array[8] == 20:
        plate9.configure(background='blue')
    elif array[8] == 15:
        plate9.configure(background='yellow')
    elif array[8] == 10:
        plate9.configure(background='green')
    elif array[8] == 5:
        plate9.configure(background='white')
    elif array[8] == 2.5:
        plate9.configure(background='black',foreground='white')
    elif array[8] == 1.25:
        plate9.configure(background='grey')
    else:
        print("error")

    if array[9] == 25:
        plate10.configure(background='red')
    elif array[9] == 20:
        plate10.configure(background='blue')
    elif array[9] == 15:
        plate10.configure(background='yellow')
    elif array[9] == 10:
        plate10.configure(background='green')
    elif array[9] == 5:
        plate10.configure(background='white')
    elif array[9] == 2.5:
        plate10.configure(background='black',foreground='white')
    elif array[9] == 1.25:
        plate10.configure(background='grey')
    else:
        print("error")

    if array[10] == 25:
        plate11.configure(background='red')
    elif array[10] == 20:
        plate11.configure(background='blue')
    elif array[10] == 15:
        plate11.configure(background='yellow')
    elif array[10] == 10:
        plate11.configure(background='green')
    elif array[10] == 5:
        plate11.configure(background='white')
    elif array[10] == 2.5:
        plate11.configure(background='black',foreground='white')
    elif array[10] == 1.25:
        plate11.configure(background='grey')
    else:
        print("error")


button1 = Button(text="calculate kilos to pounds", command=kilo2pound)

button2 = Button(text="calculate 1 rep max", command=algorithm)

button3 = Button(text="calculate pounds to kilos", command=pound2kilo)

button4 = Button(text="Show plates for my weight", command=platesCalc)

button5 = Button(text="Calculate Wilks", command=calcWilks)

e1 = Entry(root)
e2 = Entry(root)
e3 = Entry(root)
e4 = Entry(root)
e5 = Entry(root)
e6 = Entry(root)
e7 = Entry(root)
e8 = Entry(root)




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
label6.configure(background='sky blue')
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

label8.grid(row=15)
e6.grid(row=16)
e7.grid(row=17)
e8.grid(row=18)
button5.grid(row=19)
label9.grid(row=20)




root.configure(background='sky blue')
root.geometry("800x800+800+800")


root.mainloop()
