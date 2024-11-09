import tkinter

from stuff import experienceLeft, leftoverExperience, levelFromXP
import tkinter as tk
from tkinter.ttk import Progressbar
import math

# Constants
STUDY_TIME = 3 * 60  # 3 minutes
BREAK_TIME = 1 * 60 # 1 minute
class StudyTimer:
    def __init__(self, root, startXP):
        self.root = root
        self.root.title("Study Timer")
        
        # Timer settings
        self.time_left = STUDY_TIME
        self.studyMode = True
        self.color = "black"
        
        # Set up UI elements
        self.progress = Progressbar(root, orient=tkinter.HORIZONTAL, length=100, mode='determinate')
        self.progress.pack()

        self.canvas = tk.Canvas(root, width=200, height=200, bg="white")
        self.canvas.pack()

        self.mode_label = tk.Label(root, text=self.format_time(self.time_left), font=("Helvetica", 14))
        self.mode_label.pack()

        self.time_label = tk.Label(root, text=self.format_time(self.time_left), font=("Helvetica", 14))
        self.time_label.pack()

        self.xp = startXP

        self.level_label = tk.Label(root, text="Your current level is " + str(levelFromXP(self.xp)) + "!")
        self.level_label.pack()

        self.update_timer()
    
    def format_time(self, seconds):
        minutes = int(seconds // 60)
        seconds = int(seconds % 60)
        return f"{minutes:02}:{seconds:02}"
    
    def draw_circle(self):
        # Draw a circle with filling proportionate to time left
        angle = 360 * (self.time_left / (STUDY_TIME if self.studyMode else BREAK_TIME))
        self.canvas.delete("arc")
        self.canvas.create_arc(10, 10, 190, 190, start=90, extent=angle, fill=self.color, tags="arc")

    def update_timer(self):
        leftover = leftoverExperience(self.xp, levelFromXP(self.xp))
        to_go = experienceLeft(self.xp, levelFromXP(self.xp))
        self.progress['value'] = (leftover / (to_go + leftover)) * 100
        self.level_label.config(text="Your current level is " + str(levelFromXP(self.xp)) + "!")
        if self.studyMode:
            self.mode_label.config(text="Study Time!")
            self.color = "blue"
            self.xp += 1
        else:
            self.mode_label.config(text="Break Time!")
            self.color = "purple"

        if self.time_left > 0:
            self.time_left -= 1
            self.draw_circle()
            self.time_label.config(text=self.format_time(self.time_left))
            self.root.after(1000, self.update_timer)
        else:
            self.studyMode = not self.studyMode
            self.time_left = STUDY_TIME if self.studyMode else BREAK_TIME
            self.update_timer()

## Run the timer app
#if __name__ == "__main__":
#    root = tk.Tk()
#    app = StudyTimer(root)
#    root.mainloop()
