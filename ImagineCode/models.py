from django.db import models


class Box(models.Model):
    id = models.CharField(max_length=20, primary_key=True)
    type = models.CharField(max_length=6)
    pos = models.IntegerField()


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    quantity = models.IntegerField()
    box = models.ForeignKey(Box, on_delete=models.CASCADE)


class Instruction(models.Model):
    id = models.AutoField(primary_key=True)
    action = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    quantity = models.IntegerField()
    box = models.ForeignKey(Box, on_delete=models.CASCADE)
