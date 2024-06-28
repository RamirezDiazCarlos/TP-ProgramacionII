
class DibujarAhorcado:
    @staticmethod
    def dibujar(intentos):
        if intentos == 0:
            print("  ____")
            print(" |    |")
            print(" |")
            print(" |")
            print(" |")
            print(" |_________")
        elif intentos == 1:
            print("  ____")
            print(" |    |")
            print(" |    O")
            print(" |")
            print(" |")
            print(" |_________")
        elif intentos == 2:
            print("  ____")
            print(" |    |")
            print(" |    O")
            print(" |    |")
            print(" |")
            print(" |_________")
        elif intentos == 3:
            print("  ____")
            print(" |    |")
            print(" |    O")
            print(" |   /|")
            print(" |")
            print(" |_________")
        elif intentos == 4:
            print("  ____")
            print(" |    |")
            print(" |    O")
            print(" |   /|\\")
            print(" |")
            print(" |_________")
        elif intentos == 5:
            print("  ____")
            print(" |    |")
            print(" |    O")
            print(" |   /|\\")
            print(" |   /")
            print(" |_________")
        elif intentos == 6:
            print("  ____")
            print(" |    |")
            print(" |    O")
            print(" |   /|\\")
            print(" |   / \\")
            print(" |_________")
