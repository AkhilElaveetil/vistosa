from django.db import models


class User(models.Model):
    username = models.CharField(max_length=100)
    image = models.ImageField(upload_to='pics')
    desc = models.TextField()
    price = models.IntegerField
    offer = models.BooleanField(default=False)

