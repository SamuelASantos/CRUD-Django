from django.urls import path, include
from .views import home, salvar, atualizar, editar, deletar

urlpatterns = [
    path('', home, name='home'),
    path('salvar/', salvar, name='salvar'),
    path('atualizar/<int:id>', atualizar, name='atualizar'),
    path('editar/<int:id>', editar, name='editar'),
    path('deletar/<int:id>', deletar, name='deletar'),
]