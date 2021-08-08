from django.shortcuts import render

# Create your views here.
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveUpdateAPIView,
    RetrieveDestroyAPIView
)

from .models import Juego
from .serializers import JuegoSerializer

class JuegosListApiView(ListAPIView):

    serializer_class = JuegoSerializer

    def get_queryset(self):
        kword = self.request.query_params.get('kword','')
    
        return Juego.objects.filter(
            name__icontains=kword,
        )

class JuegosCreateApiView(CreateAPIView):

    serializer_class = JuegoSerializer
    

    
class JuegosUpdateDetailApiView(RetrieveUpdateAPIView):
    queryset = Juego.objects.all()
    serializer_class = JuegoSerializer


class JuegosDeleteApiView(RetrieveDestroyAPIView):
    queryset = Juego.objects.all()
    serializer_class = JuegoSerializer