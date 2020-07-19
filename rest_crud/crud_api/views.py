from rest_framework import generics, viewsets
from crud_api.models import HeroDetails
from crud_api import serializers

# Create your views here.

class HeroList(generics.ListCreateAPIView):
    def get_queryset(self):
        quearyset = HeroDetails.objects.all()
        return quearyset
        
    def get_serializer_class(self):
        serializer_class = serializers.HeroSerializer
        return serializer_class

class HeroViewDetails(generics.RetrieveUpdateDestroyAPIView):
    def get_queryset(self):
        quearyset = HeroDetails.objects.all()
        return quearyset
        
    def get_serializer_class(self):
        serializer_class = serializers.HeroSerializer
        return serializer_class

