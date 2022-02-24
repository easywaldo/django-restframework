from django.db import models

# Create your models here.
class Purchase(models.Model):
    purchase_user = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)