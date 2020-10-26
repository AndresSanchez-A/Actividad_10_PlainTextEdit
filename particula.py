from algoritmos import distancia_euclidiana

class Particula:
    def __init__(self, identificador=0, originx=0 , origeny=0, destinox=0, destinoy=0, velocidad=0, red=0, green=0, blue=0):
        self.__id = identificador
        self.__origen_x = originx
        self.__origen_y = origeny
        self.__destino_x = destinox
        self.__destino_y = destinoy
        self.__velocidad = velocidad
        self.__red = red
        self.__green = green
        self.__blue = blue
        self.__distancia = distancia_euclidiana(originx, origeny, destinox, destinoy)
    
    #converitir objeto libro a String(cadena)
    def __str__(self):
        return (
            'ID: ' + str(self.__id)+'\n' +
            'Origen en x: ' + str(self.__origen_x) +'\n' +
            'Origen en y: ' + str(self.__origen_y) +'\n' +
            'Destino en x: ' + str(self.__destino_x) +'\n' +
            'Destino en y: ' + str(self.__destino_y) +'\n' +
            'Velocidad: ' + str(self.__velocidad) +'\n' +
            'Red: ' + str(self.__red) +'\n' +
            'Green: ' + str(self.__green) +'\n' +
            'Blue: ' + str(self.__blue) +'\n' +
            'Distancia: ' + str(self.__distancia) +'\n'
        )