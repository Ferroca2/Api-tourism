from django.db import models
from atractions.models import Atractions
from comments.models import Comment
from avaliations.models import Avaliation
from addresses.models import Address

class TouristSpot(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    approved = models.BooleanField(default=False)
    atractions = models.ManyToManyField(Atractions)
    comments = models.ManyToManyField(Comment)
    avaliations = models.ManyToManyField(Avaliation)
    address =  models.ForeignKey(Address, on_delete=models.CASCADE, null=True, blank= True)
    photo = models.ImageField(upload_to='pontos_turisticos', null=True, blank=True)

    def __str__(self):
        return self.name
