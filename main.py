import pygame
from mecanicas.mechanical import Mechanical
from Abstrac_factory.factory import Factory
from Abstrac_factory.pvp_factory import PvpFactory
from Abstrac_factory.pc_factory import PCFactory
from mecanicas.seleccion import MechanicalSeleccion
from typing import List

pygame.init()
ancho = 800
alto = 400
screen = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption("Videojuego")
clock = pygame.time.Clock()
#  texto
test_font = pygame.font.SysFont("Curier", 29)
text_surface1 = test_font.render("PvP", False, "White")
text_surface2 = test_font.render("PC", False, "White")
text_surface3 = test_font.render("Salir", False, "White")
text_surface4 = test_font.render("Sanador", False, "White")
text_surface5 = test_font.render("Guerrero", False, "White")
text_surface6 = test_font.render("Mago", False, "White")

# Musica

pygame.mixer.music.load('Music/Pelea.mp3')

#  Puntajes
test_font2 = pygame.font.SysFont("Curier", 32)
puntajej1 = test_font2.render("Jugador 1:", False, "Red")
puntajej2 = test_font2.render("Jugador 2:", False, "Blue")
ganador_partida: str = ""

#  imagenes -- Estas son de prueba para ver como funciddddddddddddona esto
fondo_surface = pygame.image.load("Assets/Otros/Fondo_1.png").convert()
indice_fondo: int = 0

#  Fabricas y mecanicas de pantallas
fabrica: Factory = PvpFactory()
fabrica_pc: Factory = PCFactory()
mecanica: Mechanical = Mechanical()
mecanica_seleccion: MechanicalSeleccion = MechanicalSeleccion()
mecanica_seleccion_2: MechanicalSeleccion = MechanicalSeleccion()
personaje_1: int = 0
personaje_2: int = 0
creados: bool = False


def pantalla_inicio(text_surface1, text_surface2, text_surface3):
    fondo = pygame.image.load("Assets/Otros/Fondo_4.png").convert()
    screen.blit(fondo, (0, 0))
    if mecanica.eleccion == 1:
        text_surface2 = test_font.render("PC", False, "White")
        text_surface1 = test_font.render("PvP", False, "Cyan")
    elif mecanica.eleccion == 2:
        text_surface1 = test_font.render("PvP", False, "White")
        text_surface3 = test_font.render("Salir", False, "White")
        text_surface2 = test_font.render("PC", False, "Cyan")
    elif mecanica.eleccion == 3:
        text_surface2 = test_font.render("PC", False, "White")
        text_surface3 = test_font.render("Salir", False, "Cyan")
    screen.blit(text_surface1, (ancho / 3, alto / 3))
    screen.blit(text_surface2, (ancho / 3, alto / 3 + 50))
    screen.blit(text_surface3, (ancho / 3, alto / 3 + 100))


def imagenes_seleccion(texto: str):
    fondo = pygame.image.load("Assets/Otros/Fondo_4.png").convert()
    screen.blit(fondo, (0, 0))
    letra = pygame.font.SysFont("Curier", 30)
    texto = letra.render(texto, True, (0, 170, 228))
    rectangulo_texto = texto.get_rect()
    rectangulo_texto.centerx = 400
    rectangulo_texto.centery = 45
    screen.blit(texto, rectangulo_texto)
    imagen_1 = pygame.image.load("Assets/Sanador/Ataque.png").convert_alpha()
    imagen_1 = pygame.transform.scale(imagen_1, (100, 100))
    rec_imagen_1 = imagen_1.get_rect(topright=(ancho / 3 + 200, alto / 3 - 60))
    imagen_2 = pygame.image.load("Assets/Caballero/Ataque.png").convert_alpha()
    imagen_2 = pygame.transform.scale(imagen_2, (100, 100))
    rec_imagen_2 = imagen_2.get_rect(topright=(ancho / 3 + 200, alto / 3 + 45))
    imagen_3 = pygame.image.load("Assets/Mago/Ataque.png").convert_alpha()
    imagen_3 = pygame.transform.scale(imagen_3, (100, 100))
    rec_imagen_3 = imagen_3.get_rect(topright=(ancho / 3 + 200, alto / 3 + 160))
    screen.blit(imagen_1, rec_imagen_1)
    screen.blit(imagen_2, rec_imagen_2)
    screen.blit(imagen_3, rec_imagen_3)


def pantalla_seleccion(texto: str):
    pygame.mixer.music.play(5)
    global text_surface4, text_surface5, text_surface6
    imagenes_seleccion(texto)
    if mecanica_seleccion.eleccion == 1:
        text_surface4 = test_font.render("Sanador", False, "Cyan")
        text_surface5 = test_font.render("Guerrero", False, "White")
        text_surface6 = test_font.render("Mago", False, "White")
    elif mecanica_seleccion.eleccion == 2:
        text_surface4 = test_font.render("Sanador", False, "White")
        text_surface5 = test_font.render("Guerrero", False, "Cyan")
        text_surface6 = test_font.render("Mago", False, "White")
    elif mecanica_seleccion.eleccion == 3:
        text_surface4 = test_font.render("Sanador", False, "White")
        text_surface5 = test_font.render("Guerrero", False, "White")
        text_surface6 = test_font.render("Mago", False, "Cyan")
    screen.blit(text_surface4, (ancho / 3, alto / 3 - 40))
    screen.blit(text_surface5, (ancho / 3, alto / 3 + 50))
    screen.blit(text_surface6, (ancho / 3, alto / 3 + 150))


def pantalla_seleccion_2(texto: str):
    global text_surface4, text_surface5, text_surface6
    imagenes_seleccion(texto)
    text_surface4 = test_font.render("Sanador", False, "Cyan")
    text_surface5 = test_font.render("Guerrero", False, "White")
    text_surface6 = test_font.render("Mago", False, "White")
    if mecanica_seleccion_2.eleccion == 1:
        text_surface4 = test_font.render("Sanador", False, "Cyan")
        text_surface5 = test_font.render("Guerrero", False, "White")
        text_surface6 = test_font.render("Mago", False, "White")
    elif mecanica_seleccion_2.eleccion == 2:
        text_surface4 = test_font.render("Sanador", False, "White")
        text_surface5 = test_font.render("Guerrero", False, "Cyan")
        text_surface6 = test_font.render("Mago", False, "White")
    elif mecanica_seleccion_2.eleccion == 3:
        text_surface4 = test_font.render("Sanador", False, "White")
        text_surface5 = test_font.render("Guerrero", False, "White")
        text_surface6 = test_font.render("Mago", False, "Cyan")
    screen.blit(text_surface4, (ancho / 3, alto / 3 - 40))
    screen.blit(text_surface5, (ancho / 3, alto / 3 + 50))
    screen.blit(text_surface6, (ancho / 3, alto / 3 + 150))


def pantalla_pvp(personaje, rect_personaje, villano, rec_villano, daños):
    fondos = [
        "Assets/Otros/Fondo_1.png",
        "Assets/Otros/Fondo_2.png",
        "Assets/Otros/Fondo_3.png",
        "Assets/Otros/Fondo_2.png",
    ]
    fondo = pygame.image.load(fondos[int(indice_fondo)]).convert()
    screen.blit(fondo, (0, 0))
    screen.blit(personaje, rect_personaje)
    screen.blit(villano, rec_villano)

    # Puntajes
    puntaje1 = test_font.render(str(daños[1]), False, "White")
    puntaje2 = test_font.render(str(daños[0]), False, "White")
    screen.blit(puntajej1, (10, 10))
    screen.blit(puntajej2, (640, 10))
    screen.blit(puntaje1, (125, 12))
    screen.blit(puntaje2, (755, 12))

    pygame.draw.rect(screen, (255, 0, 0), (10, 40, 200, 10))
    pygame.draw.rect(screen, (255, 0, 0), (585, 40, 200, 10))
    pygame.draw.rect(screen, (0, 128, 0), (10, 40, daños[1], 10))
    pygame.draw.rect(screen, (0, 128, 0), (585, 40, daños[0], 10))


def modo1():
    global creados, indice_fondo
    # una vez terminada la partida, solo debemos cambiar el valor de mecanica.pantalla
    if creados:
        daños: List[int] = fabrica.daño()
        # impresion en pantalla
        indice_fondo += 0.02
        if int(indice_fondo) == 3:
            indice_fondo = 0
        pantalla_pvp(fabrica.jugadores[0].get_imagen(), fabrica.jugadores[0].get_rect(),
                     fabrica.jugadores[1].get_imagen(), fabrica.jugadores[1].get_rect(), daños)


def seleccionar_segundo():
    global personaje_2
    pantalla_seleccion_2('Selección personaje - Jugador 2')
    if mecanica_seleccion_2.personaje == 1:
        personaje_2 = 1
        modo1()
    elif mecanica_seleccion_2.personaje == 2:
        personaje_2 = 2
        modo1()
    elif mecanica_seleccion_2.personaje == 3:
        personaje_2 = 3
        modo1()


def pantalla_vencedor():
    test_font3 = pygame.font.SysFont("Curier", 48)
    test_font4 = pygame.font.SysFont("Curier", 32)
    vencedor = test_font3.render(f"Gana {ganador_partida}", False, "White")
    continuar = test_font4.render("Presione Enter para continuar", False, "White")
    screen.blit(continuar, (ancho / 2 - 125, 7 * alto / 8))
    screen.blit(vencedor, (ancho / 2 - 125, alto / 2 - 100))


while True:
    #  Movimiento (funciona debido a que inicializada la fabrica, están en false)
    if mecanica.pantalla == 1:
        if creados:
            fabrica.movimiento_de_jugadores()
            if fabrica.partida_terminada():
                pygame.mixer.music.stop()
                pantalla_vencedor()
    if mecanica.pantalla == 2:
        if creados:
            fabrica_pc.movimiento_de_jugadores()
            fabrica_pc.ataque_enemigo()
            if fabrica_pc.partida_terminada():
                pygame.mixer.music.stop()
                pantalla_vencedor()
    # manejo de eventos
    for event in pygame.event.get():
        mecanica.operar_evento(event)
        if mecanica.pantalla == 1:
            if personaje_1 == 0:
                mecanica_seleccion.operar_evento(event)
            elif personaje_1 != 0 and personaje_2 == 0:
                mecanica_seleccion_2.operar_evento(event)
            else:
                fabrica.operar_evento(event)
                if not fabrica.personajes_creados:
                    fabrica.crear_jugador(personaje_1)
                    fabrica.crear_rival(personaje_2)
                    creados = True
        if mecanica.pantalla == 2:
            if personaje_1 == 0:
                mecanica_seleccion.operar_evento(event)
            else:
                if not fabrica_pc.personajes_creados:
                    fabrica_pc.crear_jugador(personaje_1)
                    fabrica_pc.crear_rival()
                    creados = True
                fabrica_pc.operar_evento(event)
    # pantallas y acciones de impresion en ellas
    if mecanica.pantalla == 0:
        pantalla_inicio(text_surface1, text_surface2, text_surface3)
        fabrica.limpiar()
        fabrica_pc.limpiar()
        mecanica_seleccion.finalizdo()
        mecanica_seleccion_2.finalizdo()
        personaje_1 = 0
        personaje_2 = 0
        creados = False
    elif mecanica.pantalla == 1:
        if not creados:
            pantalla_seleccion('Selección personaje - Jugador 1')
            if mecanica_seleccion.personaje == 1:
                personaje_1 = 1
                seleccionar_segundo()
            elif mecanica_seleccion.personaje == 2:
                personaje_1 = 2
                seleccionar_segundo()
            elif mecanica_seleccion.personaje == 3:
                personaje_1 = 3
                seleccionar_segundo()
        elif creados and not fabrica.partida_terminada():
            modo1()
            if fabrica.partida_terminada():
                ganador_partida = fabrica.obtener_ganador()
                mecanica.finalizado = True
    elif mecanica.pantalla == 2:
        if not creados:
            pantalla_seleccion('Selección personaje - Jugador 1')
            if mecanica_seleccion.personaje == 1:
                personaje_1 = 1
            elif mecanica_seleccion.personaje == 2:
                personaje_1 = 2
            elif mecanica_seleccion.personaje == 3:
                personaje_1 = 3
        elif creados and not fabrica_pc.partida_terminada():
            daño: List[int] = fabrica_pc.daño()
            indice_fondo += 0.02
            if int(indice_fondo) == 3:
                indice_fondo = 0
            pantalla_pvp(fabrica_pc.jugadores[0].get_imagen(), fabrica_pc.jugadores[0].get_rect(),
                         fabrica_pc.jugadores[1].get_imagen(), fabrica_pc.jugadores[1].get_rect(), daño)
            if fabrica_pc.partida_terminada():
                ganador_partida = fabrica_pc.obtener_ganador()
                mecanica.finalizado = True
    pygame.display.update()
    clock.tick(60)
