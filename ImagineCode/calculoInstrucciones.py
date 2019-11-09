import math;
#Box
    # type = models.CharField(max_length=6)
    # posX = models.FloatField()
    # posY = models.FloatField()

#producto
    # name = models.CharField(max_length=50)
    # quantity = models.IntegerField()
    # box = models.ForeignKey(Box, on_delete=models.CASCADE)

#Instrus
#    action = models.CharField(max_length=20)
    # name = models.CharField(max_length=20)
    # quantity = models.IntegerField()
    # box = models.ForeignKey(Box, on_delete=models.CASCADE)

def calculaInstrucciones(productos_origen, productos_destino, distancias, inicio_usuario, producto_usuario):
    
    min_distancia = math.inf
    tupla_origen_destino = []
    for destino in productos_destino:
        origenes = (x for x in productos_origen if x.name == destino.name)
        for origen in origenes:
            if distancias[destino.box][origen.box] < min_distancia:
                min_distancia = distancias[destino.box][origen.box]
                tupla_origen_destino = [origen.box, destino.box]
        ##Eliminar origen destino
        ##Insertar instruccion


    pass