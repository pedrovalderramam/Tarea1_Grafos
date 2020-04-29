from django.db import models
from .clases import Grafo as grafoInterno

class Grafo(models.Model):
    n_vertices = models.IntegerField()
    n_aristas = models.IntegerField()

    vertices_labels = models.CharField(max_length=100000, default='')
    aristas_de = models.CharField(max_length=100000, default='')
    aristas_hasta = models.CharField(max_length=100000, default='')
    pesos = models.CharField(max_length=100000, default='')

    id = models.AutoField(primary_key=True)

    def create_grafo(self):
        vertices_labels = self.vertices_labels.split('-')
        aristas_de = self.aristas_de.split('-')
        aristas_hasta = self.aristas_hasta.split('-')
        pesos = self.pesos.split('-')
        grafo = grafoInterno()
        for vertice in vertices_labels:
            grafo.agregarVertice(vertice)

        for de, hasta, peso in zip(aristas_de, aristas_hasta, pesos):
            try:

                peso = int(peso)
            except:
                raise Exception(peso)
            grafo.agregarArista(de, hasta, peso)

        return grafo
