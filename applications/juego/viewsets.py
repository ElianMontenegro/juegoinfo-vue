from rest_framework import viewsets
from .models import Juego
from .serializers import JuegoSerializer


class JuegoViewSet(viewsets.ModelViewSet):
    queryset = Juego.objects.all()
    serializer_class = JuegoSerializer