from django.shortcuts import render
from rest_framework import viewsets

from lectures.serializers import LectureSerializer, ProfessorSerializer
from lectures.models import Lecture, Professor

# Create your views here.
class LectureViewSet(viewsets.ModelViewSet):
    queryset = Lecture.objects.all()
    serializer_class = LectureSerializer

    def perform_create(self, serializer):
        if serializer.is_valid(raise_exception=True):
            print('valid...')
            ##serializer.create(serializer.validated_data)  ## 저장 역할 수행
            print(serializer.validated_data)
            serializer.save()   ## 저장역할 수행
            
            
class ProfessorViewSet(viewsets.ModelViewSet):
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer
    
    def perform_create(self, serializer):
        if serializer.is_valid(raise_exception=True):
            serializer.save()
