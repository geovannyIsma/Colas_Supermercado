from Cliente import Cliente
from configuracion import *

class Caja:
    def __init__(self, x, y, es_express=False, es_experto=False):
        self.x = x
        self.y = y
        self.cola = []
        self.es_express = es_express
        self.es_experto = es_experto
        self.tiempo_procesamiento = 0
        self.cliente_actual = None
        self.tiempo_total = 0
        self.num_clientes = 0

    def agregar_cliente(self, num_articulos):
        self.cola.append(Cliente(num_articulos))

    def longitud_cola(self):
        return len(self.cola)

    def procesar_clientes(self):
        if self.cliente_actual is None and self.cola:
            self.cliente_actual = self.cola.pop(0)
            self.num_clientes += 1
            if self.es_experto:
                tiempo_escanear = self.cliente_actual.num_articulos * TIEMPO_ESCANEO_NORMAL_EXPERTO
            else:
                tiempo_escanear = self.cliente_actual.num_articulos * (
                    TIEMPO_ESCANEO_EXPRESS if self.es_express else TIEMPO_ESCANEO_NORMAL)
            self.tiempo_procesamiento = tiempo_escanear + self.cliente_actual.tiempo_pago

        if self.cliente_actual is not None:
            self.tiempo_procesamiento -= 1
            if self.tiempo_procesamiento <= 0:
                self.tiempo_total += self.cliente_actual.num_articulos * (
                    TIEMPO_ESCANEO_EXPRESS if self.es_express else TIEMPO_ESCANEO_NORMAL) + self.cliente_actual.tiempo_pago
                self.cliente_actual = None

    def dibujar_cola(self, pantalla, imagen_cliente):
        for indice, cliente in enumerate(self.cola):
            cliente.y = self.y + DESPLAZAMIENTO_COLA + ALTO_CAJA + (indice + 1) * (TAMANIO_CLIENTE + ESPACIO_COLA)
            pantalla.blit(imagen_cliente, (self.x + 10, cliente.y))
            texto_articulos = pygame.font.Font(None, 24).render(f"Artículos: {cliente.num_articulos}", True,
                                                                (32, 178, 170))
            pantalla.blit(texto_articulos, (self.x + 10, cliente.y - 25))

    def dibujar_tiempo_total(self, pantalla):
        tiempo_total_minutos = self.tiempo_total // 60
        tiempo_total_segundos = self.tiempo_total % 60
        texto_tiempo = pygame.font.Font(None, 24).render(
            f"Tiempo total: {tiempo_total_minutos} min {tiempo_total_segundos} s", True, (0, 0, 0))
        pantalla.blit(texto_tiempo, (self.x, self.y - 30))
        texto_clientes = pygame.font.Font(None, 24).render(f"Clientes atendidos: {self.num_clientes}", True, (0, 0, 0))
        pantalla.blit(texto_clientes, (self.x, self.y - 60))