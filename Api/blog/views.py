from django.shortcuts import render
from requests import Response
from rest_framework import generics
from rest_framework.decorators import api_view

from blog.models import Book
from blog.serializers import BookSerializer


# Create your views here.


class BookListCreateAPIView(generics.ListCreateAPIView):
    queryset = Book.objets.all()
    serializer_class = BookSerializer
class BookListApi(generics.ListAPIView):
    queryset = Book.objets.all()
    serializer_class = BookSerializer
class BookupdateDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objets.all()
    serializer_class = BookSerializer
class BookDetailAPIView(generics.RetrieveAPIView):
    queryset = Book.objets.all()
    serializer_class = BookSerializer
class BookDeleteAPIView(generics.DestroyAPIView):
    queryset = Book.objets.all()
    serializer_class = BookSerializer
class BookupdateApiView(generics.UpdateAPIView):
    queryset = Book.objets.all()
    serializer_class = BookSerializer
class BookCreateApiView(generics.CreateAPIView):
    queryset = Book.objets.all()
    serializer_class = BookSerializer

@api_view(['GET'])
def book_list_view(request, *args, **kwargs):
    books =Book.objects.all()
    serializer = BookSerializer(books,many=True)
    return Response(serializer.data)