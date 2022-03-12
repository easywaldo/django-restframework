from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

from rest_framework import status, viewsets

from bookstore.models import Author, Book
from bookstore.serializers import AuthroSerializer

# Create your views here.
@api_view(['GET', 'POST'])
def get_book_sample(request):
    print(request.data)
    serializer = AuthroSerializer(data=request.data)
    print(serializer.is_valid())
    return Response({"message": "Hello, world!!!"})

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthroSerializer
    
    def perform_create(self, serializer):
        print(serializer.validated_data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(serializer.data)
        
        