from rest_framework import viewsets, permissions
# Create your views here.
from .models import Jogo
from .serializers import PromoSerializer
from rest_framework.response import Response
from promodb.promodb_scrapper.steam_scrap import rodar_spider

class PromoViewSet(viewsets.ModelViewSet):
    queryset = Jogo.objects.all()
    serializer_class = PromoSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        if not queryset.exists():
            rodar_spider()  # chama sua função que executa a spider
            queryset = self.get_queryset()  # busca de novo após raspagem

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def get_view_name(self):
        return "Lista de Promoções Steam"