"""
* Write a Python program that asks the user for two numbers.

* Display the sum of the two numbers to the user
"""

import turtle
from tkinter import messagebox, simpledialog, Tk

window = Tk()
window.withdraw()

num1 = simpledialog.askinteger("1 + 1", "put in a number that you want to add")
num2 = simpledialog.askinteger("1 + 1", "put in another number that you want to add with the previous number")
sum = num1 + num2
messagebox.showinfo("1 + 1", "The sum of " + num1.__str__() + " and " + num2.__str__()  + " is "  + sum.__str__() + "!")
