from rest_framework import serializers
from .models import Box, Instruction


class BoxSerializer(serializers.ModelSerializer):
    class Meta:
        model = Box
        fields = ("id", "type", "posX", "posY")


class InstructionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instruction
        fields = ("id", "action", "name", "quantity", "box")
