from rest_framework import serializers
from .models import Cat

class CatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cat
        fields = ['id', 'user', 'name', 'years', 'breed', 'img',]

