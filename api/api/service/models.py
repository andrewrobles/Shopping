from django.db import models

# Create your models here.
class Item(models.Model):
    item_name = models.CharField(max_length=100)
    description = models.TextField()
    amount = models.IntegerField()

