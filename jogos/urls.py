from django.urls import path
from . import views

urlpatterns = [
    path('jogos/', views.listar_jogos),
    path('jogos/anunciados', views.listar_jogos_anunciados),
    path('jogos/pre-venda', views.listar_jogos_em_pre_venda),
    path('jogos/lancados', views.listar_jogos_lancados),
]