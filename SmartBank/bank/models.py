from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class BankAccount(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    balance = models.FloatField(default=0.0)

    def __str__(self):
        return f"{self.user.username}'s account"
