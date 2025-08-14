from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=15) 
    text = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.id}: {self.title}'


class Categoty(models.Model):
    name = models.CharField(max_length=20)