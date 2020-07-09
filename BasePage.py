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


#driver code
if __name__ == "__main__":
    #to make the GUi window
    window=Tk()

    #to adjustment the screen size
    window.geometry("265x210")
    #to add a title to the GUI window
    window.title("Basic Calculator")
    #for background colr
    window.configure(bg="#989898")
    # StringVar() is the variable class
    # we create an instance of this class
    equation = StringVar()
    # for adding entry widgets on window and more stuff
    element_field = Entry(window, textvariable=equation ,justify='center')
    element_field.grid(columnspan=4, ipadx=65)
    equation.set('0000')








    #here it's the button and all adjustment
    button7 = Button(window, text=' 7 ', fg='black', bg='white',
                     command=lambda: press(7), height=2, width=8)
    button7.grid(row=2, column=0)
    button8 = Button(window, text=' 8 ', fg='black', bg='white',
                     command=lambda: press(8), height=2, width=8)
    button8.grid(row=2, column=1)
    button9 = Button(window, text=' 9 ', fg='black', bg='white',
                     command=lambda: press(9), height=2, width=8)
    button9.grid(row=2, column=2)
    button4 = Button(window, text=' 4 ', fg='black', bg='white',
                     command=lambda: press(4), height=2, width=8)
    button4.grid(row=3, column=0)
    button5 = Button(window, text=' 5 ', fg='black', bg='white',
                     command=lambda: press(5), height=2, width=8)
    button5.grid(row=3, column=1)
    button6 = Button(window, text=' 6 ', fg='black', bg='white',
                     command=lambda: press(6), height=2, width=8)
    button6.grid(row=3, column=2)
    button1 = Button(window, text=' 1 ', fg='black', bg='white',
                     command=lambda: press(1), height=2, width=8)
    button1.grid(row=4, column=0)
    button2 = Button(window, text=' 2 ', fg='black', bg='white',
                     command=lambda: press(7), height=2, width=8)
    button2.grid(row=4, column=1)
    button3 = Button(window, text=' 3 ', fg='black', bg='white',
                     command=lambda: press(3), height=2, width=8)
    button3.grid(row=4, column=2)
    button0 = Button(window, text=' 0 ', fg='black', bg='white',
                     command=lambda: press(0), height=2, width=8)
    button0.grid(row=5, column=1)


    plus = Button(window, text=' + ', fg='black', bg='white',
                    command=lambda: press("+"), height=2, width=8)
    plus.grid(row=2, column=3)

    minus = Button(window, text=' - ', fg='black', bg='white',
                    command=lambda: press("-"), height=2, width=8)
    minus.grid(row=3, column=3)

    multiply = Button(window, text=' * ', fg='black', bg='white',
                    command=lambda: press("*"), height=2, width=8)
    multiply.grid(row=4, column=3)

    divide = Button(window, text=' / ', fg='black', bg='white',
                    command=lambda: press("/"), height=2, width=8)
    divide.grid(row=5, column=2)

    equal = Button(window, text=' = ', fg='black', bg='#00cc44',
                    command=equalpress, height=2, width=8)
    equal.grid(row=5, column=3)

    clear = Button(window, text='Clear', fg='black', bg='#ff6666',
                    command=clear, height=2, width=8)
    clear.grid(row=0, column=3)

    Decimal = Button(window, text='.', fg='black', bg='white',
                    command=lambda: press('.'), height=2, width=8)
    Decimal.grid(row=5, column=0)
    #for start the gui;;its a enless loop
window.mainloop()