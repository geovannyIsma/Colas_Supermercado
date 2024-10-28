import random
from configuracion import ALTO, TAMANIO_CLIENTE

class Cliente:
    def __init__(self, num_articulos):
        self.num_articulos = num_articulos
        self.tiempo_pago = random.randint(15, 360)
        self.y = ALTO - TAMANIO_CLIENTE
