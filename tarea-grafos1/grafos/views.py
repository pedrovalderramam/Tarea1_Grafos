from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import loader

from django.forms import formset_factory




from .models import Grafo

from .forms import GrafoForm, VerticeForm, AristaForm, Dijkstra, N, FulkersonForm

def pagina_inicio(request):
    template = loader.get_template('grafos/pagina_inicio.html')
    context = {}
    return HttpResponse(template.render(context, request))


def crear_grafo(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = GrafoForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            n_vertices = form.cleaned_data['n_vertices']
            n_aristas = form.cleaned_data['n_aristas']
            grafo = Grafo.objects.create(n_vertices=n_vertices, n_aristas=n_aristas)
            pk = grafo.id
            return HttpResponseRedirect(f'/grafos/crear-grafo/editar-vertices/{pk}')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = GrafoForm()

    return render(request, 'grafos/crear_grafo.html', {'form': form})

def vertices_grafo(request, id):
    grafo = Grafo.objects.get(id=id)
    n_vertices = grafo.n_vertices

    vertices_form_set = formset_factory(VerticeForm, extra=n_vertices )
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        vertices_form = vertices_form_set(request.POST)
        # check whether it's valid:
        if vertices_form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL
            vertices = '-'.join(form.cleaned_data['clave'] for form in vertices_form)
            grafo = Grafo.objects.get(id=id)
            grafo.vertices_labels = vertices
            grafo.save()

            return HttpResponseRedirect(f'/grafos/crear-grafo/editar-aristas/{id}')

    # if a GET (or any other method) we'll create a blank form
    else:
        vertices_form = vertices_form_set()

    return render(request, 'grafos/vertices_grafo.html', {'vertices_form': vertices_form})

def aristas_grafo(request, id):
    grafo = Grafo.objects.get(id=id)
    n_aristas = grafo.n_aristas

    aristas_form_set = formset_factory(AristaForm, extra=n_aristas )

    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        aristas_form = aristas_form_set(request.POST)
        # check whether it's valid:
        if aristas_form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL
            de = '-'.join(form.cleaned_data['de'] for form in aristas_form)
            hasta = '-'.join(form.cleaned_data['hasta'] for form in aristas_form)
            pesos = '-'.join(str(form.cleaned_data['peso']) for form in aristas_form)

            grafo = Grafo.objects.get(id=id)
            grafo.aristas_de = de
            grafo.aristas_hasta = hasta
            grafo.pesos = pesos
            grafo.save()

            return HttpResponseRedirect(f'/grafos/{id}')

    # if a GET (or any other method) we'll create a blank form
    else:
        aristas_form = aristas_form_set()

    return render(request, 'grafos/aristas_grafo.html', {'aristas_form': aristas_form})


def grafo_view(request, id):
    grafo = Grafo.objects.get(id=id)


    grafo = grafo.create_grafo()
    return render(request, 'grafos/grafo.html', {'grafo': grafo, 'id':id})

def matriz_adyacencia(request, id):
    grafo = Grafo.objects.get(id=id)
    grafo_obj = grafo.create_grafo()

    return render(request, 'grafos/matriz_adyacencia.html', {'grafo':grafo_obj, 'id':id})

def es_conexo(request, id):
    grafo = Grafo.objects.get(id=id)
    grafo_obj = grafo.create_grafo()

    return render(request, 'grafos/es_conexo.html', {'grafo': grafo_obj, 'id': id})

def dijkstra_view(request, id):


    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        dijkstra_form= Dijkstra(request.POST)
        # check whether it's valid:
        if dijkstra_form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL
            inicio =dijkstra_form.cleaned_data['vertice_inicial']
            final = dijkstra_form.cleaned_data['vertice_final']

            return HttpResponseRedirect(f'/grafos/{id}/dijkstra/{inicio}/{final}')

    # if a GET (or any other method) we'll create a blank form
    else:
        dijkstra_form = Dijkstra()

    return render(request, 'grafos/dijkstra_form.html', {'form': dijkstra_form})

def dijkstra_results(request, id, inicio, final):
    grafo = Grafo.objects.get(id=id)
    grafo = grafo.create_grafo()

    costo, camino = grafo.dijkstra(inicio, final)

    return render(request, 'grafos/dijkstra_results.html', {'camino':camino, 'costo':costo})

def ingresar_n(request, id):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        n_form = N(request.POST)
        # check whether it's valid:
        if n_form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL
            n = n_form.cleaned_data['n']

            return HttpResponseRedirect(f'/grafos/{id}/caminos-n/{n}')

    # if a GET (or any other method) we'll create a blank form
    else:
        n_form = N()

    return render(request, 'grafos/ingresar_n.html', {'form': n_form})


def n_caminos(request, id, n):
    grafo = Grafo.objects.get(id=id)

    grafo = grafo.create_grafo()

    resultados = grafo.n_caminos(n)

    return render(request, 'grafos/resultados_n_caminos.html', {'resultados':resultados, 'n':n})



def fulkerson_form(request, id):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = FulkersonForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL
            de = form.cleaned_data['de']
            hasta = form.cleaned_data['hasta']

            return HttpResponseRedirect(f'/grafos/{id}/ford-fulkerson/{de}/{hasta}')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = FulkersonForm()

    return render(request, 'grafos/fulkerson_form.html', {'form': form})

def Fulkerson(request, id, de, hasta):
    grafo = Grafo.objects.get(id=id)
    grafo = grafo.create_grafo()

    flujo = grafo.FordFulkerson(de, hasta)

    return render(request, 'grafos/fulkerson_resultados.html', {'de':de, 'hasta':hasta, 'flujo':flujo})

def Prim(request, id):
    grafo = Grafo.objects.get(id=id)
    grafo = grafo.create_grafo()

    resultados = grafo.primMST()
    return render(request, 'grafos/prim.html', {'resultados': resultados})













