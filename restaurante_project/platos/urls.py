from django.urls import path
from . import views

urlpatterns = [
    path('',views.inicio, name='inicio'),
    path('platos/', views.lista_platos, name='lista_platos'),
    path('crear/', views.crear_plato, name='crear_plato'),
    path('editar/<int:id>/', views.editar_plato, name='editar_plato'),
    path('eliminar/<int:id>/', views.eliminar_plato, name='eliminar_plato'),
]

