import tkinter as tk
from bar import updateBar
from study_timer import Study_Timer


def main():
    root = tk.Tk()

    label = tk.Label(root, text='We cookin now')
    label.pack()

    updateBar(root, 150, 200)

    root.mainloop()

if __name__ == '__main__':
    main()
