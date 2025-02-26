from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    favorite_number = models.IntegerField()

    def __str__(self):
        return f"{self.name} {self.surname}"