import tkinter as tk
from bar import updateBar
from

def main():
    root = tk.Tk()

    label = tk.Label(root, text='We cookin now')
    label.pack()

    root.mainloop()

if __name__ == '__main__':
    main()
