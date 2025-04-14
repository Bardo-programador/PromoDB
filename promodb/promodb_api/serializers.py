from rest_framework import serializers
from .models import Jogo
class PromoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jogo
        fields = '__all__'