from tkinter import *

root = Tk()

C = Canvas(root, bg="white", height=600, width=600)

def anotherArc(i):
    arc = C.create_arc(180, 150, 80, 210, start = i, extent = (i+1),
        fill = "green")
    root.update()

for i in range(100):
    root.after(1000, anotherArc(i))


C.pack()
mainloop()
