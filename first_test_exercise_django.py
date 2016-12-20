from django.db import models


class User(models.Model):
    """User model"""
    username = models.CharField('Username', max_length=50)

    def __str__(self):
        return self.username


class Device(models.Model):
    """Device model"""
    title = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
