from rest_framework import serializers
from .models import Box, Instruction, Product


class BoxSerializer(serializers.ModelSerializer):
    class Meta:
        model = Box
        fields = ("id", "type", "pos")


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ("name", "quantity", "box")


class InstructionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instruction
        fields = ("id", "action", "name", "quantity", "box")
