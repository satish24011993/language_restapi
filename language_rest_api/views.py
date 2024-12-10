from django.shortcuts import render
from .models import Language
from .serializers import LanguageSerializer
from rest_framework import viewsets

# Create your views here.
class LanguageViewset(viewsets.ModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer
