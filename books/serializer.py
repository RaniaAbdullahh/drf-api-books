
from rest_framework import serializers
from .models import Books
class booksSerializer(serializers.ModelSerializer):
    class Meta:
        fields =  ('author', 'title', 'description')
        model = Books