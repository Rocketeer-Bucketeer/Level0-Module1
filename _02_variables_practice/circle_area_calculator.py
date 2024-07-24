import turtle
from tkinter import messagebox, simpledialog, Tk
import math

# Goal: Write a Python program that asks the user for the radius 
#       of a circle and displays the area of that circle.
#       The formula for the area of a circle is πr^2.
#       See example image in package to check your output.

if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    
    # Ask the user for the radius in pixels and store it in a variable
    radius = simpledialog.askinteger("circle calculator", "put the radius in pixels")
    my_turtle = turtle.Turtle
    turtle.speed(10)
    turtle.circle(radius)
    turtle.penup()
    turtle.goto(100, 100)
    circle = math.pi * radius * radius
    print(circle)
    turtle.write(arg="area = " + str(circle), move=True, align='left', font=('Arial' ,8, 'normal'))
    turtle.hideturtle()
    turtle.done()

    # simpledialog.askinteger()
    
    # Make a new turtle
    
    # Have your turtle draw a circle with the correct radius
    # my_turtle.circle()

    # Call the turtle .penup() method

    # Move your turtle to a new x,y position using .goto()

    # Calculate the area of your circle and store it in a variable
    # Hint, you can use math.pi
    
    # Write the area of your circle using the turtle .write() method
    # my_turtle.write(arg="area = " + str(area), move=True, align='left', font=('Arial',8,'normal'))

    # Hide your turtle

    # Call turtle.done()
