from django.db import models

# Create your models here.
class Question(models.Model):
    qno = models.IntegerField(primary_key=True,auto_created=True)
    que = models.CharField(max_length=200)
    optiona = models.CharField(max_length=100)
    optionb = models.CharField(max_length=100)
    optionc = models.CharField(max_length=100)
    optiond = models.CharField(max_length=100)
    answer = models.CharField(max_length=1)

class User(models.Model):
    username = models.CharField(max_length=15,primary_key=True)
    realname = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    role = models.CharField(max_length=12)