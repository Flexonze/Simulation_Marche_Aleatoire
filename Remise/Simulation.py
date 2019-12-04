from marche import Marche
from modele import Modele
from tkinter import *
import statistics

def main():
    distances = []
    executions = 100000
    number_of_steps = 50
    walk_type = 'C' # 'C', 'S', 'U'

    # Génère une marche pour le render
    marche = Marche()
    marche.generate_z_steps(number_of_steps, walk_type)
    window = Tk(); window.geometry("+0+0"); window.title("simulation")
    modele = Modele(marche.get_steps(), master=window)
    modele.run()

    for i in range(executions):
        marche = Marche()
        marche.generate_z_steps(number_of_steps, walk_type)
        distances.append(marche.get_distance())

    print(statistics.mean(distances))

    # Debugs #
    # marche.display_walk() # Debug
    # print(marche.get_previous_step())
    # print(marche.get_distance())
    return

if __name__ == "__main__":
    main()