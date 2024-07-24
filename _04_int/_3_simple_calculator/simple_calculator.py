"""
* Write a Python program that asks the user for two numbers.

* Then ask the user if the would like to add, subtract, multiply, or divide.

* Use if-else statements to provide the desired math operation on the numbers
  and display the result.
"""
import turtle
from tkinter import messagebox, simpledialog, Tk
window = Tk()
window.withdraw()

thing = simpledialog.askstring("upper calculator", "would you like to add, subtract, multiply, or divide?")
if thing == 'add':
    add1 = simpledialog.askinteger("upper calculator", "put in the number that you would like to add")
    add2 = simpledialog.askinteger("upper calculator", "put in another number")
    add_answer = add2 + add1
    messagebox.showinfo("upper calculator", "The sum of " + add1.__str__() + " and " + add2.__str__() + " is " + add_answer.__str__() + "!")
elif thing == 'subtract':
    sub1 = simpledialog.askinteger("upper calculator", "input the number that you would like to subtract FROM")
    sub2 = simpledialog.askinteger("upper calculator", "input the number that you would like to subtract BY")
    sub_answer = sub1 = sub2
    messagebox.showinfo("upper calculator", "The difference of " + sub1.__str__() + " and " + sub2.__str__() + " is " + sub_answer.__str__() + "!")

