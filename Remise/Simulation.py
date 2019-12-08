from marche import Marche
from modele import Modele
from tkinter import *
import statistics
import csv


def localize_floats(row):
    """ Fontion d'aide pour créer un csv français """
    return [
        str(el).replace('.', ',') if isinstance(el, float) else el 
        for el in row
    ]


def generate_one_to_x_csv(number_of_steps, executions, walk_type):
    """ Création d'un csv contenant la moyenne des distances au carrée de (executions) marches pour un nombre de pas allant de 1 jusqu'à (number_of_steps) """
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


def render_walk(number_of_steps, walk_type):
    """ Génère une marche pour le rendering """ 
    marche = Marche()
    failed = marche.generate_z_steps(number_of_steps, walk_type)

    while failed:
        marche.failed = False
        failed = marche.generate_z_steps(number_of_steps, walk_type)

    window = Tk(); window.geometry("+0+0"); window.title("simulation")
    modele = Modele(marche.get_steps(), master=window)
    modele.run()


def generate_walks(executions, number_of_steps, walk_type):
    """ Génère (executions) marches de (number_of_steps) pas de type (walk_type) """
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

    print(statistics.mean(distances))
    print(f'fails : {fail_count}')

def generate_martian_walks(executions, number_of_minutes, walk_type):
    """ Génère (executions) marches de (number_of_minutes) minutes de type (walk_type) """
    distances = []
    fail_count = 0
    for i in range(executions):
        marche = Marche()
        failed = marche.generate_z_martian_steps(number_of_minutes, walk_type)

        while failed:
            fail_count = fail_count + 1
            marche.failed = False
            failed = marche.generate_z_martian_steps(number_of_minutes, walk_type)

        distances.append(marche.get_distance())

    # Imprime la moyenne
    print(statistics.mean(distances))
    print(f'fails : {fail_count}')
    print(f'meters : {len(marche.get_steps()) - 1}')

def main():
    executions = 1
    number_of_steps = 150
    walk_type = 'S' # 'C', 'S', 'U'

    ## Render une marche ##
    render_walk(number_of_steps, walk_type)

    ## Génère (executions) marches de (number_of_steps) pas de type (walk_type) ##
    generate_walks(executions, number_of_steps, walk_type)

    ## Création d'un csv ##
    # generate_one_to_x_csv(number_of_steps, executions, walk_type)

    #### Partie 2 ####
    executions = 1
    number_of_minutes = 150 # 1 step per minute on speed 1
    walk_type = 'U' # 'C', 'S', 'U'

    ## Génère (executions) marches de (number_of_minutes) minutes de type (walk_type) ##
    # generate_martian_walks(executions, number_of_minutes, walk_type)



    return

if __name__ == "__main__":
    main()