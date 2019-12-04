from marche import Marche
from modele import Modele
from tkinter import *

def main():
    marche = Marche()
    marche.generate_z_steps(40,'C')
    # marche.display_walk() # Debug

    window = Tk(); window.geometry("+0+0"); window.title("simulation")

    modele = Modele(marche.get_steps(), master=window)
    modele.run()

    return

if __name__ == "__main__":
    main()