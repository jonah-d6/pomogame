from tkinter import *
import time

root = Tk()

C = Canvas(root, bg="white", height=600, width=600)
C.pack()

def createArc(n, c):
    C.create_arc(10, 10, 190, 190, start=0, extent =i+1, fill = c)

for i in range(360):
    createArc(i, "blue")
    C.update()
    time.sleep(0.1)
    C.delete('all')

for i in range(360):
    createArc(i, "purple")
    C.update()
    time.sleep(0.01)
    C.delete('all')


C.pack()
mainloop()
