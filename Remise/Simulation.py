from marche import Marche
from modele import Modele
from tkinter import *
import statistics
import csv

def generate_one_to_x_csv(number_of_steps, executions, walk_type):
    # Création d'un csv contenant la moyenne des distances au carrée de (executions) marches pour un nombre de pas allant de 1 jusqu'à (number_of_steps)
    averages = []
    for x in range(number_of_steps):
        distances = []
        for i in range(executions):
            marche = Marche()
            marche.generate_z_steps(x, walk_type)
            distances.append(marche.get_distance())

        # Imprime la moyenne
        average = statistics.mean(distances)
        print(average)
        averages.append(average)

    with open(f'{walk_type}_1_to_{number_of_steps}.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(averages)
        print("fin")

def main():
    executions = 10000
    number_of_steps = 500
    walk_type = 'S' # 'C', 'S', 'U'

    # Génère une marche pour le render
    marche = Marche()
    marche.generate_z_steps(number_of_steps, walk_type)
    window = Tk(); window.geometry("+0+0"); window.title("simulation")
    modele = Modele(marche.get_steps(), master=window)
    modele.run()

    # Génère et calcule la moyenne des distances au carrée des (executions) marches de (number_of_steps) pas
    distances = []
    for i in range(executions):
        marche = Marche()
        marche.generate_z_steps(number_of_steps, walk_type)
        distances.append(marche.get_distance())

    # Imprime la moyenne
    print(statistics.mean(distances))


    # Création d'un csv contenant la moyenne des distances au carrée de (executions) marches pour un nombre de pas allant de 1 jusqu'à (number_of_steps)
    # generate_one_to_x_csv(number_of_steps, executions, walk_type)

    # Debugs #
    # marche.display_walk() # Debug
    # print(marche.get_previous_step())
    # print(marche.get_distance())
    return

if __name__ == "__main__":
    main()