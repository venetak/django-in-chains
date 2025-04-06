import uuid
from django.db import models

class Flower(models.Model):
    name = models.CharField(max_length=200)
    color = models.CharField(max_length=200)
    symbolism = models.TextField(max_length=1000)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)


class Track(models.Model):
    flower = models.ForeignKey(Flower, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)