from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    favorite_animal = models.CharField(max_length=100, default="Pies")

    def __str__(self):
        return f"{self.name} {self.surname}"