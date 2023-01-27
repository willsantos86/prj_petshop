import json

from django.http import HttpResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, SAFE_METHODS

from reserva.models import Reserva

from base.models import Contato

from rest_api.serializers import AgendamentoModelSerializer, ContatoModelSerializer


# Create your views here.



class AgendamentoModelViewSet(ModelViewSet):
    queryset = Reserva.objects.all()
    serializer_class = AgendamentoModelSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    

class ContatoModelViewSet(ModelViewSet):

    serializer_class = ContatoModelSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        if self.request.method in SAFE_METHODS:
            return Contato.objects.all()
        return Contato.objects.filter(criado_por=self.request.user)

    def perform_create(self, serializer):
        if self.request.user.is_authenticated:
            serializer.save(criado_por=self.request.user)
        else:
            serializer.save()
