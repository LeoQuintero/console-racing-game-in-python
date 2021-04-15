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
        # crea un diccionario donde asigna un ID de jugador con valor diccionario de llave jugador con valor nombre jugador.
        cantidad_jugadores = int(input(self.cantidad_jugadores))
        jugadores_dict = {}
        for id_jugador in range(1, cantidad_jugadores+1):
            nombre_jugador = input(f'{self.dato_nombre_jugador}{id_jugador}: ')          
            jugadores_dict[id_jugador+100] = {'jugador': nombre_jugador} # diccionario  llave id con llave jugador con valor nombre del jugador
        return jugadores_dict          


class Conductor(Jugador):
    # Agrega al diccionario de jugadores el nombre de conductor.    
    def adiciona_conductor(self):
        jugadores_dict = self.adiciona_jugador()
        for id_jugador in jugadores_dict.keys():
            nombre_jugador = jugadores_dict[id_jugador]['jugador']
            nombre_conductor = input(f'para el jugador {nombre_jugador} {self.dato_nombre_conductor}: ')
            jugadores_dict[id_jugador]['conductor'] = nombre_conductor # aciciono llave conductor y su valor
        return jugadores_dict


class Carro(Conductor):
    # Agrega según elecciónn del usuario el carro a cada conductor.
    def adiciona_carro(self):
        jugadores_dict = self.adiciona_conductor()
        for id_jugador in jugadores_dict.keys():
            nombre_conductor = jugadores_dict[id_jugador]['conductor']
            tipo_carro = input(f'para el jugador {nombre_conductor} {self.dato_marca_carro} : ')
            jugadores_dict[id_jugador]['carro'] = tipo_carro
        return jugadores_dict 

class Pista(Carro):
    #Agrega la pista con la distancia en kilómetros segun valor ingresado por usuario.
    def distancia_pista(self):
        jugadores_dict = self.adiciona_carro()
        distancia_km = int(input("Ingrese el valor entero de límete de KM de la pista: "))
        for id_jugador in jugadores_dict.keys():
            jugadores_dict[id_jugador]['pista'] = distancia_km # adiciono llave pista y valor
        return jugadores_dict


class Carriles(Pista):
    # agrega en # carril de acuerdo a las cantidad de carros automáticamente de forma descendente.
    def numero_carriles(self):
        jugadores_dict = self.distancia_pista()
        cantidad_carros = len(list(jugadores_dict.keys()))
        for carro in jugadores_dict.keys():
            jugadores_dict[carro]['carril'] = cantidad_carros # adiciono llave carril y valor
            cantidad_carros -= 1
        return jugadores_dict


class Podio():
    # contiene un dado de 1 a 6 para avanzar en multiplos de 100 metros cada carro.
    # Hace la converción en metros de la distancia restante para llegar
    # los tre primeros en llegar reciben podio con valor oro, plata y bronce respectivamente.
    #def run_carrera()
    pass
    

"""
n_jugadores = int(input("Número de jugadores: " ))
inicio_juego = Juego(n_jugadores)
print(inicio_juego.bienvenida
"""
if __name__ == "__main__":
    jugador = Carriles()
    print(jugador.bienvenida)
    jugadores_dict = jugador.numero_carriles()
    print(jugadores_dict)



# preguntar marca carro
# preguntar cantidad km de la pista.
# los carriles van orden de llegada jugador1 con carril1, jugador2 con carril3, jugador3 con carril3

