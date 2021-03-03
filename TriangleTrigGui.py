from tkinter import *

root = Tk()
root.geometry('230x150')
root.title("Triangle Trig")

toggle = IntVar()


def selection():
    if toggle == 1:
        triangleArea()
    elif toggle == 2:
        lawOfSines()


def triangleArea():
    window = Toplevel()
    window.geometry('200x200')
    window.title("Area of a Triangle")


def lawOfSines():
    window = Toplevel()
    window.geometry('200x200')
    window.title("Law of Sines")


# Initializes all of the radio buttons
triangleAreaRadioButton = Radiobutton(root , text="Area of a Triangle" , value=1 , variable=toggle, command=selection())
triangleAreaRadioButton.pack(anchor=W)
lawOfSinesRadioButton = Radiobutton(root , text="Law of Sines" , value=2 , variable=toggle)
lawOfSinesRadioButton.pack(anchor=W)
lawOfCosinesRadioButton = Radiobutton(root , text="Law of Cosines" , value=3 , variable=toggle)
lawOfCosinesRadioButton.pack(anchor=W)

selectButton = Button(root, text="Select", command=selection())
selectButton.pack()


root.mainloop()
