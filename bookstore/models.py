from django.db import models

# Create your models here.
# Class 종료 후 한개 라인 띄우기
class Author(models.Model):
    seq = models.AutoField(primary_key=True)
    author_name = models.CharField(max_length=100)
    gender = models.BooleanField
    description = models.TextField
    
    class Meta:
        db_table = 'author'
 
 
class Book(models.Model):
    seq = models.AutoField(primary_key=True)
    book_name = models.CharField(max_length=200)
    description = models.TextField
    author_seq = models.ForeignKey(Author, on_delete=models.CASCADE, db_column='author_seq')
    
    class Meta:
        db_table = 'book'
