from django.shortcuts import render
from api.serializers import FundoImobiliarioSerializers
from rest_framework import viewsets, permissions
from api.models import FundoImobiliarios

# Create your views here.

class FundoImobiliarioViewSet(viewsets.ModelViewSet):
    queryset = FundoImobiliarios.objects.all()
    serializer_class = FundoImobiliarioSerializers
    permission_class = ['permissions.IsAuthenticated']
