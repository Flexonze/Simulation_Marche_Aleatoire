import random

class Marche():
    # step[0] = X
    # step[1] = Y
    def __init__(self):
        self.steps = [[0,0]]

    def get_previous_step(self):
        return self.steps[-1]

    def add_step(self, step):
        self.steps.append(step)

    def generate_step(self, walk_type):
        if walk_type == 'C':
            step = self.generate_C()
            self.add_step(step)

        elif walk_type == 'S':
            step = self.generate_S()

        elif walk_type == 'U':
            step = self.generate_U()
        
    def generate_C(self):
        direction = random.randrange(4)
        step = self.get_previous_step()

        # Haut
        if direction == 0:
            step = [step[0], step[1] + 1]

        # Bas
        elif direction == 1:
            step = [step[0], step[1] - 1]

        # Gauche
        elif direction == 2:
            step = [step[0] - 1, step[1]]

        # Droite
        elif direction == 3:
            step = [step[0] + 1, step[1]]

        return step


    def generate_S(self):
        step = self.get_previous_step()
        return step

    def generate_U(self):
        step = self.get_previous_step()
        return step

    def generate_z_steps(self, z, walk_type):
        for z in range(z):
            self.generate_step(walk_type)

    # Affiche en console les steps générées
    def display_walk(self): 
        for step in self.steps:
            print(step)

    def get_steps(self):
        return self.steps