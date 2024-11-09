from tkinter import *
from tkinter.ttk import *
import time

def updateBar(leftover_exp, exp_to_go):
    progress = Progressbar(root, orient = HORIZONTAL, length = 100,
            mode = 'determinate')
    progress.pack()

    progress['value'] = (leftover_exp / (exp_to_go + leftover_exp)) * 100
