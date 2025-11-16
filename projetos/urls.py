from django.urls import path
from . import views

app_name = 'projetos'

urlpatterns = [
    path('', views.home, name='home'),
    path('projetos/', views.lista_projetos, name='lista_projetos'),
    path('projeto/<int:projeto_id>/', views.detalhes_projeto, name='detalhes_projeto'),
    path('meus-projetos/', views.meus_projetos, name='meus_projetos'),
]