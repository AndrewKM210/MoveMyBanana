import math;


def calculate_intructions(productos_origen, productos_destino, distancias, inicio_usuario, producto_usuario):
    
    min_distancia = math.inf
    tupla_origen_destino = []
    for destino in productos_destino:
        origenes = (x for x in productos_origen if x.name == destino.name)
        for origen in origenes:
            if distancias[destino.box][origen.box] < min_distancia:
                min_distancia = distancias[destino.box][origen.box]
                tupla_origen_destino = [origen.box, destino.box]

        # Eliminar origen destino
        # Insertar instruccion


def calculate_distances(origin_boxes, target_boxes):
    return ''
