""" Renderin d'un modele avec Tkinter. """
import sys
from tkinter import *
from time import sleep

doRenderTk=True # choix de faire un rendering Tk ou pas

class Modele():
    """ Modele pour simulation. """
  
    def __init__(self, master=None):
        self.init_modele() # init du modele lui-meme
        # canvas pour le rendering graphique 
        self.canvas_size=(600,600) # taille du canvas pour le rendering
        if master is not None: # fenetre de rendering si necessaire
            self.refreshTk=1.0
            self.waitTk=3
            self.frame = Frame(master)
            self.frame.pack()
            self.bframe=Frame(self.frame)
            self.bframe.pack(side=TOP)
            self.gframe=Frame(self.frame,bd=2,relief=RAISED)
            self.g=Canvas(self.gframe,bg='white',width=self.canvas_size[0],height=self.canvas_size[1]) 
            self.g.pack()
            self.gframe.pack(side=TOP)
            self.g.delete(ALL) # clean du canvas
        else: self.g=None

    def init_modele(self): # init du modele
        self.nbPas=5 # nombre de pas de simulation
        self.etat=0 # variable d'etat

    def update(self): # update du modele                                                            #Ici, l'on implémente le code afin de faire notre pas (2.)
        self.etat=self.etat+1 # mise a jour de l'etat du modele

    def render(self,g): # rendering du modele dans le canvas Tk g                                   #Ici, l'on doit modifier la fonction afin de faire afficher une petite ligne (create line)
        bfont=('times',14,'bold')
        bbox=(100,100,150,140)
        g.create_rectangle(bbox,width=1,outline="black",fill="yellow")
        g.create_text((bbox[0]+25,bbox[1]+20),text=str(self.etat),font=bfont,fill='black')

    def run(self):
        ############################################
        # debut boucle de simulation de la dynamique
        for i in range(self.nbPas):
            # on opere le systeme pour un pas
            self.update()                                                                           #Ici, le modèle fait 1 pas
            # rendering tkinter
            if self.g is not None: 
                self.g.delete(ALL)                                                                  #Mettre ça en commentaire afin de faire afficher toutes les lignes de la simulation
                self.render(self.g)                                                                 #Ici, s'affiche le pas que nous avons fait
                self.g.update(); sleep(self.refreshTk)
                if i==0: sleep(self.waitTk) # on attends pour laisser voir l'etat initial
        # fin boucle de simulation de la dynamique
        ############################################

""" A executer seulement si ce n'est pas un import, mais bien un run du code. """
if __name__ == '__main__':
    if doRenderTk: # avec rendering Tk (animation)
        root = Tk(); root.geometry("+0+0"); root.title("simulation")
    else: root=None
    x = Modele(root) # creation du modele
    x.run() # run du modele (simulation) avec ou sans animation
    if root is not None: root.mainloop()

