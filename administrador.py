from particula import Particula

class Administrador:
    #constructror
    def __init__(self):
        #atributo privado
        self.__particula = [] 
        #[] lista de elementos.

        #agregar al final.
    def agregar_final(self, particula:Particula): 
        self.__particula.append(particula) 
        #append:agregar lista en el final hasta agotar memoria.
        #append agrega elementos nuevos al final del programa

    def agregar_inicio(self, particula:Particula):
        self.__particula.insert(0, particula) 
        #insert: agregar elementos en el principio,
        #recibe dos parametros: posición de inicio "0", objeto "particula" que queremos guardar en esa posición.
        #insert recorre la posicion de los elementos para incluir el nuevo libro
        #al inicio de nuestra lista

    def mostrar(self):
        for particula in self.__particula: #inserta particulas en la posición nueva ingresada
            print(particula) #imprime los posiciones

    def __str__(self):
        # presentar en pantalla ('\n':salto de linea)(for...Repetir ciclo de posicion registrados)
        # ("":string vacío), (.join(): es un metodo que rebibe n cantidad de elementos para meter en el string)
        return "".join(str(particula) + '\n' for particula in self.__particula)