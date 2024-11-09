import tkinter as tk
import math

# Constants
STUDY_TIME = 25 * 60  # 25 minutes

class StudyTimer:
    def __init__(self, root):
        self.root = root
        self.root.title("Study Timer")
        
        # Timer settings
        self.time_left = STUDY_TIME
        
        # Set up UI elements
        self.canvas = tk.Canvas(root, width=200, height=200, bg="white")
        self.canvas.pack()
        
        self.time_label = tk.Label(root, text=self.format_time(self.time_left), font=("Helvetica", 14))
        self.time_label.pack()
        
        self.update_timer()
    
    def format_time(self, seconds):
        minutes = seconds // 60
        seconds = seconds % 60
        return f"{minutes:02}:{seconds:02}"
    
    def draw_circle(self):
        # Draw a circle with filling proportionate to time left
        angle = 360 * (1 - self.time_left / STUDY_TIME)
        self.canvas.delete("arc")
        self.canvas.create_arc(10, 10, 190, 190, start=90, extent=angle, fill="blue", tags="arc")

    def update_timer(self):
        if self.time_left > 0:
            self.time_left -= 1
            self.draw_circle()
            self.time_label.config(text=self.format_time(self.time_left))
            self.root.after(1000, self.update_timer)
        else:
            self.time_label.config(text="Time's up!")
            self.canvas.delete("arc")

# Run the timer app
if __name__ == "__main__":
    root = tk.Tk()
    app = StudyTimer(root)
    root.mainloop()
