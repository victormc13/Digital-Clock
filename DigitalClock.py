from tkinter import *
from tkinter.ttk import *

from time import strftime

main = Tk()

main.title('Digital clock in Python. by Victor')

def clock():
    tick = strftime('%H:%M:%S %p  %a')

    clock_label .config(text = tick)

    clock_label .after(1000, clock)

clock_label = Label(main, font = ('arial', 80), background = 'black', foreground = 'blue')

clock_label.pack(anchor = 'center')

clock()
mainloop()