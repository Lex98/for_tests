from django.db import models


# Create your models here.
class User(models.Model):
    user_name = models.CharField('Username', max_length=50)

    def __str__(self):
        return self.user_name


class Device(models.Model):
    title = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
