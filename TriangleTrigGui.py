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
    toggle = IntVar()
    angleRadioButton = Radiobutton(window , text = "Calculate an Angle" , value = 1 , variable = toggle)
    angleRadioButton.grid(column = 0 , row = 0 , padx = 10 , pady = 10)
    sideRadioButton = Radiobutton(window , text = "Calculate a Side" , value = 2 , variable = toggle)
    sideRadioButton.grid(row = 0 , column = 1 , padx = 5 , pady = 10)

    # Initializes everything for angle A
    angleALabel = Label(window , text = "Angle A:" , borderwidth = 5 , font = ("Arial" , 10))
    angleALabel.grid(row = 1 , column = 0 , padx = 10 , pady = 7)
    angleAText = Text(window , height = 1 , width = 25 , font = ("Arial", 10))
    angleAText.grid(row = 1, column = 1 , padx = 2 , pady = 7)

    # Initializes everything for side A
    sideALabel = Label(window , text = "Side A:" , borderwidth = 5 , font = ("Arial" , 10))
    sideALabel.grid(row = 2 , column = 0 , padx = 10 , pady = 7)
    sideAText = Text(window , height = 1 , width = 25 , font = ("Arial", 10))
    sideAText.grid(row = 2, column = 1 , padx = 2 , pady = 7)

    # Initializes everything for side B
    sideOrAngleBLabel = Label(window , text = "Side/Angle B:" , borderwidth = 2 , font = ("Arial" , 10))
    sideOrAngleBLabel.grid(row = 3 , column = 0 , padx = 10 , pady = 7)
    sideOrAngleBText = Text(window , height = 1 , width = 25 , font = ("Arial" , 10))
    sideOrAngleBText.grid(row = 3 , column = 1 , padx = 2 , pady = 7)

    # Label that tells users that angle measurements are in degrees.
    degreeLabel = Label(window , text = "All angle measurements are in degrees." , font = ("Arial" , 10))
    degreeLabel.grid(row = 4 , pady = 10 , padx = 10 , sticky = N , columnspan = 4)

    # Label that tells the user what side/angle B means
    bMeaningLabel = Label(window , text = "Side B is used when calculating an angle. "
                                          "Angle B is used when calculating a side."
                          , font = ("Arial" , 10))
    bMeaningLabel.grid(row = 5 , pady = 10 , padx = 10 , sticky = N , columnspan = 4)

    # Initializes everything for the answer label
    answerLabel = Label(window , font = ("Arial" , 12))
    answerLabel.grid(row = 7 , pady = 10 , padx = 10 , sticky = N , columnspan = 4)

    def calculate():

        # Calculates the angle of a triangle using the law of sins
        def calculateAngle():
            try:
                angleA = float(angleAText.get(1.0, 'end-1c'))
                sideA = float(sideAText.get(1.0, 'end-1c'))
                sideB = float(sideOrAngleBText.get(1.0, 'end-1c'))

                sinB = (sideB * math.sin(math.radians(angleA))) / sideA
                if sinB > 1 or sinB < 0:
                    answerLabel.config(text = "There are no possible angles that will work in this triangle.")
                else:
                    angleB = math.degrees(math.asin(sinB))
                    angleB2 = 180 - angleB
                    answerLabel.config(text = "Angle B is " + str(angleB) + " or " + str(angleB2) + ".")
            except ValueError:
                showerror("Invalid Number", "Make sure all numbers are valid!")

        # Calculates the side of a triangle using the law of sins
        def calculateSide():
            try:
                angleA = float(angleAText.get(1.0, 'end-1c'))
                sideA = float(sideAText.get(1.0, 'end-1c'))
                angleB = float(sideOrAngleBText.get(1.0, 'end-1c'))

                sideB = (sideA * math.sin(math.radians(angleB))) / math.sin(math.radians(angleA))
                answerLabel.config(text = "Side B is " + str(sideB) + ".")
            except ValueError:
                showerror("Invalid Number", "Make sure all numbers are valid!")

        if toggle.get() == 1:
            calculateAngle()
        elif toggle.get() == 2:
            calculateSide()

    # Initializes everything for the calculate button
    calculate = Button(window , text = "Calculate" , command = calculate)
    calculate.grid(row = 6 , pady = 10 , padx = 10 , sticky = N, columnspan = 5)

def lawOfCosines():
    window = Toplevel(root)
    window.minsize(290 , 205)
    window.title("Law of Cosines")

    # Initializes the radio buttons and toggle variable
    toggle = IntVar()
    angleRadioButton = Radiobutton(window , text = "Calculate an Angle" , value = 1 , variable = toggle)
    angleRadioButton.grid(column = 0 , row = 0 , padx = 10 , pady = 10)
    sideRadioButton = Radiobutton(window , text = "Calculate a Side" , value = 2 , variable = toggle)
    sideRadioButton.grid(row = 0 , column = 1 , padx = 5 , pady = 10)

    # Initializes everything for side A
    sideALabel = Label(window , text = "Side A:" , borderwidth = 5 , font = ("Arial" , 10))
    sideALabel.grid(row = 1 , column = 0 , padx = 10 , pady = 7)
    sideAText = Text(window , height = 1 , width = 25 , font = ("Arial", 10))
    sideAText.grid(row = 1, column = 1 , padx = 2 , pady = 7)

    # Initializes everything for side A
    sideBLabel = Label(window , text = "Angle B:" , borderwidth = 5 , font = ("Arial" , 10))
    sideBLabel.grid(row = 2 , column = 0 , padx = 10 , pady = 7)
    sideBText = Text(window , height = 1 , width = 25 , font = ("Arial", 10))
    sideBText.grid(row = 2, column = 1 , padx = 2 , pady = 7)

    # Initializes everything for side B
    sideOrAngleCLabel = Label(window , text = "Side/Angle C:" , borderwidth = 2 , font = ("Arial" , 10))
    sideOrAngleCLabel.grid(row = 3 , column = 0 , padx = 10 , pady = 7)
    sideOrAngleCText = Text(window , height = 1 , width = 25 , font = ("Arial" , 10))
    sideOrAngleCText.grid(row = 3 , column = 1 , padx = 2 , pady = 7)

    # Label that tells users that angle measurements are in degrees.
    degreeLabel = Label(window , text = "All angle measurements are in degrees." , font = ("Arial" , 10))
    degreeLabel.grid(row = 4 , pady = 10 , padx = 10 , sticky = N , columnspan = 4)

    # Label that tells the user what side/angle B means
    cMeaningLabel = Label(window , text = "Side C is used when calculating an angle. "
                                          "Angle C is used when calculating a side."
                          , font = ("Arial" , 10))
    cMeaningLabel.grid(row = 5 , pady = 10 , padx = 10 , sticky = N , columnspan = 4)

    # Initializes everything for the answer label
    answerLabel = Label(window , font = ("Arial" , 12))
    answerLabel.grid(row = 7 , pady = 10 , padx = 10 , sticky = N , columnspan = 4)

    def calculate():

        # Calculates the angle of a triangle using the law of cos
        def calculateAngle():
            try:
                sideA = float(sideAText.get(1.0, 'end-1c'))
                sideB = float(sideBText.get(1.0, 'end-1c'))
                sideC = float(sideOrAngleCText.get(1.0, 'end-1c'))

                sideC = math.pow(sideC, 2)
                d = math.pow(sideA, 2) + math.pow(sideB, 2)
                e = -2 * sideA * sideB
                sideC -= d
                e = sideC / e

                if e < 0:
                    alpha = math.degrees(math.acos(abs(e)))
                    angleC = 180 - alpha
                    answerLabel.config(text = "Alpha = " + str(alpha) + ". Angle C = " + str(angleC) + ".")

                else:
                    angleC = math.degrees(math.acos(abs(e)))
                    answerLabel.config(text = "Alpha = " + str(angleC) + ". Angle C = " + str(angleC) + ".")

            except ValueError:
                showerror("Invalid Number", "Make sure all numbers are valid!")

        # Calculates the side of a triangle using the law of cos
        def calculateSide():
            try:
                sideA = float(sideAText.get(1.0, 'end-1c'))
                sideB = float(sideAText.get(1.0, 'end-1c'))
                angleC = float(sideOrAngleCText.get(1.0, 'end-1c'))

                sideCSquared = \
                    math.pow(sideA, 2) + math.pow(sideB, 2) - 2 * sideA * sideB * math.cos(math.radians(angleC))
                sideC = math.sqrt(sideCSquared)
                answerLabel.config(text = "Side C Squared is " + str(sideCSquared) + ". Side C is " + str(sideC) + ".")
            except ValueError:
                showerror("Invalid Number", "Make sure all numbers are valid!")

        if toggle.get() == 1:
            calculateAngle()
        elif toggle.get() == 2:
            calculateSide()

    # Initializes everything for the calculate button
    calculate = Button(window , text = "Calculate" , command = calculate)
    calculate.grid(row = 6 , pady = 10 , padx = 10 , sticky = N, columnspan = 5)

# Initializes all of the buttons
triangleAreaButton = Button(root, text="Area of a Triangle", command=triangleArea)
triangleAreaButton.pack(pady=7, padx=7)
lawOfSinesButton = Button(root, text="Law of Sines", command=lawOfSines)
lawOfSinesButton.pack(pady=7, padx=7)
lawOfCosinesButton = Button(root, text="Law of Cosines", command=lawOfCosines)
lawOfCosinesButton.pack(pady=7, padx=7)

root.mainloop()
