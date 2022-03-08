from turtle import title
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    def __repr__(self):
        return f"<User username={self.username}>"

    def __str__(self):
        return self.username

class books(models.Model):
    title = models.CharField(max_length=250)
    author = models.CharField(max_length=250)
    description = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)