# app.py
from jugar import Jugar
from registro_de_puntajes import RegistroDePuntajes

def menu():
    registro = RegistroDePuntajes()
    while True:
        print("\nMenu:")
        print("1. Jugar")
        print("2. Ver puntajes")
        print("3. Salir")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            nombre_jugador = input("Ingresa tu nombre: ")
            juego = Jugar(nombre_jugador, registro)
            juego.jugar()
        elif opcion == "2":
            registro.mostrar_registros()
        elif opcion == "3":
            print("¡Gracias por jugar! Nos vemos")
            break
        else:
            print("Opción no válida. Intenta de nuevo")

menu()
