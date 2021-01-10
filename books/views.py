from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView, RetrieveDestroyAPIView, RetrieveUpdateDestroyAPIView

from .serializer import booksSerializer
from .models import Books

class BooksListView(ListAPIView):
    queryset = Books.objects.all()
    serializer_class = booksSerializer

class BooksDetailsView(RetrieveUpdateDestroyAPIView):
    queryset = Books.objects.all()
    serializer_class = booksSerializer