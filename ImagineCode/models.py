from django.db import models


class Box(models.Model):

    id = models.CharField(max_length=20, null=False, primary_key=True)
    type = models.CharField(max_length=6, null=False)
    posX = models.FloatField(null=False)
    posY = models.FloatField(null=False)


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, null=False)
    quantity = models.IntegerField(null=False)
    box = models.ForeignKey(Box, on_delete=models.CASCADE)
