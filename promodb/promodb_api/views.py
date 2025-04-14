from rest_framework import viewsets, permissions
# Create your views here.
from .models import Jogo
from .serializers import PromoSerializer


class PromoViewSet(viewsets.ModelViewSet):
    queryset = Jogo.objects.all()
    serializer_class = PromoSerializer