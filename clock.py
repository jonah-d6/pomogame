from tkinter import *
import time

root = Tk()

C = Canvas(root, bg="white", height=600, width=600)

for i in range(360):
    arc = C.create_arc(180, 150, 80, 210, start = i, extent = (i+1),
        fill = "green")
    time.sleep(1)
C.pack()
mainloop()
