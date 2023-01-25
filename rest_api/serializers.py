
from rest_framework import serializers
from datetime import date
from reserva.models import Reserva
from base.models import Contato

class AgendamentoModelSerializer(serializers.ModelSerializer):

    def validated_data(self,value):
        hoje = date.today()
        if value < hoje:
            raise serializers.ValidationError('Não é possivel criar um evento com data no passado!')
        return value

    class Meta:
        model = Reserva
        fields = '__all__'


class ContatoModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contato
        fields = '__all__'