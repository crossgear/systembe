from django import forms
from register.models import DetallesComprobantes
import django_filters

class SearchComprobante(django_filters.FilterSet):
    class Meta:
        model = DetallesComprobantes
        fields = ['id_comp', 'id_tarjetas', 'id_tipopago', 'cantidad', 'monto_pagado']
