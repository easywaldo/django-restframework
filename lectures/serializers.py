from rest_framework import serializers
from lectures.models import Lecture, Professor

class ProfessorSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Professor
        fields = ['professor_name']

class LectureSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Lecture
        professor = ProfessorSerializer
        fields = ['lecture_name', 'professor']
        

