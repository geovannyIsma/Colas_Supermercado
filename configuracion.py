import pygame

ANCHO, ALTO = 1080, 720
BLANCO = (255, 255, 255)
TIEMPO_ESCANEO_NORMAL = 10
TIEMPO_ESCANEO_NORMAL_EXPERTO = 5
TIEMPO_ESCANEO_EXPRESS = 5
LIMITE_ARTICULOS_EXPRESS = 10
TAMANIO_CLIENTE = 40
ANCHO_CAJA, ALTO_CAJA = 80, 100
ESPACIO_COLA = 10
DESPLAZAMIENTO_COLA = 20

def inicializar_pygame():
    pygame.init()
    pantalla = pygame.display.set_mode((ANCHO, ALTO))
    pygame.display.set_caption("Simulación de Supermercado")
    return pantalla