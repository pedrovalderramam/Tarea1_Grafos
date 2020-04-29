from django import forms
from django.contrib.postgres.forms import SimpleArrayField




class GrafoForm(forms.Form):
    n_vertices = forms.IntegerField(label="Número de vertices")
    n_aristas = forms.IntegerField(label="Número de aristas")
class VerticeForm(forms.Form):
    clave = forms.CharField(max_length=5)

class AristaForm(forms.Form):
    de = forms.CharField(max_length=5)
    hasta = forms.CharField(max_length=5)
    peso = forms.IntegerField()

class Dijkstra(forms.Form):
    vertice_inicial = forms.CharField(label="Vertice inicial")
    vertice_final = forms.CharField(label="Vértice final")

class N(forms.Form):
    n = forms.IntegerField(label='n')

class FulkersonForm(forms.Form):
    de = forms.CharField(max_length=5)
    hasta = forms.CharField(max_length=5)

