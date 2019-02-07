from django.shortcuts import render

from core.serializers import BeerSerializer

from rest_framework import generics

from rest_framework import permissions


# Create your views here.
class BeerListCreateView(generics.ListCreateAPIView):
    serializer_class = BeerSerializer
    queryset = BeerSerializer.Meta.model.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)