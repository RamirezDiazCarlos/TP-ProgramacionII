
from dibujar_ahorcado import DibujarAhorcado
from data import *
from puntaje import Puntaje
from registro_de_puntajes import RegistroDePuntajes

class Jugar:
    def __init__(self, nombre_jugador, registro):
        self.nombre_jugador = nombre_jugador
        self.registro = registro
        self.palabra_secreta = obtener_palabra()
        self.letras_adivinadas = []
        self.intentos_maximos = 6
        self.intentos = 0
        self.puntaje = Puntaje()

    def mostrar_palabra(self):
        resultado = ""
        for letra in self.palabra_secreta:
            if letra in self.letras_adivinadas:
                resultado += letra + " "
            else:
                resultado += "_ "
        return resultado

    def jugar(self):
        print(f"Bienvenido {self.nombre_jugador} al juego del ahorcado")
        print("Adivina la palabra")
        print(self.mostrar_palabra())

        while True:
            letra = input("Adivina una letra: ")

            if letra in self.letras_adivinadas:
                print("Ya se ingresó esa letra. Intenta otra.")
            else:
                self.letras_adivinadas.append(letra)

                if letra not in self.palabra_secreta:
                    self.intentos += 1
                    DibujarAhorcado.dibujar(self.intentos)
                    print(f"Letra incorrecta. Intentos restantes: {self.intentos_maximos - self.intentos}")
                else:
                    print("Letra correcta")

                palabra_mostrada = self.mostrar_palabra()
                print(palabra_mostrada)

                if palabra_mostrada.replace(" ", "") == self.palabra_secreta:
                    print(f"¡Felicidades, adivinaste la palabra! La palabra era '{self.palabra_secreta}'")
                    self.puntaje.calcular_puntaje(self.intentos_maximos - self.intentos)
                    self.registro.registrar_puntaje(self.nombre_jugador, self.puntaje.obtener_puntaje())
                    break

                if self.intentos == self.intentos_maximos:
                    print(f"Se agotaron los intentos. La palabra secreta era: '{self.palabra_secreta}'")
                    self.puntaje.calcular_puntaje(0)
                    self.registro.registrar_puntaje(self.nombre_jugador, self.puntaje.obtener_puntaje())
                    break

