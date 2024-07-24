"""
* Write a python program that asks the user a minimum of 3 riddles.

* You can look at riddles.com if you don't already know any riddles.

* Collect the response of each riddle from the user and compare their
  answers to the correct answer.

* Use a variable to keep track of the correctly answered riddles

* After all the riddles have been asked, tell the user how many they got
  correct
"""
import turtle
from tkinter import messagebox, simpledialog, Tk
window = Tk()
window.withdraw()
score = 0
ridde1 = simpledialog.askstring("hi", "Where does christmas come before thanksgiving?")
if ridde1 == 'In the dictionary':
    score = score + 1
riddle2 = simpledialog.askstring("hi", "What gets bigger the more you take away?")
if riddle2 == 'A hole':
    score = score + 1
riddle3 = simpledialog.askstring("hi", "what comes once in a minute, twice in a moment, and never in a thousand years?")
if riddle3 == 'The letter M':
    score = score + 1
messagebox.showinfo("hi", "You answered " + score.__str__() + " questions right! Congratulations! ... or not...")
