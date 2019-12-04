""" Renderin d'un modele avec Tkinter. """
import sys
from tkinter import *
from time import sleep

doRenderTk=True # choix de faire un rendering Tk ou pas
step_length = 10
offset = 500

class Modele():
    """ Modele pour simulation. """
  
    def __init__(self, steps, master=None):
        #self.init_modele() # init du modele lui-meme
        # canvas pour le rendering graphique 
        self.steps = steps
        self.state = 0
        self.current_step = self.steps[self.state]
        self.previous_step = self.current_step

        if master is None:
            self.g = None
            return
        
        self.refreshTk=0.05
        self.waitTk=3
        self.frame = Frame(master)
        self.frame.pack()
        self.bframe = Frame(self.frame)
        self.bframe.pack(side=TOP)
        self.canvas_frame = Frame(self.frame, bd=2, relief=RAISED)
        self.canvas=Canvas(self.canvas_frame, bg='white', width=1000, height=1000) 
        self.canvas.pack()
        self.canvas_frame.pack(side=TOP)
        self.canvas.delete(ALL)

    # update du modele 
    def update(self):
        self.previous_step = self.current_step
        self.state = self.state + 1 
        if self.state < len(self.steps):
            self.current_step = self.steps[self.state]

    # rendering du modele dans le canvas Tk
    def render(self, canvas):
        canvas.create_line(
            self.previous_step[0] * step_length + offset,
            self.previous_step[1] * step_length + offset,
            self.current_step[0] * step_length + offset,
            self.current_step[1] * step_length + offset,
        )

    def run(self):
        for step in self.steps:
            self.update()
            self.render(self.canvas)

            if self.canvas is not None:                                                                      
                self.render(self.canvas)                                                                
                self.canvas.update(); sleep(self.refreshTk)

        sleep(int(5))
