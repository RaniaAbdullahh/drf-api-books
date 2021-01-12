from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView, RetrieveDestroyAPIView, RetrieveUpdateDestroyAPIView
from .permission import permission
from .serializer import booksSerializer
from .models import Books
from rest_framework.permissions import IsAuthenticated

class BooksListView(ListAPIView):
    queryset = Books.objects.all()
    serializer_class = booksSerializer
    permissions_classes = (permission,IsAuthenticated)

class BooksDetailsView(RetrieveUpdateDestroyAPIView):
    queryset = Books.objects.all()
    serializer_class = booksSerializer
    permissions_classes = (permission,IsAuthenticated)