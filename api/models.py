from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    birth_date = models.DateField()
    profile_picture = models.CharField(max_length=150)
    about_me = models.CharField(max_length=1000)
    status = models.CharField(max_length=500)
