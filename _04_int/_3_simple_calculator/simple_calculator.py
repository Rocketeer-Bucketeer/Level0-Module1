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
    sub_answer = sub1 - sub2
    messagebox.showinfo("upper calculator", "The difference of " + sub1.__str__() + " and " + sub2.__str__() + " is " + sub_answer.__str__() + "!")
elif thing == 'multiply':
    mult1 = simpledialog.askinteger("upper calculator", "input the number that you would like to multiply")
    mult2 = simpledialog.askinteger("upper calculator", "input the number that you would to multiply " + mult1.__str__() + "by.")
    mult_answer = mult1 * mult2
    messagebox.showinfo("upper calculator", "The product of " + mult1.__str__() + " and " + mult2.__str__() + " is " + mult_answer.__str__() + "!")
elif thing == 'divide':
    div1 = simpledialog.askinteger("upper calculator", "input the number that you would like to DIVIDE")
    div2 = simpledialog.askinteger("upper calculator", "input the number that you would like to divide BY")
    div_answer = div1 / div2
    messagebox.showinfo("upper calculator", "The quotient of " + div1.__str__() + " and " + div2.__str__() + " is " + div_answer.__str__())
else:
    messagebox.showinfo("upper calculator", "sorry, i couldn't read what you said. please type the option in lowercases. ( example: subtract )")
