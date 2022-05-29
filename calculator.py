#!/usr/bin/env python3

__version__: '1.0' # Revised January 5th, 2022

# Tkinter based GUI Calculator

# Import everything from tkinter module
from tkinter import *

# Define the default expression value (thing to be evaluated by calc AND displayed in textbox)
# via equation variable and set.
expression = ""

# Define the calculator

def calculator():
    # Define function to update expression in the text box on button press
    def press(num):
        # Make sure this updates globally, not just within this function
        global expression

        # Take button press related text that was fed to this function and append to expression
        expression = expression + str(num)

        # Use set method to make sure the textbox is correctly updated on button press
        # equation is the variable use to define what the user sees in textbox. Must be a
        # str value. Set class later.
        equation.set(expression)


    # Define the function to evaluate the final expression
    def equalpress():
        # In case of errors like attempts to divide by zero etc, try/except used
        try:

            global expression

            # Use built in eval function from python to run the calculation and use 
            # str to convert it to a string for display
            total = str(eval(expression))

            # Again, use set method to update textbox
            equation.set(total)

            # Return expression back to a blank state ready for the next calculation
            expression = ""

        # Except - use to give error message for bad expressions
        except:

            equation.set(" error ")
            expression = ""


    # Define function to clear text box on related button press
    def clear():
        global expression
        expression = ""
        equation.set("")


    # Use above defined functions in GUI format

    # Establish the app window
    app = Tk()

    # Background colour
    app.configure(background="grey")

    # Window title
    app.title("Python Calculator V1.0")

    # Size of window
    app.geometry("355x200")

    # Variable needs to be of the string class always. Define instance of this.
    equation = StringVar()

    # Create the text box that shows the expression
    expression_field = Entry(app, textvariable=equation)

    # Use a grid widget to define object/button placement.
    expression_field.grid(columnspan=4, ipadx=70)

    # Define buttons, the command/function they should trigger, and their placement.
    button1 = Button(app, text=' 1 ', fg='white', bg='black',
                    command=lambda: press(1), height=1, width=7)
    button1.grid(row=2, column=0)

    button2 = Button(app, text=' 2 ', fg='white', bg='black',
                    command=lambda: press(2), height=1, width=7)
    button2.grid(row=2, column=1)

    button3 = Button(app, text=' 3 ', fg='white', bg='black',
                    command=lambda: press(3), height=1, width=7)
    button3.grid(row=2, column=2)

    button4 = Button(app, text=' 4 ', fg='white', bg='black',
                    command=lambda: press(4), height=1, width=7)
    button4.grid(row=3, column=0)

    button5 = Button(app, text=' 5 ', fg='white', bg='black',
                    command=lambda: press(5), height=1, width=7)
    button5.grid(row=3, column=1)

    button6 = Button(app, text=' 6 ', fg='white', bg='black',
                    command=lambda: press(6), height=1, width=7)
    button6.grid(row=3, column=2)

    button7 = Button(app, text=' 7 ', fg='white', bg='black',
                    command=lambda: press(7), height=1, width=7)
    button7.grid(row=4, column=0)

    button8 = Button(app, text=' 8 ', fg='white', bg='black',
                    command=lambda: press(8), height=1, width=7)
    button8.grid(row=4, column=1)

    button9 = Button(app, text=' 9 ', fg='white', bg='black',
                    command=lambda: press(9), height=1, width=7)
    button9.grid(row=4, column=2)

    button0 = Button(app, text=' 0 ', fg='white', bg='black',
                    command=lambda: press(0), height=1, width=7)
    button0.grid(row=5, column=0)

    plus = Button(app, text=' + ', fg='black', bg='orange',
                command=lambda: press("+"), height=1, width=7)
    plus.grid(row=5, column=1)

    minus = Button(app, text=' - ', fg='black', bg='orange',
                command=lambda: press("-"), height=1, width=7)
    minus.grid(row=6, column=1)

    multiply = Button(app, text=' * ', fg='black', bg='orange',
                    command=lambda: press("*"), height=1, width=7)
    multiply.grid(row=4, column=3)

    divide = Button(app, text=' / ', fg='black', bg='orange',
                    command=lambda: press("/"), height=1, width=7)
    divide.grid(row=3, column=3)

    equal = Button(app, text=' = ', fg='black', bg='orange',
                command=equalpress, height=3, width=18)
    equal.grid(row=5, column=2, columnspan=2, rowspan=2)

    clear = Button(app, text='Clear', fg='black', bg='orange',
                command=clear, height=1, width=7)
    clear.grid(row=2, column=3)

    Decimal= Button(app, text='.', fg='black', bg='orange',
                    command=lambda: press('.'), height=1, width=7)
    Decimal.grid(row=6, column=0)
    
    # Boot calculator and ensure it runs till closed by user
    app.mainloop()

if __name__ == "__main__":
    calculator()