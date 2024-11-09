import tkinter as tk
from tkinter.ttk import *
from bar import updateBar
from study_timer import StudyTimer, level
from log import save, read
import stuff


def main():
    root = tk.Tk()

    Button(root, text = 'Stop Studying', command = stopStudy)

    label = tk.Label(root, text="Your current level is " +
            str(study_timer.level()) + "!")

    xp, pastLog = read()

    updateBar(root, stuff.leftoverExperience(), stuff.experienceLeft())

    app = StudyTimer(root)

    root.mainloop()

if __name__ == '__main__':
    main()
