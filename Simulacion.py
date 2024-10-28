import time
import random
from configuracion import *
from Caja import Caja

def main():
    pantalla = inicializar_pygame()
    imagen_cliente = pygame.transform.scale(pygame.image.load('assets/cliente.png'), (TAMANIO_CLIENTE, TAMANIO_CLIENTE))
    imagen_caja = pygame.transform.scale(pygame.image.load('assets/caja.png'), (ANCHO_CAJA, ALTO_CAJA))

    caja_normal1 = Caja(100, 100)
    caja_normal2 = Caja(300, 100, es_experto=True)
    caja_normal3 = Caja(500, 100)
    caja_express = Caja(700, 100, es_express=True)

    NUM_CLIENTES = 15

    for _ in range(NUM_CLIENTES):
        num_articulos = random.randint(1, 50)
        if num_articulos <= LIMITE_ARTICULOS_EXPRESS:
            caja_express.agregar_cliente(num_articulos)
        else:
            if caja_normal1.longitud_cola() <= caja_normal2.longitud_cola():
                caja_normal1.agregar_cliente(num_articulos)
            elif caja_normal2.longitud_cola() <= caja_normal3.longitud_cola():
                caja_normal2.agregar_cliente(num_articulos)
            else:
                caja_normal3.agregar_cliente(num_articulos)

    corriendo = True
    while corriendo:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                corriendo = False

        pantalla.fill(BLANCO)

        # Dibujar y procesar cajas
        for caja in [caja_normal1, caja_normal2, caja_normal3, caja_express]:
            if caja.es_express:
                pygame.draw.rect(pantalla, (255, 215, 0), (caja.x, caja.y, 100, 50))
            else:
                pygame.draw.rect(pantalla, (0, 0, 255), (caja.x, caja.y, 100, 50))
            caja.procesar_clientes()
            pantalla.blit(imagen_caja, (caja.x, caja.y))
            caja.dibujar_cola(pantalla, imagen_cliente)
            caja.dibujar_tiempo_total(pantalla)

            # Dibujar cliente actual siendo atendido
            if caja.cliente_actual:
                y_cliente_actual = caja.y + ALTO_CAJA + DESPLAZAMIENTO_COLA + 10
                pantalla.blit(imagen_cliente, (caja.x + 10, y_cliente_actual))
                texto_articulos = pygame.font.Font(None, 24).render(f"Artículos: {caja.cliente_actual.num_articulos}", True,
                                                                    (32, 178, 170))
                pantalla.blit(texto_articulos, (caja.x + 10, y_cliente_actual - 25))

        pygame.display.flip()
        time.sleep(0.02)

    pygame.quit()

if __name__ == "__main__":
    main()