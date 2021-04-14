import random

"""
PASOS
1. Configurar Juego**\: Crear juego con jugadores, el juego debe tener los límites de kilómetros por 
   cada pista (un jugador puede ser un conductor y un conductor debe tener un carro asociado y un carro debe 
   estar asociado a un carril que a su vez debe estar en una pista)
2. Crear el ciclo con los imputs de variables
3. Revisar como hacer el dado tal vez con random
"""

class Juego():
    def __init__(self, n_jugadores):
        # Contiene la configuración inicial del juego 
        self.bienvenida = "¡Bienvenido al juego de carros por consola!"       
        self.cantidad_jugadores = n_jugadores        
               
        
class Jugador(Juego): 
    # Adiona en una diccionario el id con nombre del jugador.
    def adicionar_jugador(self):
        pregunta = "adicione el nombre del jugador #"
        player_dict = {}
        for nplayer in range(1, self.cantidad_jugadores+1):  
            name_player = input(f'{pregunta} {nplayer}:')    
            player_dict[nplayer+100] = name_player
            print(player_dict)

class Conductor():
    # hereda jugador
    # mas carril asociado.
    pass

class Carro():
    # debe tener un conductor
    # debe tener un carril    
    pass

class Pista():
    # límite distancia
    # cantidad carriles ej: 3 carriles
    pass  

class Carril():
    # Número Carril
    # Carro asociado    
    pass

class Podio():
    # podio nombre jugador 
    # posición 1 = oro
    # posicion 2 = plata
    # posicion 3 = bronce
    pass

"""
n_jugadores = int(input("Número de jugadores: " ))
inicio_juego = Juego(n_jugadores)
print(inicio_juego.bienvenida
"""

prueba = Jugador(3)
print(prueba.bienvenida)
print(prueba.adicionar_jugador())


# preguntar marca carro
# preguntar cantidad km de la pista.
# los carriles van orden de llegada jugador1 con carril1, jugador2 con carril3, jugador3 con carril3

