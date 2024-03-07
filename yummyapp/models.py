from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=200)
    email = models.EmailField()
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.username

class Login(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.username