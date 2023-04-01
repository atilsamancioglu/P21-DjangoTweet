from django.db import models

# Create your models here.

class Tweet(models.Model):
    nickname = models.CharField(max_length=50)
    message = models.CharField(max_length=100)

    def __str__(self):
        return f"Tweet nick: {self.nickname} message: {self.message}"