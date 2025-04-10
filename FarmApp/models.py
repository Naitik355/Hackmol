from django.db import models
# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    city=models.CharField(max_length=100, blank=True)
    state=models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.username