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
        self.cantidad_jugadores = 'Ingrese cantidad de jugadores: '
        self.dato_nombre_jugador = 'Ingrese el nombre del jugador #'
        self.dato_nombre_conductor = "Asigne un nombre a su conductor: "
        self.dato_marca_carro = "eliga una opción para marca de carro:\n 1. Lotus Evija\n 2. NIO EP9\n"
            
               
        
class Jugador(Juego): 
    # Adiciona en una diccionario el id con nombre del jugador  que ingrese el usuario.
       
    def adiciona_jugador(self):
        cantidad_jugadores = int(input(self.cantidad_jugadores))
        jugadores_dict = {}
        for id_jugador in range(1, cantidad_jugadores+1):
            nombre_jugador = input(f'{self.dato_nombre_jugador}{id_jugador}: ')          
            jugadores_dict[id_jugador+100] = {'jugador': nombre_jugador}
        return jugadores_dict          


class Conductor(Jugador):    
    def adiciona_conductor(self):
        jugadores_dict = self.adiciona_jugador()
        for id_jugador in jugadores_dict.keys():
            nombre_jugador = jugadores_dict[id_jugador]['jugador']
            nombre_conductor = input(f'para el jugador {nombre_jugador} {self.dato_nombre_conductor}: ')
            jugadores_dict[id_jugador]['conductor'] = nombre_conductor
        return jugadores_dict


class Carro(Conductor):
    def adiciona_carro(self):
        jugadores_dict = self.adiciona_conductor()
        for id_jugador in jugadores_dict.keys():
            nombre_conductor = jugadores_dict[id_jugador]['conductor']
            nombre_carro = input(f'para el jugador {nombre_conductor} {self.dato_marca_carro} : ')
            jugadores_dict[id_jugador]['carro'] = nombre_carro
        return jugadores_dict  

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

jugador = Carro()  
print(jugador.bienvenida)  
jugadores_dict = jugador.adiciona_carro()
print(jugadores_dict)



# preguntar marca carro
# preguntar cantidad km de la pista.
# los carriles van orden de llegada jugador1 con carril1, jugador2 con carril3, jugador3 con carril3

