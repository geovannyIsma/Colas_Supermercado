import time
import random
from configuracion import *
from Caja import Caja

def prueba_sin_caja_express():
    caja_normal1 = Caja(100, 100)
    caja_normal2 = Caja(300, 100, es_experto=True)
    caja_normal3 = Caja(500, 100)
    NUM_CLIENTES = 15

    for _ in range(NUM_CLIENTES):
        num_articulos = random.randint(1, 50)
        if caja_normal1.longitud_cola() <= caja_normal2.longitud_cola():
            caja_normal1.agregar_cliente(num_articulos)
        elif caja_normal2.longitud_cola() <= caja_normal3.longitud_cola():
            caja_normal2.agregar_cliente(num_articulos)
        else:
            caja_normal3.agregar_cliente(num_articulos)

    return [caja_normal1, caja_normal2, caja_normal3]


def prueba_caja_express_limite_normal():
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

    return [caja_normal1, caja_normal2, caja_normal3, caja_express]

def prueba_caja_express_limite_alto():
    caja_normal1 = Caja(100, 100)
    caja_normal2 = Caja(300, 100, es_experto=True)
    caja_normal3 = Caja(500, 100)
    caja_express = Caja(700, 100, es_express=True)

    LIMITE_ARTICULOS_EXPRESS_ALTO = 20
    NUM_CLIENTES = 15

    for _ in range(NUM_CLIENTES):
        num_articulos = random.randint(1, 50)
        if num_articulos <= LIMITE_ARTICULOS_EXPRESS_ALTO:
            caja_express.agregar_cliente(num_articulos)
        else:
            if caja_normal1.longitud_cola() <= caja_normal2.longitud_cola():
                caja_normal1.agregar_cliente(num_articulos)
            elif caja_normal2.longitud_cola() <= caja_normal3.longitud_cola():
                caja_normal2.agregar_cliente(num_articulos)
            else:
                caja_normal3.agregar_cliente(num_articulos)

    return [caja_normal1, caja_normal2, caja_normal3, caja_express]

def prueba_menos_cajas_normales():
    caja_normal1 = Caja(100, 100)
    caja_normal2 = Caja(300, 100, es_experto=True)
    caja_express = Caja(500, 100, es_express=True)
    NUM_CLIENTES = 15

    for _ in range(NUM_CLIENTES):
        num_articulos = random.randint(1, 50)
        if num_articulos <= LIMITE_ARTICULOS_EXPRESS:
            caja_express.agregar_cliente(num_articulos)
        else:
            if caja_normal1.longitud_cola() <= caja_normal2.longitud_cola():
                caja_normal1.agregar_cliente(num_articulos)
            else:
                caja_normal2.agregar_cliente(num_articulos)

    return [caja_normal1, caja_normal2, caja_express]

def prueba_mas_clientes():
    caja_normal1 = Caja(100, 100)
    caja_normal2 = Caja(300, 100, es_experto=True)
    caja_normal3 = Caja(500, 100)
    caja_express = Caja(700, 100, es_express=True)
    NUM_CLIENTES_ALTO = 30

    for _ in range(NUM_CLIENTES_ALTO):
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

    return [caja_normal1, caja_normal2, caja_normal3, caja_express]

def ejecutar_simulacion(cajas):
    pantalla = inicializar_pygame()
    imagen_cliente = pygame.transform.scale(pygame.image.load('assets/cliente.png'), (TAMANIO_CLIENTE, TAMANIO_CLIENTE))
    imagen_caja = pygame.transform.scale(pygame.image.load('assets/caja.png'), (ANCHO_CAJA, ALTO_CAJA))

    corriendo = True
    while corriendo:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                corriendo = False

        pantalla.fill(BLANCO)

        # Dibujar y procesar cada caja
        for caja in cajas:
            color = (255, 215, 0) if caja.es_express else (0, 0, 255)
            pygame.draw.rect(pantalla, color, (caja.x, caja.y, 100, 50))
            caja.procesar_clientes()
            pantalla.blit(imagen_caja, (caja.x, caja.y))
            caja.dibujar_cola(pantalla, imagen_cliente)
            caja.dibujar_tiempo_total(pantalla)

            # Dibujar cliente actual
            if caja.cliente_actual:
                y_cliente_actual = caja.y + ALTO_CAJA + 20
                pantalla.blit(imagen_cliente, (caja.x + 10, y_cliente_actual))
                texto_articulos = pygame.font.Font(None, 24).render(
                    f"Artículos: {caja.cliente_actual.num_articulos}", True, (32, 178, 170))
                pantalla.blit(texto_articulos, (caja.x + 10, y_cliente_actual - 25))

        pygame.display.flip()
        time.sleep(0.02)

    pygame.quit()

if __name__ == "__main__":
    print("Elige el caso de prueba:")
    print("1 - Sin caja express")
    print("2 - Caja express con límite de artículos normal")
    print("3 - Caja express con límite de artículos alto")
    print("4 - Menos cajas normales")
    print("5 - Más clientes")

    opcion = input("Introduce el número del caso de prueba: ")

    if opcion == "1":
        cajas = prueba_sin_caja_express()
    elif opcion == "2":
        cajas = prueba_caja_express_limite_normal()
    elif opcion == "3":
        cajas = prueba_caja_express_limite_alto()
    elif opcion == "4":
        cajas = prueba_menos_cajas_normales()
    elif opcion == "5":
        cajas = prueba_mas_clientes()
    else:
        print("Opción no válida")
        exit()

    ejecutar_simulacion(cajas)