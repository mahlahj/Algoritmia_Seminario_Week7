from algoritmos import distancia_euclidiana

class Particula:
    def __init__(self, Id = 0, origen_X = 0, origen_Y = 0, destino_X = 0, destino_Y = 0, velocidad = 0, rojo = 0, verde = 0, azul = 0, distancia = 0):
        self.__Id = Id
        self.__origenX = origen_X
        self.__origenY = origen_Y
        self.__destinoX = destino_X
        self.__destinoY = destino_Y
        self.__velocidad = velocidad
        self.__rojo = rojo
        self.__verde = verde
        self.__azul = azul
        self.__distancia = distancia_euclidiana(origen_X, origen_Y, destino_X, destino_Y)

    def __str__(self):
        cadenas = \
            'Id: ' + str(self.__Id) + '\n' +\
            'Origen en X: ' + str(self.__origenX) + '\n' +\
            'Origen en Y: ' + str(self.__origenY) + '\n' +\
            'Destino en X: ' + str(self.__destinoX) + '\n' +\
            'Destino en Y: ' + str(self.__destinoY) + '\n' +\
            'Velocidad: ' + str(self.__velocidad) + '\n' +\
            'Rojo: ' + str(self.__rojo) + '\n' +\
            'Verde: ' + str(self.__verde) + '\n' +\
            'Azul: ' + str(self.__azul) + '\n' +\
            'Distancia: ' + str(self.__distancia) + '\n'
        return str(cadenas)

    def to_dict(self):
        return {
            'id': self.__Id,
	        'origen_x': self.__origenX,
	        'origen_y': self.__origenY,
	        'destino_x': self.__destinoX,
	        'destino_y': self.__destinoY,
	        'velocidad': 0,
	        'red': self.__rojo,
	        'green': self.__verde,
	        'blue': self.__azul
        }

    def getId(self):
        return str(self.__Id)
    
    def getOrigen(self):
        return str( "(" + str(self.__origenX) + ", " + str(self.__origenY) + ")")
    
    def getDestino(self):
        return str("(" + str(self.__destinoX) + ", " + str(self.__destinoY) + ")")
    
    def getVelocidad(self):
        return str(self.__velocidad)
    
    def getColor(self):
        return str("(" + str(self.__rojo) + ", " + str(self.__verde) + ", " + str(self.__azul) + ")")
    
    def getDistancia(self):
        return str(self.__distancia)