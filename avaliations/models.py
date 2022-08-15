from django.db import models
from django.contrib.auth.models import User


class Avaliation(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    comment = models.TextField(null=True, blank=True)
    score = models.DecimalField(decimal_places=1, max_digits=4)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username
