from tkinter import *
from pandas import *
from math import sin
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Data for plot
df = DataFrame({'A': range(20),
                'B': [sin(i) for i in range(20)]
                }, index=range(20))

app = Tk()
app.config(bg='lightgray')
app.title("The title of the project")
app.geometry("800x600")
app.minsize(1000, 700)
app.rowconfigure(0, weight=1)
app.columnconfigure(3, weight=1)

fr_plot = Frame(app)
fr_plot.grid(row=0, column=1, sticky=N+S)

figure1 = plt.Figure(figsize=(5,4), dpi=80)
ax1 = figure1.add_subplot()
line1 = FigureCanvasTkAgg(figure1, fr_plot)
line1.get_tk_widget().pack(side=TOP, fill=BOTH)
df = df.iloc[:,1]
df.plot(kind='line', legend=True, ax=ax1, color='r', marker='o', fontsize=10)
ax1.set_title('Initial data')

app.mainloop()
