from tkinter import *
import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure


# Creating tkinter window
win = Tk()


# Creating Figure.
fig = Figure(figsize = (5,5), dpi = 100)

x = [1,2,3,4,5]
y = ["Debdut", "Sayoni", "Aishwarya", "Ankit", "Brata"]


# Plotting the graph inside the Figure
a = fig.add_subplot(122)
a.plot(x,y, marker = "o", label = "October")
a.set_xlabel("Marks")
a.set_ylabel("Students")
a.set_title("Graph_Tk")
a.legend()
a.grid()


# Creating Canvas
canv = FigureCanvasTkAgg(fig, master = win)
canv.draw()

get_widz = canv.get_tk_widget()
get_widz.pack()

win.mainloop()
