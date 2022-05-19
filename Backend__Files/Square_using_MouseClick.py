# Import the required libraries
from tkinter import *
from tkinter import ttk

# Create an instance of tkinter frame or window
win = Tk()
# Set the size of the window
win.geometry("700x350")

# Define a function to draw the line between two points
def draw_line(event):
    x1 = event.x
    y1 = event.y
    x2 = event.x
    y2 = event.y
    # Draw an rectabgle in the given co-ordinates
    canvas.create_rectangle(x1, y1, x2, y2, outline='black', width=20)

# Create a canvas widget
canvas = Canvas(win, width=700, height=350, background="white")
canvas.grid(row=0, column=0)
canvas.bind('<Button-1>', draw_line)
click_num = 0
win.mainloop()
