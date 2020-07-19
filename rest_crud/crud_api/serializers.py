from rest_framework import serializers
from crud_api.models import HeroDetails

class HeroSerializer(serializers.ModelSerializer):
    class Meta:
        model = HeroDetails
        fields = '__all__'
