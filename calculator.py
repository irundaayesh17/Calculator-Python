import tkinter as tk
from tkinter import *
import math
from math import *


calc = ""
#functions
def add_calculations(number):
    try:
        calc = type_bar.get()
        type_bar.delete(0, END)
        type_bar.insert(0,str(calc) + str(number))
    
    except Exception as e:
         print("Error" + e)
    

def evaluate_calculations():
    global calc
    try:
        calc = type_bar.get()
        type_bar.delete(0, END)
        type_bar.insert(0, eval(calc))
    except ZeroDivisionError:
        type_bar.delete(0, END)
        type_bar.insert(0, "Cannot divide by zero")
    except Exception as e:
         print("Error" + e)

def clear_calculations():
    global calc
    calc = ""
    type_bar.delete(0, END)


#Creating the GUI

cal = tk.Tk()
cal.title("Calculator")
cal.geometry("320x287")
cal.resizable(False,  False)
cal.configure(background="black")

#entry frame
entry_frame = Frame(cal, width=320, height=50, bg="black")
entry_frame.pack(side=TOP)

type_bar = Entry(entry_frame, font=('arial', 20, 'bold'), bd=5, insertwidth=4, width=20 ,justify='right', bg="#202020", fg="white")
type_bar.grid(row=0, column=0)
type_bar.pack(ipady=10)

#button pad frame
button_pad = Frame(cal, width=320, height=400, bg="black")
button_pad.pack()

#row1
result = Button(button_pad, text="=", fg="#202020", width=10, height=3, bd=0, bg="#47b1e8", cursor="hand2", command=evaluate_calculations)
result.grid(row=0, column=0, padx=1, pady=1)

zero = Button(button_pad, text="0", fg="white", width=10, height=3, bd=0, bg="#202020", cursor="hand2", command=lambda: add_calculations(0))
zero.grid(row=0, column=1, padx=1, pady=1)

clear = Button(button_pad, text="CLEAR", fg="white", width=10, height=3, bd=0, bg="#202020", cursor="hand2", command=clear_calculations)
clear.grid(row=0, column=2, padx=1, pady=1)

divide = Button(button_pad, text="/", fg="white", width=10, height=3, bd=0, bg="#202020", cursor="hand2", command=lambda: add_calculations("/"))
divide.grid(row=0, column=3, padx=1, pady=1)

#row2
seven = Button(button_pad, text="7", fg="white", width=10, height=3, bd=0, bg="#202020", cursor="hand2", command=lambda: add_calculations(7))
seven.grid(row=1, column=0, padx=1, pady=1)

eight = Button(button_pad, text="8", fg="white", width=10, height=3, bd=0, bg="#202020", cursor="hand2", command=lambda: add_calculations(8))
eight.grid(row=1, column=1, padx=1, pady=1)

nine = Button(button_pad, text="9", fg="white", width=10, height=3, bd=0, bg="#202020", cursor="hand2", command=lambda: add_calculations(9))
nine.grid(row=1, column=2, padx=1, pady=1)


multiply = Button(button_pad, text="X", fg="white", width=10, height=3, bd=0, bg="#202020", cursor="hand2", command=lambda: add_calculations("*"))
multiply.grid(row=1, column=3, padx=1, pady=1)

#row3
four = Button(button_pad, text="4", fg="white", width=10, height=3, bd=0, bg="#202020", cursor="hand2", command=lambda: add_calculations(4))
four.grid(row=2, column=0, padx=1, pady=1)

five = Button(button_pad, text="5", fg="white", width=10, height=3, bd=0, bg="#202020", cursor="hand2", command=lambda: add_calculations(5))
five.grid(row=2, column=1, padx=1, pady=1)

six = Button(button_pad, text="6", fg="white", width=10, height=3, bd=0, bg="#202020", cursor="hand2", command=lambda: add_calculations(6))
six.grid(row=2, column=2, padx=1, pady=1)


substract = Button(button_pad, text="-", fg="white", width=10, height=3, bd=0, bg="#202020", cursor="hand2", command=lambda: add_calculations("-"))
substract.grid(row=2, column=3, padx=1, pady=1)

#row4
one = Button(button_pad, text="1" ,fg="white", width=10, height=3, bd=0, bg="#202020", cursor="hand2", command=lambda: add_calculations(1))
one.grid(row=3, column=0, padx=1, pady=1)

two = Button(button_pad, text="2", fg="white", width=10, height=3, bd=0, bg="#202020", cursor="hand2", command=lambda: add_calculations(2))
two.grid(row=3, column=1, padx=1, pady=1)

three = Button(button_pad, text="3", fg="white", width=10, height=3, bd=0, bg="#202020", cursor="hand2", command=lambda: add_calculations(3))
three.grid(row=3, column=2, padx=1, pady=1)


addition = Button(button_pad, text="+", fg="white", width=10, height=3, bd=0, bg="#202020", cursor="hand2", command=lambda: add_calculations("+"))
addition.grid(row=3, column=3, padx=1, pady=1)

cal.mainloop()