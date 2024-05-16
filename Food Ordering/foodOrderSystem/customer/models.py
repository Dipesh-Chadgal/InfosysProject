from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    is_user = models.BooleanField(default=False)
    is_restaurant = models.BooleanField(default=False)


class customerUser(CustomUser):
    name = models.CharField(max_length=50)

    
class Feedback(models.Model):
    stars = models.IntegerField()
    comments = models.TextField()

