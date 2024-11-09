from tkinter import *
import time

def createArc(n, c):
    C.create_arc(10, 10, 190, 190, start=0, extent =i+1, fill = c)

root = Tk()
root.title("pomogame")

C = Canvas(root, bg="white", height=600, width=600)
C.pack()

breakStatus = StringVar()
breakStatus.set("It is working time! Get to work!")

label = Label(root, textvariable = breakStatus)
label.pack()

while True:

    breakStatus.set("It is working time! Get to work!")
    label = Label(root, textvariable = breakStatus)
    for i in range(360):
        createArc(i, "blue")
        C.update()
        time.sleep(0.02)
        C.delete('all')

    C.delete('all')

    breakStatus.set("It is break time!")
    label = Label(root, textvariable = breakStatus)
    for i in range(360):
        createArc(i, "purple")
        C.update()
        time.sleep(0.01)
        C.delete('all')

    C.delete('all')

    C.pack()
#mainloop()
