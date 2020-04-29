
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

#------------------------------------------------------------------PROGRAMA PRINCIPAL----------------------------------------------------------------------------------------------------------------------------------------

_vertices=int(input("Ingrese la cantidad de Vertices: "))
_aristas=int(input("Ingrese la cantidad de Aristas: "))

# CREO EL OBJETO GRAFO

grafo=Grafo()

# CREO TANTOS VERTICES COMO DIGA EL USUARIO CON LA VARIABLE VERTICES

listaClaves=[]
listaClavesx={}
listaAdyacencia=[]
diccionarioSei={}

for x in range(_vertices):
    separador()
    print("VERTICE ", x+1 , " :")
    clave=input("Ingrese clave del vertice: ")
    listaClaves.append(clave)
    listaClavesx.update({clave:x+1})
    grafo.agregarVertice(clave)
    diccionarioSei[clave]={}



for a in range(_aristas):
    separador()
    print("ARISTA ", a+1 , " :")
    de=input("Desde: ")
    hasta=input("Hasta: ")
    peso=int(input("Peso: "))
    listaAdyacencia.append(de)
    listaAdyacencia.append(hasta)
    listaAdyacencia.append(peso)
    #listaAdyacencia.append(hasta)
    #listaAdyacencia.append(de)
    #listaAdyacencia.append(peso)
    diccionarioSei[de][hasta]=peso
    #diccionarioSei[hasta][de]=peso


    grafo.agregarArista(de,hasta,peso)

separador()
print("GRAFO CREADO EXITOSAMENTE")
separador()
print(listaClaves)
print(listaClavesx)
print(listaAdyacencia)
print("Vertices :" , end=" ")
print("")
for clave in listaClaves:
    print (clave,end=" ")
separador()
print("Conexiones: ")
print("")
for v in grafo:
    for w in v.obtenerConexiones():
        print("( %s , %s )" % (v.obtenerId(), w.obtenerId()))





input("ENTRAR AL PROGRAMA PRINCPAL")




exit=False
while exit==False:
    separador()
    Menu()

    alternativa=int(input("Ingrese alternativa aqui: "))
    if alternativa==1:
        separador()
        print("MATRIZ DE ADYACENCIA ")
        for x in listaClaves:

            for y in listaClaves:

                if grafo.listaVertices[y] in grafo.listaVertices[x].conectadoA :

                    print("1",end=" ")
                else:
                    print ("0",end=" ")
            print("")

        input("Presiona para volver al Menu...")

    if alternativa==2:
        visitados=[]
        origen=listaClaves[0]
        DFS(origen)

        conexo=True
        for vertice in listaClaves:
            if vertice in visitados:
                None
            else:
                conexo=False
        separador()
        if conexo==True:
            print("EL GRAFO ES CONEXO")

        else:
            print("EL GRAFO NO ES CONEXO")

        separador()
        input("Presiona para volver al menu Principal")

    if alternativa==3:
        separador()
        listaclaves2=listaClaves
        granfila=[]
        n=int(input("Ingrese largo de camino: "))
        for x in listaClaves:
            fila=[]
            for y in listaClaves:

                if grafo.listaVertices[y] in grafo.listaVertices[x].conectadoA :
                    fila.append(1)

                else:

                    fila.append(0)
            granfila.append(fila)

            #matriz=np.append(matriz,np.array[fila])
            print("")
        matriz=np.array(granfila)

        matriz_elevada = np.linalg.matrix_power(matriz, n)
        print("Matriz Elevada a ", n)
        separador()
        print(matriz_elevada)
        separador()


        sumador=0

        for f in range(len(listaClaves)) :

            for c in range(len(listaClaves)):
                c_modificado=c+sumador

                if c_modificado<=(len(listaClaves)-1):
                    #print ("(",f,",",c_modificado,")")
                    #print(matriz_elevada[f][c_modificado])
                    if matriz_elevada[f][c_modificado] != 0 :
                        print("Entre ",listaClaves[f], " y ", listaClaves[c_modificado]," hay ",matriz_elevada[f][c_modificado], " caminos de largo ", n )
            sumador=sumador+1




#---------------------------------------------DICCIONARIO ------------------------------------------------------------

    if alternativa==4:
        separador()
        separador()
        print("Algoritmo de Dijkstra para encontrar camino mas corto")
        separador()
        vertice_inicio=input("Ingrese el vértice de partida ")
        vertice_final=input("Ingrese el vértice final ")

        dijkstra(diccionarioSei, vertice_inicio, vertice_final)

    if alternativa==0:
        exit=True
