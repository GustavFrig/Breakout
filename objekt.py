import pygame as pg
from constants import *

class Platform(object):
    def __init__(self, farge, x, y:int) -> None:
        self.farge = farge 
        self.x = x
        self.y = y
        self.width = 100
        self.height = 20

    def oppdater(self):
        pos = pg.mouse.get_pos()
        self.x = pos[0] - (self.width/2)

    def tegn(self, vindu):
        pg.draw.rect(vindu, self.farge, (self.x, self.y, self.width, self.height))