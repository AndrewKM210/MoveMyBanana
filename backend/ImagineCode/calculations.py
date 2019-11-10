import math
from ImagineCode.models import Instruction, Box, Product


def calculate_instructions(productos_origen, productos_destino, distancias, inicio_usuario, producto_usuario):
    min_distancia = math.inf
    tupla_origen_destino = []
    for origen in productos_origen:
        destinos = (x for x in productos_destino if x.name == origen.name and x.quantity <= origen.quantity)

        for destino in destinos:
            key_id = origen.box.id + "-" + destino.box.id
            distancia_user = 0
            if inicio_usuario is not None:
                distancia_user = distancias.get(origen.box.id + "-" + inicio_usuario.box.id)
            if distancias.get(key_id) + distancia_user < min_distancia:
                min_distancia = distancias.get(key_id)
                tupla_origen_destino = [origen, destino]

    if min_distancia == math.inf:
        Instruction.objects.create(action="fin", name="fin", quantity=0, box=Box.objects.first())
    else:
        Instruction.objects.create(action="take", name=tupla_origen_destino[0].name, quantity=tupla_origen_destino[1]
                                   .quantity, box=tupla_origen_destino[0].box)
        Instruction.objects.create(action="put", name=tupla_origen_destino[1].name, quantity=tupla_origen_destino[1]
                                   .quantity, box=tupla_origen_destino[1].box)

        productos_destino.remove(tupla_origen_destino[1])

        tupla_origen_destino[0].quantity = tupla_origen_destino[0].quantity - tupla_origen_destino[1].quantity

        if tupla_origen_destino[0].quantity == 0:
            productos_origen.remove(tupla_origen_destino[0])
        else:
            productos_origen[productos_origen.index(tupla_origen_destino[0])].quantity = tupla_origen_destino[0].quantity

        calculate_instructions(productos_origen, productos_destino, distancias, tupla_origen_destino[1], None)


def calculate_distances(origin_boxes, target_boxes):
    distancias = {}
    for origin_box in origin_boxes:
        for target_box in target_boxes:
            distancias.update({origin_box.id + "-" + target_box.id: abs(target_box.pos-origin_box.pos)})
    return distancias


def recalculate_instructions():
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
            products_origin.append(Product(name=product.get("name"), quantity=product.get("quantity")
                                           , box=box))
        else:
            boxes_target.append(box)
            products_target.append(Product(name=product.get("name"), quantity=product.get("quantity")
                                           , box=box))

    distances = calculate_distances(boxes_origin, boxes_target)
    calculate_instructions(products_origin, products_target, distances, None, None)
