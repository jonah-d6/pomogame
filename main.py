import datetime
import tkinter as tk
from tkinter.ttk import *
from study_timer import StudyTimer
from log import save, read
import stuff

def leave():
    raise SystemExit

def main():
    start = datetime.datetime.now()

    root = tk.Tk()

    Button(root, text='Save And Exit', command=leave).pack()

    xp, pastLog = read()

    print(xp)

    app = StudyTimer(root, xp)

    try:
        root.mainloop()
    except SystemExit:
        timeSpent = datetime.datetime.now() - start
        save(start, timeSpent.total_seconds() / 60, app.xp - xp)

if __name__ == '__main__':
    main()
