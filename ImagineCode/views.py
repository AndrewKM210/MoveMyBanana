from rest_framework import generics
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from rest_framework.utils import json

from ImagineCode.calculations import recalculate_instructions
from .models import Box, Product, Instruction
from ImagineCode.serializers import BoxSerializer, InstructionSerializer


class ListBoxes(generics.ListAPIView):

    queryset = ''

    def get(self, request, *args):
        serialized_boxes = BoxSerializer(Box.objects.all(), many=True)
        # Product.objects.get(pk=11165).delete()
        # Product.objects.create(name="Banana", quantity=3, box_id="O.2")
        return Response(serialized_boxes.data)


class ListInstructions(generics.ListAPIView):

    queryset = ''

    def get(self, request, *args):
        serialized_instructions = InstructionSerializer(Instruction.objects.all(), many=True)
        return Response(serialized_instructions.data)


class CreateBox(generics.CreateAPIView):

    def post(self, request, *args):
        box = json.loads(request.body.decode())
        box_type = "origin" if box.get("id").split('.')[0] == "O" else "target"
        box_foreign = Box.objects.create(id=box.get("id"), type=box_type, pos=box.get("pos"))
        products = box.get("products")
        for product in products:
            Product.objects.create(name=product.get("name"), quantity=product.get("quantity"), box=box_foreign)
        return Response('OK')


class CreateInstruction(generics.CreateAPIView):

    def post(self, request, *args):
        instruction = json.loads(request.body.decode())
        box = Box.objects.get(pk=instruction.get("box"))
        Instruction.objects.create(action=instruction.get("action"), name=instruction.get("name"), quantity=instruction
                                   .get("quantity"), box=box)
        return Response('OK')


class Resume(generics.ListAPIView):

    def get(self, request, *args):
        if Instruction.objects.all().count() == 0:
            try:
                recalculate_instructions()
                return Response(InstructionSerializer(Instruction.objects.first()).data)

            except Box.DoesNotExist:
                print("THERE ARE NO BOXES AVAILABE")
                return Response(None)

        else:
            return Response(InstructionSerializer(Instruction.objects.first()).data)


class TakeProduct(generics.UpdateAPIView):

    def post(self, request, *args):
        instruction = Instruction.objects.first()
        take_json = json.loads(request.body.decode())
        if instruction.box_id == take_json.get("id") and instruction.name == take_json.get("name") \
                and instruction.quantity == take_json.get("quantity") and instruction.action == "take":
            instruction.delete()
            product = Product.objects.get(name=take_json.get("name"), box_id=take_json.get("id"))
            product.quantity = product.quantity - int(take_json.get("quantity"))
            product.save()
            response = InstructionSerializer(Instruction.objects.first()).data
            response.update({"error": "false"})
            return Response(response)
        else:
            if instruction.box_id == take_json.get("id") and instruction.action == "take":
                return Response({"action": "review", "box": instruction.box_id})

            response = InstructionSerializer(Instruction.objects.first()).data
            response.update({"error": "true"})
            return Response(response)


class PutProduct(generics.UpdateAPIView):

    def post(self, request, *args):
        instruction = Instruction.objects.first()
        take_json = json.loads(request.body.decode())
        if instruction.box_id == take_json.get("id") and instruction.name == take_json.get("name") \
                and instruction.quantity == take_json.get("quantity") and instruction.action == "put":
            instruction.delete()
            product = Product.objects.get(name=take_json.get("name"), box_id=take_json.get("id"))
            product.quantity = product.quantity - int(take_json.get("quantity"))
            product.save()
            response = InstructionSerializer(Instruction.objects.first()).data
            response.update({"error": "false"})
            return Response(response)
        else:
            response = InstructionSerializer(Instruction.objects.first()).data
            response.update({"error": "true"})
            return Response(response)


class ReviewBox(generics.UpdateAPIView):

    def post(self, request, *args):
        take_json = json.loads(request.body.decode())
        Product.objects.get(box_id=take_json.get("id")).delete()
        Product.objects.create(name=take_json.get("name"), quantity=take_json.get("quantity"), box_id=take_json.get("id"))
        Instruction.objects.all().delete()
        recalculate_instructions()
        return Response(InstructionSerializer(Instruction.objects.first()).data)


class CreateTest(generics.UpdateAPIView):

    def post(self, request, *args):
        Box.objects.all().delete()
        Product.objects.all().delete()
        Instruction.objects.all().delete()
        Box.objects.create(id="O.1", type="origin", pos=1)
        Box.objects.create(id="O.2", type="origin", pos=2)
        Box.objects.create(id="O.3", type="origin", pos=3)
        Box.objects.create(id="D.1", type="target", pos=1)
        Box.objects.create(id="D.2", type="target", pos=2)
        Product.objects.create(name="platano", quantity=5, box_id="O.1")
        Product.objects.create(name="fresa", quantity=5, box_id="O.2")
        Product.objects.create(name="naranja", quantity=5, box_id="O.3")
        Product.objects.create(name="fresa", quantity=2, box_id="D.1")
        Product.objects.create(name="platano", quantity=3, box_id="D.1")
        Product.objects.create(name="platano", quantity=2, box_id="D.2")
        Product.objects.create(name="fresa", quantity=3, box_id="D.2")
        Product.objects.create(name="naranja", quantity=5, box_id="D.2")
        return Response("OK")