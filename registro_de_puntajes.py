
class RegistroDePuntajes:
    def __init__(self):
        self._registros = []
        self._id = 1

    def registrar_puntaje(self, nombre_jugador, puntaje):
        self._registros.append((self._id, nombre_jugador, puntaje))
        self._id += 1

    def mostrar_registros(self):
        print("Puntajes:")
        for id_, nombre, puntaje in self._registros:
            print(f"ID: {id_} - {nombre}: {puntaje} puntos")

    @property
    def registros(self):
        return self._registros

    @property
    def id(self):
        return self._id
