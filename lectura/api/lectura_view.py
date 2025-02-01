from rest_framework import viewsets
from lectura.models import Lectura
from rest_framework import serializers


# Create your views here.

class LecturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lectura
        fields = ('titulo', 'autor', 'resumen')

        


class LecturaViewSet(viewsets.ModelViewSet):
    queryset = Lectura.objects.all()
    serializer_class = LecturaSerializer