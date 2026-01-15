import pygame as pg
from constants import *

class Platform(object):
    def __init__(self, farge, x, y:int) -> None:
        self.farge = farge 
        self.x = x
        self.y = y
        self.width = 100
        self.height = 20
        self.rect = pg.Rect(x, y, self.width, self.height)

    def oppdater(self):
        pos = pg.mouse.get_pos()
        self.x = pos[0] - (self.width/2)
        self.rect.x = self.x

    def tegn(self, vindu):
        pg.draw.rect(vindu, self.farge, self.rect)

class Ball:
    def __init__(self, x, y, bredde, hoyde, farge, vx, vy):
        self.x = x
        self.y = y
        self.rect = pg.Rect(x, y, bredde, hoyde)
        self.farge = farge
        self.vx = vx
        self.vy = vy

    def oppdater(self):
        self.rect.x += self.vx
        self.rect.y += self.vy

        if self.rect.bottom >= VINDU_HOYDE or self.rect.top <= 0:
            self.vy *= -1

        if self.rect.right >= VINDU_BREDDE or self.rect.left <= 0:
            self.vx *= -1
    

    def tegn(self, vindu):
        pg.draw.rect(vindu, self.farge, self.rect)

