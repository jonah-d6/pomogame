import datetime
import tkinter as tk
from tkinter.ttk import *
from study_timer import StudyTimer
from log import save, read
import stuff

# exits cleanly
def leave():
    raise SystemExit

def main():
    start = datetime.datetime.now()

    root = tk.Tk()

    Button(root, text='Save And Exit', command=leave).pack()

    # pull in save data
    xp, pastLog = read()

    app = StudyTimer(root, xp)

    try:
        root.mainloop()
    except SystemExit:
        # saves when exiting
        timeSpent = datetime.datetime.now() - start
        save(start, timeSpent.total_seconds() / 60, app.xp - xp)

if __name__ == '__main__':
    main()
