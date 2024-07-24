import math
from tkinter import messagebox, simpledialog, Tk
import tkinter as tk

window = Tk()
window.withdraw()
radius = simpledialog.askinteger(title="the complete circle calculator", prompt="enter the radius of the circle")
choice = simpledialog.askstring(title="the complete circle calculator", prompt="Would you like the circumference or the area?")
if choice == 'area':
    circle = math.pi * radius * radius
    messagebox.showinfo("smurt", circle.__str__())
elif choice == 'circumference':
    circumference = math.pi * radius * 2
    messagebox.showinfo("smurt", circumference.__str__())
# Write a Python program that asks the user for the radius of a circle.
# Next, ask the user if they would like to calculate the area or circumference of a circle.
# If they choose area, display the area of the circle using the radius.
# Otherwise, display the circumference of the circle using the radius.

#Area = πr^2
#Circumference = 2πr 
