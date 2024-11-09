import tkinter as tk
from bar import updateBar
from study_timer import StudyTimer


def main():
    root = tk.Tk()

    updateBar(root, 150, 200)

    app = StudyTimer(root)

    root.mainloop()

if __name__ == '__main__':
    main()
