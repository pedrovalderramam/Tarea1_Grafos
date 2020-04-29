import numpy as np
import collections


# CLASES--------------------------------------------------------------------------------------
class Vertice:
    """
    Clase que modela un vértice
    """

    def __init__(self, clave):
        """
        Inicializa el grafo
        clave: identificador del vértice
        """
        self.id = clave
        # vertices a los que está conectado
        # es de la forma {'clave': ponderación}
        self.conectadoA = {}

    def agregarVecino(self, vecino, ponderacion=0):
        """
        Conecta este vertice, con el vértice 'vecino' (Vertice),
        con una arista de ponderación 'ponderación'
        """
        self.conectadoA[vecino] = ponderacion

    def __str__(self):
        """
        Muestra todas las conexiones que posee Vertice
        """
        return str(self.id) + ' conectado A: ' + str([x.id for x in self.conectadoA])

    def obtenerConexiones(self):
        """
        Obtiene todos los vertices a los que está conectado este vertice
        """
        return self.conectadoA.keys()

    def obtenerId(self):
        """
        Obtiene el id de este vertice
        """
        return self.id

    def obtenerPonderacion(self, vecino):
        """
        Obtiene la ponderación de este vertice con vertice "vecino" (Vertice)
        Retornará error el vertice no está conectado a Vecino
        """
        return self.conectadoA[vecino]


# ----------------------------------------------------------------------------------------------
class Grafo:
    """
    Clase que modela un oobjeto grafo, con vertices unidos con aristas pesadas.
    """

    def __init__(self):
        # vertices del grafo de la forma "clave_del_vertice": vertice (Vertice)
        self.listaVertices = {}
        # numero de vertics presentes
        self.numVertices = 0

        self.listaClaves = []
        self.listaClavesx = {}
        self.listaAdyacencia = []
        self.diccionarioSei = {}

    def agregarVertice(self, clave):
        """
        Recibe el id de un vertice a agregar al grafo, lo crea, y lo agrega al grafo
        """
        self.listaClaves.append(clave)
        self.diccionarioSei[clave] = {}

        # instancia un vertice
        nuevoVertice = Vertice(clave)
        # lo agrega a la lista de vertices
        self.listaVertices[clave] = nuevoVertice
        self.numVertices = self.numVertices + 1
        return nuevoVertice

    def obtenerVertice(self, n):
        """
        Retorna el vertice con clave "n"
        """
        if n in self.listaVertices:
            return self.listaVertices[n]
        else:
            return None

    def __contains__(self, n):
        """
        Verifica si el vertice con id "n" existe en el grafo
        """
        return n in self.listaVertices

    def agregarArista(self, de, hasta, costo=0):
        """
        Conecta el vertice con clave 'de' con el vertice con clave 'a', con un peso 'costo'
        """
        # Crea los vertices con clave 'de' y 'a' si no existen
        if de not in self.listaVertices:
            nv = self.agregarVertice(de)
        if hasta not in self.listaVertices:
            nv = self.agregarVertice(hasta)

        # conecta los vertices
        self.listaVertices[de].agregarVecino(self.listaVertices[hasta], costo)
        # self.listaVertices[a].agregarVecino(self.listaVertices[de], costo)

        self.listaAdyacencia.append(de)
        self.listaAdyacencia.append(hasta)
        self.listaAdyacencia.append(costo)
        # self.listaAdyacencia.append(hasta)
        # self.listaAdyacencia.append(de)
        # self.listaAdyacencia.append(peso)
        self.diccionarioSei[de][hasta] = costo
        # self.diccionarioSei[hasta][de]=peso



    def obtenerVertices(self):
        """
        retorna las claves de todos los vertices del grafo
        """
        return self.listaVertices.keys()

    def adya(self, verticeinicio):
        ady = []
        i = 0

        while i <= (len(self.listaAdyacencia) - 3):
            if self.listaAdyacencia[i] == verticeinicio:
                ady.append(self.listaAdyacencia[i + 1])
            i = i + 3
        return ady

    def BFS(self, s, t, parent):
        '''Returns true if there is a path from source 's' to sink 't' in
        residual graph. Also fills parent[] to store the path '''

        # Mark all the vertices as not visited
        visited = [False] * len(self.grafo)

        # Create a queue for BFS
        queue = collections.deque()

        # Mark the source node as visited and enqueue it
        queue.append(s)
        visited[s] = True

        # Standard BFS loop
        while queue:
            u = queue.popleft()

            # Get all adjacent vertices's of the dequeued vertex u
            # If an adjacent has not been visited, then mark it
            # visited and enqueue it
            for ind, val in enumerate(self.grafo[u]):
                if (visited[ind] == False) and (val > 0):
                    queue.append(ind)
                    visited[ind] = True
                    parent[ind] = u

        # If we reached sink in BFS starting from source, then return
        # true, else false
        return visited[t]

    def FordFulkerson(self, source, sink):

        source = self.listaClaves.index(source)
        sink = self.listaClaves.index(sink)
        # This array is filled by BFS and to store path
        self.grafo = self.matriz_adyacencia_pesos
        parent = [-1] * len(self.grafo)

        max_flow = 0  # There is no flow initially

        # Augment the flow while there is path from source to sink
        while self.BFS(source, sink, parent):

            # Find minimum residual capacity of the edges along the
            # path filled by BFS. Or we can say find the maximum flow
            # through the path found.
            path_flow = float("Inf")
            s = sink
            while s != source:
                path_flow = min(path_flow, self.grafo[parent[s]][s])
                s = parent[s]

            # Add path flow to overall flow
            max_flow += path_flow

            # update residual capacities of the edges and reverse edges
            # along the path
            v = sink
            while v != source:
                u = parent[v]
                self.grafo[u][v] -= path_flow
                self.grafo[v][u] += path_flow
                v = parent[v]

        return max_flow

    def DFS(self, origen, visitados=list()):
        ady = self.adya(origen)
        visitados.append(origen)
        for vertice in ady:
            if vertice in visitados:
                None
            else:
                self.DFS(vertice, visitados=visitados)
        return visitados

    def __iter__(self):
        """
        retorna un interador sobre todos los objetos Vertice del grafo
        """
        return iter(self.listaVertices.values())

    def __index__(self, value):
        return self.obtenerVertice(value)

    @property
    def matriz_adyacencia(self):
        matriz = []
        for x in self.listaClaves:
            fila = []
            for y in self.listaClaves:

                if self.listaVertices[y] in self.listaVertices[x].conectadoA:
                    vertice_y = self.obtenerVertice(y)

                    fila.append(1)
                else:
                    fila.append(0)
            matriz.append(fila)

        return np.array(matriz)

    @property
    def matriz_adyacencia_pesos(self):
        matriz = []
        for x in self.listaClaves:
            fila = []
            for y in self.listaClaves:

                if self.listaVertices[y] in self.listaVertices[x].conectadoA:
                    vertice_y = self.obtenerVertice(y)
                    print()
                    fila.append(self.obtenerVertice(x).conectadoA[vertice_y])

                else:
                    fila.append(0)
            matriz.append(fila)

        return matriz

    @property
    def es_conexo(self):
        origen = self.listaClaves[0]
        visitados = self.DFS(origen)

        conexo = True
        for vertice in self.listaClaves:
            if vertice in visitados:
                None
            else:
                conexo = False
        return conexo


    def mejor_camino(self, dicCostos, noRevisado):
        inf=999999
        node_masBarato = None
        masBarato = inf
        for node in noRevisado:
            if dicCostos[node] <= masBarato:
                masBarato = dicCostos[node]
                node_masBarato = node
        return node_masBarato

    def dijkstra(self, startVertice, endVertice):
        inf=999999
        costos = {}
        padres = {}
        grafosei = self.diccionarioSei
        for node in grafosei:
            costos[node] = inf
            padres[node] = {}

        costos[startVertice] = 0

        no_revisado = [node for node in costos]
        node = self.mejor_camino(costos, no_revisado)
        while no_revisado:
            # Esto es para debugear
            # print(f"No revisado: {no_revisado} ")
            soloCosto = costos[node]
            costoPequeño = grafosei[node]
            for contador in costoPequeño:
                if costos[contador] > soloCosto + costoPequeño[contador]:
                    costos[contador] = soloCosto + costoPequeño[contador]
                    padres[contador] = node
            no_revisado.pop(no_revisado.index(node))
            node = self.mejor_camino(costos, no_revisado)

        # Debug

        #print(f"Costos: {costos}")
        #print(f"El costo para ir desde {startVertice} a {endVertice} es: {costos[endVertice]}")


        costo_final = costos[endVertice]

        # Imprimir

        if costos[endVertice] < inf:
            camino = [endVertice]
            i = 0
            while startVertice not in camino:
                camino.append(padres[camino[i]])
                i += 1
            camino_final = camino[::-1]
        else:
            camino_final = None

        return costo_final, camino_final

    def n_caminos(self, n):

        granfila = []
        for x in self.listaClaves:
            fila = []
            for y in self.listaClaves:

                if self.listaVertices[y] in self.listaVertices[x].conectadoA:
                    fila.append(1)

                else:

                    fila.append(0)
            granfila.append(fila)

            # matriz=np.append(matriz,np.array[fila])
            print("")
        matriz = np.array(granfila)

        matriz_elevada = np.linalg.matrix_power(matriz, n)
        print("Matriz Elevada a ", n)

        print(matriz_elevada)

        sumador = 0

        # (vertice_inicial, vertice_final, numero_caminos)
        resultados = []
        for f in range(len(self.listaClaves)):

            for c in range(len(self.listaClaves)):
                c_modificado = c + sumador

                if c_modificado <= (len(self.listaClaves) - 1):
                    # print ("(",f,",",c_modificado,")")
                    # print(matriz_elevada[f][c_modificado])
                    if matriz_elevada[f][c_modificado] != 0:
                        resultados.append((self.listaClaves[f], self.listaClaves[c_modificado], matriz_elevada[f][c_modificado]))
                        print("Entre ", self.listaClaves[f], " y ", self.listaClaves[c_modificado], " hay ",
                              matriz_elevada[f][c_modificado], " caminos de largo ", n)
            sumador = sumador + 1

        return resultados

    # A utility function to print the constructed MST stored in parent[]
    def printMST(self, parent):
        resultado = []
        print("Edge \tWeight")
        for i in range(1, len(self.graph)):
            inicio = self.listaClaves[parent[i]]
            final = self.listaClaves[i]
            resultado.append((inicio, final, self.graph[parent[i]][i]))
            print(parent[i], "-", i, "\t", self.graph[parent[i]][i])
        return resultado

    # A utility function to find the vertex with
    # minimum distance value, from the set of vertices
    # not yet included in shortest path tree
    def minKey(self, key, mstSet):

        # Initilaize min value
        min = float('inf')

        for v in range(len(self.graph)):
            if key[v] < min and mstSet[v] == False:
                min = key[v]
                min_index = v

        return min_index

        # Function to construct and print MST for a graph

    # represented using adjacency matrix representation
    def primMST(self):
        self.graph = self.matriz_adyacencia_pesos
        print(self.graph)

        # Key values used to pick minimum weight edge in cut
        key = [float('inf')] * len(self.graph)
        parent = [None] * len(self.graph)  # Array to store constructed MST
        # Make key 0 so that this vertex is picked as first vertex
        key[0] = 0
        mstSet = [False] * len(self.graph)

        parent[0] = -1  # First node is always the root of

        for cout in range(len(self.graph)):

            # Pick the minimum distance vertex from
            # the set of vertices not yet processed.
            # u is always equal to src in first iteration
            u = self.minKey(key, mstSet)

            # Put the minimum distance vertex in
            # the shortest path tree
            mstSet[u] = True

            # Update dist value of the adjacent vertices
            # of the picked vertex only if the current
            # distance is greater than new distance and
            # the vertex in not in the shotest path tree
            for v in range(len(self.graph)):
                # graph[u][v] is non zero only for adjacent vertices of m
                # mstSet[v] is false for vertices not yet included in MST
                # Update the key only if graph[u][v] is smaller than key[v]
                if self.graph[u][v] > 0 and mstSet[v] == False and key[v] > self.graph[u][v]:
                    key[v] = self.graph[u][v]
                    parent[v] = u

        resultado = self.printMST(parent)
        return resultado



