from marche import Marche
from modele import Modele
from tkinter import *
import statistics
import csv

def localize_floats(row):
    return [
        str(el).replace('.', ',') if isinstance(el, float) else el 
        for el in row
    ]

def generate_one_to_x_csv(number_of_steps, executions, walk_type):
    # Création d'un csv contenant la moyenne des distances au carrée de (executions) marches pour un nombre de pas allant de 1 jusqu'à (number_of_steps)
    averages = []
    fails = []
    for x in range(number_of_steps + 1):
        distances = []
        fail_count = 0
        for i in range(executions):
            marche = Marche()
            failed = marche.generate_z_steps(x, walk_type)
            while failed:
                fail_count = fail_count + 1
                marche.failed = False
                failed = marche.generate_z_steps(x, walk_type)

            distances.append(marche.get_distance())

        # Imprime la moyenne
        print(x)
        average = statistics.mean(distances)
        print(average)
        averages.append(average)
        print(f'fails : {fail_count}')
        fails.append(fail_count)

    with open(f'{walk_type}_1_to_{number_of_steps}.csv', 'w', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(localize_floats(averages))

    if walk_type == 'U':
        with open(f'{walk_type}_1_to_{number_of_steps}_fails.csv', 'w', newline='') as file:
            writer = csv.writer(file, delimiter=';')
            writer.writerow(fails)

    print("fin")

def main():
    executions = 1
    number_of_steps = 300
    walk_type = 'U' # 'C', 'S', 'U'

    # Génère une marche pour le render

    marche = Marche()
    failed = marche.generate_z_steps(number_of_steps, walk_type)

    while failed:
        marche.failed = False
        failed = marche.generate_z_steps(number_of_steps, walk_type)

    window = Tk(); window.geometry("+0+0"); window.title("simulation")
    modele = Modele(marche.get_steps(), master=window)
    modele.run()

    # Génère et calcule la moyenne des distances au carrée des (executions) marches de (number_of_steps) pas
    distances = []
    fail_count = 0
    for i in range(executions):
        marche = Marche()
        failed = marche.generate_z_steps(number_of_steps, walk_type)

        while failed:
            fail_count = fail_count + 1
            marche.failed = False
            failed = marche.generate_z_steps(number_of_steps, walk_type)

        distances.append(marche.get_distance())

     # Imprime la moyenne
    print(statistics.mean(distances))
    print(f'fails : {fail_count}')


    # Création d'un csv contenant la moyenne des distances au carrée de (executions) marches pour un nombre de pas allant de 1 jusqu'à (number_of_steps)
    # generate_one_to_x_csv(number_of_steps, executions, walk_type)

    # Debugs #
    # marche.display_walk() # Debug
    # print(marche.get_previous_step())
    # print(marche.get_distance())
    return

if __name__ == "__main__":
    main()