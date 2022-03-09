from django.db import models

class Professor(models.Model):
    sno = models.IntegerField(auto_created=True, primary_key=True)
    professor_name = models.CharField(max_length=100)
    created_dt = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'professor'


class Lecture(models.Model):
    sno = models.IntegerField(auto_created=True, primary_key=True)
    lecture_name = models.CharField(max_length=100)
    professor = models.ForeignKey(Professor, on_delete=models.PROTECT)
    created_dt = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'lecture'

    
class Student(models.Model):
    sno = models.IntegerField(auto_created=True, primary_key=True)
    student_name = models.CharField(max_length=100)
    created_dt = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'student'
    
    
class EnrollmentLecture(models.Model):
    sno = models.IntegerField(auto_created=True, primary_key=True)
    student_sno = models.ForeignKey(Student, on_delete=models.CASCADE)
    created_dt = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'enrollment_lecture'


