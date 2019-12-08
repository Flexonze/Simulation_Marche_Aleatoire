import random
import math
import csv

class Marche():
    # step[0] = X
    # step[1] = Y
    def __init__(self):
        self.steps = [[0,0]]
        self.last_inverted_direction = None  # Cette variable représente la direction contraire du dernier pas (si le dernier pas est 0 (haut), self.last_inverted_direction = 1 (bas))
        self.failed = False
        self.speed = 1
        self.stop_durations = self.cvs_to_list()

    def get_previous_step(self):
        return self.steps[-1]

    def generate_step(self, walk_type):
        if walk_type == 'C':
            step = self.generate_random_step(avoid_last_inverted_direction=False)
            self.steps.append(step)

        elif walk_type == 'S':
            step = self.generate_random_step(avoid_last_inverted_direction=True)
            self.steps.append(step)

        elif walk_type == 'U':
            step = self.generate_U()
            self.steps.append(step)
            
    def generate_random_step(self, avoid_last_inverted_direction=False):
        direction = random.randrange(4)
        step = self.get_previous_step()

        if avoid_last_inverted_direction:
            while direction == self.last_inverted_direction:
                direction = random.randrange(4)

        # Haut
        if direction == 0:
            step = [step[0], step[1] + 1]
            self.last_inverted_direction = 1

        # Bas
        elif direction == 1:
            step = [step[0], step[1] - 1]
            self.last_inverted_direction = 0

        # Gauche
        elif direction == 2:
            step = [step[0] - 1, step[1]]
            self.last_inverted_direction = 3

        # Droite
        elif direction == 3:
            step = [step[0] + 1, step[1]]
            self.last_inverted_direction = 2

        return step

    def generate_U(self):
        temp_steps = []
        step = self.generate_random_step(avoid_last_inverted_direction=True)

        while step in self.steps:
            if step not in temp_steps:
                temp_steps.append(step)

            if len(temp_steps) == 3:
                self.failed = True
                break

            step = self.generate_random_step(avoid_last_inverted_direction=True)

        return step

    def generate_z_steps(self, z, walk_type):
        self.steps = [[0,0]]
        for z in range(z):   
            if self.failed:
                return self.failed
            self.generate_step(walk_type)

        return False

    # Affiche en console les steps générées
    def print_walk(self): 
        for step in self.steps:
            print(step)

    def get_steps(self):
        return self.steps

    def get_distance(self):
        final = self.get_previous_step()
        return pow(final[0], 2) + pow(final[1], 2)

    ##### PARTIE 2 #####
    def generate_z_martian_steps(self, z, walk_type):
        self.steps = [[0,0]]
        while z > 0:
            stop = self.get_stop()
            z = z - stop
            speed = self.get_speed()
            self.speed = speed
            while speed > 0:
                if self.failed:
                    return True
                self.generate_step(walk_type)
                speed = speed - 1
        return False

    def get_speed(self):
        test = random.randrange(12)
        if test != 0 :
            return self.speed

        if self.speed == 1:
            return 2

        if self.speed == 2:
            new_speed = random.randrange(2)
            if new_speed == 0:
                return 1 
            return 3

        if self.speed == 3:
            return 2

        return self.speed

    def get_stop(self):
        # 1206 / 172800 = Chance de faire un arrêt
        # 67 / 9600
        test = random.randrange(9600)
        if test < 67:
            test = random.randrange(len(self.stop_durations))
            return int(self.stop_durations[test])
        return 0

    def cvs_to_list(self):
        stops = []

        with open(f'arrets.csv', 'r', newline='') as file:
            reader = csv.reader(file, delimiter=',')
            for row in reader:
                stops.append(row[1])

        return stops