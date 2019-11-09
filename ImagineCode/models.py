from django.db import models


class Box(models.Model):

    id = models.CharField(max_length=20, primary_key=True)
    type = models.CharField(max_length=6)
    posX = models.FloatField()
    posY = models.FloatField()


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    quantity = models.IntegerField()
    box = models.ForeignKey(Box, on_delete=models.CASCADE)


class BoxToBox(models.Model):
    distance = models.FloatField(null=False)
    box1 = models.ForeignKey(Box, on_delete=models.DO_NOTHING, related_name='%(class)s_requests_created')
    box2 = models.ForeignKey(Box, on_delete=models.DO_NOTHING)


class Instruction(models.Model):
    id = models.AutoField(primary_key=True)
    action = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    quantity = models.IntegerField()
    box = models.ForeignKey(Box, on_delete=models.CASCADE)
