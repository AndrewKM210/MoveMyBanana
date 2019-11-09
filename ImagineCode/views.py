from rest_framework import generics
from rest_framework.response import Response
from rest_framework.utils import json

from ImagineCode.calculations import calculate_distances, calculate_intructions
from .models import Box, Product, Instruction
from ImagineCode.serializers import BoxSerializer, InstructionSerializer


class ListBoxes(generics.ListAPIView):

    queryset = ''

    def get(self, request, *args):
        serialized_boxes = BoxSerializer(Box.objects.all(), many=True)
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
        Instruction.objects.create(action=instruction.get("action"), name=instruction.get("name"), quantity=instruction.get("quantity"), box=box)
        return Response('OK')


class Resume(generics.ListAPIView):

    def get(self, request, *args):
        if Instruction.objects.all().count() == 0:
            try:
                products = Product.objects.all()
                products_values = products.values()
                products = [entry for entry in products_values]
                products_origin = []
                products_target = []
                boxes_origin = []
                boxes_target = []
                for product in products:
                    box = Box.objects.get(pk=product.get("box_id"))
                    if box.type == "origin":
                        boxes_origin.append(box)
                        products_origin.append(Product(name=product.get("name"), quantity=product.get("quantity"), box=box))
                    else:
                        boxes_target.append(box)
                        products_target.append(Product(name=product.get("name"), quantity=product.get("quantity"), box=box))

                distances = calculate_distances(boxes_origin, boxes_target)
                calculate_intructions(products_origin, products_target, distances, None, None)
                return Response(InstructionSerializer(Instruction.objects.first()).data)

            except Box.DoesNotExist:
                print("THERE ARE NO BOXES AVAILABE")
                return Response(None)

        else:
            return Response(InstructionSerializer(Instruction.objects.first()).data)


class TakeProduct(generics.UpdateAPIView):

    def post(self, request):
        id = ''





