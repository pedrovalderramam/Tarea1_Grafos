
import numpy as np


#CLASES--------------------------------------------------------------------------------------
class Vertice:
    def __init__(self,clave):
        self.id = clave
        self.conectadoA = {}

    def agregarVecino(self,vecino,ponderacion=0):
        self.conectadoA[vecino] = ponderacion

    def __str__(self):
        return str(self.id) + ' conectado A: ' + str([x.id for x in self.conectadoA])

    def obtenerConexiones(self):
        return self.conectadoA.keys()

    def obtenerId(self):
        return self.id

    def obtenerPonderacion(self,vecino):
        return self.conectadoA[vecino]
#----------------------------------------------------------------------------------------------
class Grafo:
    def __init__(self):
        self.listaVertices = {}
        self.numVertices = 0

    def agregarVertice(self,clave):
        self.numVertices = self.numVertices + 1
        nuevoVertice = Vertice(clave)
        self.listaVertices[clave] = nuevoVertice
        return nuevoVertice

    def obtenerVertice(self,n):
        if n in self.listaVertices:
            return self.listaVertices[n]
        else:
            return None

    def __contains__(self,n):
        return n in self.listaVertices

    def agregarArista(self,de,a,costo=0):
        if de not in self.listaVertices:
            nv = self.agregarVertice(de)
        if a not in self.listaVertices:
            nv = self.agregarVertice(a)

        self.listaVertices[de].agregarVecino(self.listaVertices[a], costo)
        #self.listaVertices[a].agregarVecino(self.listaVertices[de], costo)
    def obtenerVertices(self):
        return self.listaVertices.keys()

    def __iter__(self):
        return iter(self.listaVertices.values())


def separador():
    print(" ")
    print("------------------------")
    print(" ")
def Menu():
    print("Menu Principal:")
    print(" ")
    print("------------------------")
    print(" ")
    print("1) Matriz de adyacencia del grafo")
    print("2) Verificar si es Conexo")
    print("3) Cantidad de caminos de largo n entre cada par de Vertices")
    print("4) Aplicar algoritmo de Dijkstra")
    print("0) Salir")

def adya(verticeinicio):
        ady=[]
        i=0

        while i <= (len(listaAdyacencia)-3):
            if listaAdyacencia[i] == verticeinicio:

                        ady.append(listaAdyacencia[i+1])
            i=i+3
        return ady

def DFS(origen):


    ady=adya(origen)

    visitados.append(origen)
    for vertice in ady:
        if vertice in visitados:
            None
        else:

            DFS(vertice)
#------------------------------------ DIJKSTRA ----------------------------------------------------------

inf = 999999


def mejor_camino(dicCostos, noRevisado):
    node_masBarato = None
    masBarato = inf
    for node in noRevisado:
        if dicCostos[node] <= masBarato:
            masBarato = dicCostos[node]
            node_masBarato = node
    return node_masBarato


def dijkstra(grafosei, startVertice, endVertice):


    costos = {}
    padres = {}

    for node in grafosei:
        costos[node] = inf
        padres[node] = {}

    costos[startVertice] = 0

    no_revisado = [node for node in costos]
    node = mejor_camino(costos,no_revisado)
    while no_revisado:
        # Esto es para debugear
        #print(f"No revisado: {no_revisado} ")
        soloCosto = costos[node]
        costoPequeño = grafosei[node]
        for contador in costoPequeño:
            if costos[contador] > soloCosto + costoPequeño[contador]:
                costos[contador] = soloCosto + costoPequeño[contador]
                padres[contador] = node
        no_revisado.pop(no_revisado.index(node))
        node = mejor_camino(costos, no_revisado)

    # Debug

    print(f"Costos: {costos}")
    print(f"El costo para ir desde {startVertice} a {endVertice} es: {costos[endVertice]}")

    # Imprimir

    if costos[endVertice] < inf:
        camino = [endVertice]
        i = 0
        while startVertice not in camino:
            camino.append(padres[camino[i]])
            i += 1
        print(f"El camino más corto es {camino[::-1]}")
    else:
        print(f"Un camino no pudo ser encontrado")
