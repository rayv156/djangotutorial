from rest_framework import serializers
from myapi.models import Hero

class HeroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hero
        fields = '__all__'