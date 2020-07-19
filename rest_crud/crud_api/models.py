from django.db import models

# Create your models here.

class HeroDetails(models.Model):
    name = models.CharField(max_length=100)
    dob = models.DateTimeField(auto_now_add=True)
    age = models.CharField(max_length=3)
