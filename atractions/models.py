from django.db import models

class Atractions(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    working_time = models.TextField()
    min_age = models.IntegerField()

    def __str__(self):
        return self.name