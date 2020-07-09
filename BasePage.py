#import every thing from tkinter
from tkinter import *

#global declration
element =""

#its to update the element pressed by the user
def press(num):
        global element
        element = element + str(num)
        equation.set(element)
#when the user enter equalbutton
def equalpress():
    """Try and except statement is used
       for handling the errors like zero
       division error etc."""
    try:
        global element
        #evaluate the value
        total = str(eval(element))
        equation.set(total)
        element = ""
    except:

        equation.set(" error ")
        element = ""

#function to clear the text entry place
def clear():
    global element
    element = ""
    equation.set("")