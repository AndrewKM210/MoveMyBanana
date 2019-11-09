import math;

from ImagineCode.models import Instruction


def calculate_intructions(productos_origen, productos_destino, distancias, inicio_usuario, producto_usuario):
    
    min_distancia = math.inf
    for origen in productos_origen:
        destinos = (x for x in productos_destino if x.name == origen.name and x.quantity == origen.quantity)
        for destino in destinos:
            key_id = origen.box.id + "-" + destino.box.id
            if distancias.get(key_id) < min_distancia:
                min_distancia = distancias.get(key_id)
                tupla_origen_destino = [origen, destino]

    Instruction.objects.create(action="take", name=tupla_origen_destino[0].name, quantity=tupla_origen_destino[0].quantity, box=tupla_origen_destino[0].box)
    Instruction.objects.create(action="put", name=tupla_origen_destino[1].name, quantity=tupla_origen_destino[1].quantity, box=tupla_origen_destino[1].box)

    print(len(productos_origen))

    productos_origen.remove(tupla_origen_destino[0])
    productos_destino.remove(tupla_origen_destino[1])

    print(len(productos_origen))

    if len(productos_origen) > 0:
        print("WWEEEEEEEEEEE")
        calculate_intructions(productos_origen, productos_destino, distancias, None, None)


def calculate_distances(origin_boxes, target_boxes):
    distancias = {}
    for origin_box in origin_boxes:
        for target_box in target_boxes:
            distancias.update({origin_box.id + "-" + target_box.id: abs(target_box.pos-origin_box.pos)})
    return distancias
