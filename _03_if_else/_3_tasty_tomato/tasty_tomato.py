from tkinter import messagebox, simpledialog
import tkinter as tk

window_width = 600
window_height = 600

root = tk.Tk()

canvas = tk.Canvas(root, width=window_width, height=window_height, bg="#DDDDDD")
canvas.grid()

# 1. Ask the user what color tomato they would like and save their response
#    You can give them up to three choices

tomato_color = simpledialog.askstring("hi", "put in a tomato color from red or green!")
print(tomato_color)
if tomato_color == 'red':
    canvas.create_oval(75, 200, 400, 450, fill="red", outline="")
    canvas.create_oval(200, 200, 525, 450, fill="red", outline="")

    canvas.create_rectangle(275, 100, 325, 230, fill="green", outline="")
elif tomato_color == 'green':
    canvas.create_oval(75, 200, 400, 450, fill="green", outline="")
    canvas.create_oval(200, 200, 525, 450, fill="green", outline="")

    canvas.create_rectangle(275, 100, 325, 230, fill="green", outline="")



# 2. Use if-else statements to draw the tomato in the color that they chose
#    You can modify the code below or draw your own tomato

root.mainloop()
