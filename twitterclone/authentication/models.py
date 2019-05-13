from django.db import models

from django.contrib.auth.models import User

class UserProfile(models.Model):
    name = models.CharField(max_length=50)
    user = models.ManyToManyField(User, on_delete=models.CASCADE, blank=True)

        def __str__(self):
            return self.name