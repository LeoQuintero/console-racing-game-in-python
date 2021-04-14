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
    def __init__(self):
        # Contiene la configuración inicial del juego 
        self.bienvenida = "¡Bienvenido al juego de carros por consola!"            
        self.cantidad_jugadores = int(input('Ingrese cantidad de jugadores: ')) 
            
               
        
class Jugador(Juego): 
    # Adiciona en una diccionario el id con nombre del jugador  que ingrese el usuario.
    def __init__(self):
        Juego.__init__(self)
        self.dato_nombre_jugador = 'Ingrese el nombre del jugador #'
    
    def adiciona_jugador(self):
        cantidad_jugadores = self.cantidad_jugadores
        jugadores_dict = {}
        for id_jugador in range(1, cantidad_jugadores+1):
            nombre_jugador = input(f'{self.dato_nombre_jugador}{id_jugador}: ')          
            jugadores_dict[id_jugador+100] = {'nombre': nombre_jugador}
        return jugadores_dict          


class Conductor():
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

prueba = Jugador()    
print(prueba.adiciona_jugador())



# preguntar marca carro
# preguntar cantidad km de la pista.
# los carriles van orden de llegada jugador1 con carril1, jugador2 con carril3, jugador3 con carril3

