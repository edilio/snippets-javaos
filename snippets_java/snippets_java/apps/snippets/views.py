from django.shortcuts import render
from rest_framework import viewsets

from .models import Snippet
from .serializers import SnippetSerializer


class SnippetViewSet(viewsets.ModelViewSet):
    model = Snippet
    serializer_class = SnippetSerializer
    queryset = Snippet.objects.all()