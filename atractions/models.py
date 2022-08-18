from django.db import models

class Atractions(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    working_time = models.TextField()
    min_age = models.IntegerField()
    photo = models.ImageField(upload_to='atractions', null=True, blank=True)


    def __str__(self):
        return self.name