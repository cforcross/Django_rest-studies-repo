from django.db.models.query import QuerySet
from django.shortcuts import render
from rest_framework.generics import ListAPIView
from books.models import Book
from .serializers import BookSerializer
# Create your views here.


class BookAPIView(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
