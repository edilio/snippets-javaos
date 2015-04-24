from rest_framework import serializers
from .models import Snippet


class SnippetSerializer(serializers.ModelSerializer):
    created_by = serializers.CharField(source='created_by.email', max_length=120, read_only=True)

    class Meta:
        model = Snippet
        fields = ("id", "title", "code", "linenos", "language", "style", "created_on", "created_by")