import pygame
from sys import exit
from Abstrac_factory.factory import Factory
from Abstrac_factory.pvp_factory import PvpFactory

pygame.init()
ancho = 800
alto = 400
screen = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption("Inmersion Quest")
clock = pygame.time.Clock()
#  texto
test_font = pygame.font.Font(None, 20)
text_surface1 = test_font.render("PvP", False, "White")
text_surface2 = test_font.render("PC", False, "White")
text_surface3 = test_font.render("Salir", False, "White")

#  imagenes -- Estas son de prueba para ver como funciddddddddddddona esto
fondo_surface = pygame.image.load("assets/fondo.jpg").convert()
piso_surface = pygame.image.load("assets/ch.png").convert()
piso_surface = pygame.transform.scale(piso_surface, (ancho, 50))

#  Personajes
fabrica: Factory = PvpFactory()
fabrica.crear_jugador(1)
fabrica.crear_rival(2)
personaje1 = fabrica.jugadores[0]
personaje2 = fabrica.jugadores[1]


def pantalla_inicio(text_surface1, text_surface2, text_surface3):
    if fabrica.eleccion == 1:
        text_surface2 = test_font.render("PC", False, "White")
        text_surface1 = test_font.render("PvP", False, "Cyan")
    elif fabrica.eleccion == 2:
        text_surface1 = test_font.render("PvP", False, "White")
        text_surface3 = test_font.render("Salir", False, "White")
        text_surface2 = test_font.render("PC", False, "Cyan")
    elif fabrica.eleccion == 3:
        text_surface2 = test_font.render("PC", False, "White")
        text_surface3 = test_font.render("Salir", False, "Cyan")
    screen.blit(text_surface1, (ancho / 3, alto / 3))
    screen.blit(text_surface2, (ancho / 3, alto / 3 + 50))
    screen.blit(text_surface3, (ancho / 3, alto / 3 + 100))


def pantalla_pvp(fondo, personaje, rect_personaje, villano, rec_villano):
    screen.blit(fondo, (0, 0))
    screen.blit(piso_surface, (0, 350))
    screen.blit(personaje, rect_personaje)
    screen.blit(villano, rec_villano)


while True:
    #  Movimiento
    if fabrica.presion_A:
        personaje1.rec_personaje.left -= 4
        if personaje1.rec_personaje.left == -4:
            personaje1.rec_personaje.left = 0
    if fabrica.presion_D:
        personaje1.rec_personaje.left += 4
        if personaje1.rec_personaje.left == 656:
            personaje1.rec_personaje.left = 652
    if fabrica.presion_izq:
        personaje2.rec_personaje.left -= 4
        if personaje2.rec_personaje.left == -4:
            personaje2.rec_personaje.left = 0
    if fabrica.presion_der:
        personaje2.rec_personaje.left += 4
        if personaje2.rec_personaje.left == 656:
            personaje2.rec_personaje.left = 652
    #  presión de teclas ---- Corregir esto, hay mecanicas que no debería ir ahí
    for event in pygame.event.get():
        fabrica.operar_evento(event)
    # golpes
    if personaje1.golpear(personaje2.get_rect(), fabrica.z_pressed):
        personaje2.recibir_daño(personaje1.st)
        # si se quiere comprobar, den un print del hp
    if personaje2.golpear(personaje1.get_rect(), fabrica.j_pressed):
        personaje1.recibir_daño(personaje2.st)

    # pantallas
    if fabrica.pantalla == 0:
        pantalla_inicio(text_surface1, text_surface2, text_surface3)
    elif fabrica.pantalla == 1:
        pantalla_pvp(fondo_surface, personaje1.get_imagen(), personaje1.get_rect(),
                     personaje2.get_imagen(), personaje2.get_rect())
    pygame.display.update()
    clock.tick(60)
