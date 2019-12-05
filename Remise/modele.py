import math
import sys
from time import sleep
from tkinter import *

class Modele():

    def __init__(self, steps, step_length=10, refresh_rate=0.05, master=None):
        width=1000
        height=1000
        self.steps = steps
        self.state = 0
        self.current_step = self.steps[self.state]
        self.previous_step = self.current_step

        if master is None:
            self.g = None
            return
        
        self.refreshTk=refresh_rate
        self.waitTk=3
        self.frame = Frame(master)
        self.frame.pack()
        self.bframe = Frame(self.frame)
        self.bframe.pack(side=TOP)
        self.canvas_frame = Frame(self.frame, bd=2, relief=RAISED)
        self.canvas=Canvas(self.canvas_frame, bg='white', width=width, height=height) 
        self.canvas.pack()
        self.canvas_frame.pack(side=TOP)
        self.canvas.delete(ALL)
        self.offset = width // 2
        self.step_length = step_length

        # Écriture initial dans le canvas
        self.step_text = f'Step {self.state}'
        self.canvas_step_text = self.canvas.create_text(55, 20, fill="black", font="monaco", text=self.step_text)

        self.xy_text = f'0'
        self.canvas_xy_text = self.canvas.create_text(150, 40, fill="black", font="monaco", text=self.xy_text)
        self.circle = None

        # Point bleu en [0, 0]
        self.canvas.create_oval(
            0 + self.offset,
            0 + self.offset,
            0 + self.offset,
            0 + self.offset,
            outline="blue",
            fill="blue", 
            width=5,
        )

    # Update du modele 
    def update(self):
        self.previous_step = self.current_step
        self.state = self.state + 1 
        if self.state < len(self.steps):
            self.current_step = self.steps[self.state]
            self.step_text = f'Step {self.state}'
            self.xy_text = f'Current position: {self.current_step}'

    # Rendering du modele dans le canvas
    def render(self, canvas):
        canvas.create_line(
            self.previous_step[0] * self.step_length + self.offset,
            self.previous_step[1] * self.step_length + self.offset,
            self.current_step[0] * self.step_length + self.offset,
            self.current_step[1] * self.step_length + self.offset,
        )

        if self.circle != None:
            canvas.delete(self.circle)

        self.circle = canvas.create_oval(
                self.current_step[0] * self.step_length + self.offset,
                self.current_step[1] * self.step_length + self.offset,
                self.current_step[0] * self.step_length + self.offset,
                self.current_step[1] * self.step_length + self.offset,
                outline="red",
                fill="red", 
                width=5,
        )

        canvas.itemconfigure(self.canvas_step_text, text=self.step_text)
        canvas.itemconfigure(self.canvas_xy_text, text=self.xy_text)
    
        if self.state == len(self.steps):
            canvas.create_line(
                0 + self.offset,
                0 + self.offset,
                self.current_step[0] * self.step_length + self.offset,
                self.current_step[1] * self.step_length + self.offset,
                dash=(4, 4),
                fill="red"
            )
            self.canvas.create_text(112, 60, fill="red", font="monaco", text=f'Final distance: {pow(self.current_step[0], 2) + pow(self.current_step[1], 2)}')

    def run(self):
        for step in self.steps:
            self.update()
            self.render(self.canvas)

            if self.canvas is not None:                                                                      
                self.render(self.canvas)                                                                
                self.canvas.update()
                sleep(self.refreshTk)

        sleep(int(5))
