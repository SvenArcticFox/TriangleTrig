from tkinter import *
from tkinter.ttk import *
from tkinter.messagebox import *
import math

# Initializes everything for the main window except for buttons
root = Tk()
root.title("Triangle Trig")
root.minsize(240, 125)
root.maxsize(240, 125)


def triangleArea():
    window = Toplevel(root)
    window.minsize(290 , 230)
    window.maxsize(290 , 230)
    window.title("Area of a Triangle")

    # Initializes everything for side A
    sideALabel = Label(window , text = "Side A:" , borderwidth = 5 , font = ("Arial" , 10))
    sideALabel.grid(row = 0 , column = 0 , padx = 10 , pady = 7)
    sideAText = Text(window , height = 1 , width = 25 , font = ("Arial", 10))
    sideAText.grid(row = 0, column = 1 , padx = 2 , pady = 7)

    # Initializes everything for side B
    sideBLabel = Label(window , text = "Side B:" , borderwidth = 2 , font = ("Arial" , 10))
    sideBLabel.grid(row = 1 , column = 0 , padx = 10 , pady = 7)
    sideBText = Text(window , height = 1 , width = 25 , font = ("Arial" , 10))
    sideBText.grid(row = 1 , column = 1 , padx = 2 , pady = 7)

    # Initializes everything for angle C
    angleCLabel = Label(window , text = "Angle C:" , borderwidth = 2 , font = ("Arial" , 10))
    angleCLabel.grid(row = 2 , column = 0 , padx = 10 , pady = 7)
    angleCText = Text(window , height = 1 , width = 25 , font = ("Arial" , 10))
    angleCText.grid(row = 2 , column = 1 , padx = 2 , pady = 7)

    # Initializes everything for the area label
    areaLabel = Label(window , font = ("Arial" , 12))
    areaLabel.grid(row = 5 , pady = 10 , padx = 10 , sticky = N , columnspan = 4)

    # Label that tells users that angle measurements are in degrees.
    degreeLabel = Label(window , text = "All angle measurements are in degrees." , font = ("Arial" , 10))
    degreeLabel.grid(row = 3 , pady = 10 , padx = 10 , sticky = N , columnspan = 4)

    # Calculates the actual area of the triangle
    def calculate():
        try:
            sideA = float(sideAText.get(1.0 , 'end-1c'))
            sideB = float(sideBText.get(1.0, 'end-1c'))
            angleC = float(angleCText.get(1.0, 'end-1c'))

            area = 0.5 * sideA * sideB * math.sin(math.radians(angleC))
            areaLabel.config(text = "The area is " + str(area))

        except ValueError:
            showerror("Invalid Number" , "Make sure all numbers are valid!")

    # Initializes everything for the calculate button
    calculate = Button(window , text = "Calculate" , command = calculate)
    calculate.grid(row = 4 , pady = 10 , padx = 10 , sticky = N, columnspan = 5)


def lawOfSines():
    toggle = float()
    window = Toplevel(root)
    window.minsize(290 , 205)
    window.title("Law of Sines")

    # Initializes the radio buttons
    angleRadioButton = Radiobutton(window , text = "Calculate an Angle" , value = 1 , variable = toggle)
    angleRadioButton.grid(column = 0 , row = 0 , padx = 10 , pady = 10)
    sideRadioButton = Radiobutton(window , text = "Calculate a Side" , value = 2 , variable = toggle)
    sideRadioButton.grid(row = 0 , column = 1 , padx = 5 , pady = 10)


def lawOfCosines():
    window = Toplevel(root)
    window.geometry('200x200')
    window.title("Law of Cosines")


# Initializes all of the buttons
triangleAreaButton = Button(root, text="Area of a Triangle", command=triangleArea)
triangleAreaButton.pack(pady=7, padx=7)
lawOfSinesButton = Button(root, text="Law of Sines", command=lawOfSines)
lawOfSinesButton.pack(pady=7, padx=7)
lawOfCosinesButton = Button(root, text="Law of Cosines", command=lawOfCosines)
lawOfCosinesButton.pack(pady=7, padx=7)

root.mainloop()
