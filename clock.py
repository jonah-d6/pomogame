from tkinter import *
import time

root = Tk()

C = Canvas(root, bg="white", height=600, width=600)

i = 0 #counter for degrees
def anotherArc(i):
    arc = C.create_arc(180, 150, 80, 210, start = i, extent = (i+1),
        fill = "green")
    root.after(100, anotherArc(i+1))
C.pack()
mainloop()
