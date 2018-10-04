from django.shortcuts import render
from register.models import DetallesComprobantes
from .filters import SearchComprobante
"""from register.models import Tarjetas, DetallesComprobantes, Comprobantes
from django.http import HttpResponse

def home(request):
    card = Tarjetas.objects.all()
    card_id = list()

    for c in card:
        card_id.append(c.uid)

    response_html = '<br>'.join(card_id)
    return HttpResponse(response_html)"""
def consulta(request):
    comp_list = DetallesComprobantes.objects.all()
    comp_filter = SearchComprobante(request.GET, queryset=comp_list)
    return render(request, 'prueba.html', {'filter':comp_list})


