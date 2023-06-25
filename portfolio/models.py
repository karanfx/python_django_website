from django.db import models

# Create your models here.

class test_menbers(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    
