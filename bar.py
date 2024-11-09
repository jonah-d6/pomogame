from tkinter import *
from tkinter.ttk import *
import time

root = Tk()

progress = Progressbar(root, orient = HORIZONTAL, length = 100,
        mode = 'determinate')

def updateBar(leftover_exp, exp_to_go):
    progress.pack()

    progress['value'] = (leftover_exp / (exp_to_go + leftover_exp)) * 100

updateBar(150, 00)

mainloop()
