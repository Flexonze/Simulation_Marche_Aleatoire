from marche import Marche
from modele import Modele
from tkinter import *
import statistics

def main():
    distances = []
    executions = 100000

    for i in range(executions):
        marche = Marche()
        marche.generate_z_steps(1000,'S')
        distances.append(marche.get_distance())

    print(statistics.mean(distances))
    # marche.display_walk() # Debug
    # print(marche.get_previous_step())
    # print(marche.get_distance())

    # window = Tk(); window.geometry("+0+0"); window.title("simulation")
    # modele = Modele(marche.get_steps(), master=window)
    # modele.run()
    return

if __name__ == "__main__":
    main()