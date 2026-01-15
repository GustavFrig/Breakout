import pygame as pg
from constants import *

pg.init()


vindu = pg.display.set_mode((VINDU_BREDDE, VINDU_HOYDE))
pg.display.set_caption("Freeplay")

class Sirkel:
    def __init__(self, x, y, radius, farge, vy):
        self.x = x
        self.y = y
        self.radius = radius
        self.farge = farge
        self.vy = vy

    def oppdater(self):
        self.y += self.vy
        if self.y > VINDU_HOYDE - self.radius: 
            self.vy *= -1  
            self.y = VINDU_HOYDE - self.radius  
        elif self.y <= 0 + self.radius:  
            self.vy *= -1  

    def tegn(self, vindu):
        pg.draw.circle(vindu, self.farge, (self.x, self.y), self.radius)


sirkel = Sirkel(x=400, y=300, radius=30, farge=(255, 0, 0), vy=5)

running = True
while running:
    for event in pg.event.get():  
        if event.type == pg.QUIT:  
            running = False
        elif event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:  
            running = False

    vindu.fill(WHITE)

    sirkel.oppdater()
    sirkel.tegn(vindu)

  
    pg.display.update()

pg.quit()