from django.urls import path

from . import views

urlpatterns = [
    path('', views.pagina_inicio, name='index'),
    path('/crear-grafo', views.crear_grafo, name='crear_grafo'),
    path(r'/crear-grafo/editar-vertices/<int:id>', views.vertices_grafo, name='vertices-grafo'),
    path(r'/crear-grafo/editar-aristas/<int:id>', views.aristas_grafo, name='aristas-grafo'),
    path(r'/<int:id>', views.grafo_view, name='grafo'),
    path(r'/<int:id>/matriz-adyacencia', views.matriz_adyacencia, name='matriz_adyacencia'),
    path(r'/<int:id>/es-conexo', views.es_conexo, name='es_conexo'),
    path(r'/<int:id>/dijkstra', views.dijkstra_view, name='dijkstra'),
    path(r'/<int:id>/dijkstra/<str:inicio>/<str:final>', views.dijkstra_results, name='dijkstra-results'),
    path(r'/<int:id>/caminos-n', views.ingresar_n, name='n'),
    path(r'/<int:id>/caminos-n/<int:n>', views.n_caminos, name='n_caminos'),
    path(r'/<int:id>/ford-fulkerson', views.fulkerson_form, name='fulkerson-form'),
    path(r'/<int:id>/ford-fulkerson/<str:de>/<str:hasta>', views.Fulkerson, name='fulkerson'),
    path(r'/<int:id>/prim', views.Prim, name='prim'),




]

