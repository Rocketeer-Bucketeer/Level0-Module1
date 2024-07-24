import turtle
from tkinter import messagebox, simpledialog, Tk

# Goal: Write a Python program that asks the user whether they want to
#       draw a triangle, square, or circle and then draw that shape.

if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    shape_turtle = turtle.Turtle()
    turtle.speed(1)
    turtle.color('pink')
    choice = simpledialog.askstring("the shape dude", "What shape do you want to see?")
    if choice == 'circle':
        turtle.shape('circle')
    elif choice == 'square':
        turtle.shape('square')
    elif choice == 'triangle':
        turtle.shape('triangle')
    # Make a new turtle
    
    # Ask the user what shape they want to draw and store it in a variable
    
    # Draw the shape requested by the user using if-elif-else statements
    
    # Call the turtle .done() method
