from django.db import models

# Create your models here.
class Dates(models.Model):
    studentName=models.CharField(max_length=20)
    studentID=models.IntegerField()
    email=models.CharField(max_length=30)
    contact=models.IntegerField()