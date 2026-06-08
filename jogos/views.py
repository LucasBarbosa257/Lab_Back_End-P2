from django.http import JsonResponse
from .models import Jogo

def listar_jogos(request):
    jogos = Jogo.objects.all().values()

    return JsonResponse(list(jogos), safe=False)

def listar_jogos_anunciados(request):
    jogos = Jogo.objects.filter(status='anunciado').values()

    return JsonResponse(list(jogos), safe=False)

def listar_jogos_em_pre_venda(request):
    jogos = Jogo.objects.filter(status='pre_venda').values()

    return JsonResponse(list(jogos), safe=False)

def listar_jogos_lancados(request):
    jogos = Jogo.objects.filter(status='lancado').values()

    return JsonResponse(list(jogos), safe=False)