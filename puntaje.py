
class Puntaje:
    def __init__(self):
        self.puntaje = 0

    def calcular_puntaje(self, intentos_restantes):
        self.puntaje = intentos_restantes * 10 

    def obtener_puntaje(self):
        return self.puntaje
