from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from reserva.models import Reserva
from base.models import Contato
from rest_api.serializers import AgendamentoModelSerializer, ContatoModelSerializer


# Create your views here.



class AgendamentoModelViewSet(ModelViewSet):
    queryset = Reserva.objects.all()
    serializer_class = AgendamentoModelSerializer
    
class ContatoModelViewSet(ModelViewSet):
    queryset = Contato.objects.all()
    serializer_class = ContatoModelSerializer