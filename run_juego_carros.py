"""
PASOS
1. Configurar Juego**\: Crear juego con jugadores, el juego debe tener los límites de kilómetros por 
   cada pista (un jugador puede ser un conductor y un conductor debe tener un carro asociado y un carro debe 
   estar asociado a un carril que a su vez debe estar en una pista)
2. Crear el ciclo con los imputs de variables
3. Revisar como hacer el dado tal vez con random
"""

class Juego:
    def __init__(self, njugador1, njugador2, nconductor1, nconductor2, npista):
        self.jugador1 = njugador1
        self.jugador2 = njugador2
        self.conductor1 = nconductor1
        self.conductor2 = nconductor2
        self.pista = npista
    def __str__(self):
        return f'Jugadores: {self.jugador1}, {self.jugador2} \nConductores: {self.conductor1}, {self.conductor2} \npista: {self.pista}'

class Jugador():
    pass

class Conductor():
    pass

class Pista():
    pass

class Carril():
    pass

class Podio():
    pass


nombre_jugador1 = input("¿Nombre del primer jugador?: ")
nombre_jugador2 = input("¿Nombre del segundo jugador?: ")
nombre_conductor1 = f'Conductor {nombre_jugador1}'
nombre_conductor2 = f'Conductor {nombre_jugador2}'
pista = "pista1"

juego_carrera = Juego(nombre_jugador1, nombre_jugador2, nombre_conductor1, nombre_conductor2, pista)
print(juego_carrera)