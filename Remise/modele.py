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

        if master is not None: # fenetre de rendering si necessaire
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
            self.canvas.delete(ALL) # clean du canvas
        else: self.g=None

    # update du modele 
    def update(self):                                                                                   #Ici, l'on implémente le code afin de faire notre pas (2.)
        self.previous_step = self.current_step
        self.state = self.state + 1 
        if self.state < len(self.steps):                                                               # mise a jour de l'etat du modele
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
        ############################################
        # debut boucle de simulation de la dynamique
        for step in self.steps:
            # on opere le systeme pour un pas
            self.update()
            self.render(self.canvas)                                                                      #Ici, le modèle fait 1 pas
            # rendering tkinter
            if self.canvas is not None: 
                # self.canvas.delete(ALL)                                                                  #Mettre ça en commentaire afin de faire afficher toutes les lignes de la simulation
                self.render(self.canvas)                                                                 #Ici, s'affiche le pas que nous avons fait
                self.canvas.update(); sleep(self.refreshTk)
                #if i==0: sleep(self.waitTk) # on attends pour laisser voir l'etat initial
        # fin boucle de simulation de la dynamique
        ############################################
