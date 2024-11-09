from tkinter import *

root = Tk()

C = Canvas(root, bg="white", height=600, width=600)

def anotherArc(i):
    if (i > 100):
        return
    arc = C.create_arc(180, 150, 80, 210, start = i, extent = (i+1),
        fill = "green")
    root.update()
    root.after(100, anotherArc(i+1))

anotherArc(0)

C.pack()
mainloop()
