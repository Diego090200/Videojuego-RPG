from models.personaje.personaje import Personaje
from typing import Dict
import pygame


class Sanador(Personaje):
    def __init__(self, hp, mp, st, pos_x, pos_y):
        self.__hp: int = hp
        self.__mp: int = mp
        self.__st: int = st
        self.__pos_x: int = pos_x
        self.__pos_y: int = pos_y
        self.__items: Dict[str, int] = {('Item 1', 5), ('Item 2', 4), ('Item 3', 2)}

    def izquierda(self):
        pass

    def derecha(self):
        pass

    def saltar(self):
        pass

    def golpear(self) -> float:
        pass

    def super_ataque(self) -> float:
        pass

    def revivir(self):
        pass
