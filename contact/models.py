from django.db import models
import time

# Create your models here.
class cmmt(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=20)
    usr_inp = models.CharField(max_length=255)
    time = models.DateTimeField(auto_now_add=True,auto_now=False)