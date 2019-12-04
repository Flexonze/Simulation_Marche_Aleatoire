from marche import Marche

def main():
    marche = Marche()
    marche.generate_i_steps(5,'C')
    marche.display_walk()
    return

if __name__ == "__main__":
    main()