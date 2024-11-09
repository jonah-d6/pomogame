import tkinter as tk
import time

root = tk.Tk()
canvas = tk.Canvas(root, width=200, height=200)
canvas.pack()

def createArc(i):
    canvas.create_arc(10, 10, 190, 190, start=0, extent=i*5, fill='blue')


for i in range(360):
    createArc(i)
    canvas.update()
    time.sleep(1)
    
root.mainloop()