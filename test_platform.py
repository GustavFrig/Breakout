import pygame as pg
from constants import *

pg.init()

clock = pg.time.Clock()
clock = pg.time.Clock()

vindu = pg.display.set_mode((VINDU_BREDDE, VINDU_HOYDE))
pg.display.set_caption("Freeplay")

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
        
        if self.rect.colliderect(pg.Rect(platform.x, platform.y, platform.width, platform.height)):
            self.vy *= -1

    def tegn(self, vindu):
        pg.draw.rect(vindu, self.farge, self.rect)


class Platform(object):
    def __init__(self, farge, x, y:int) -> None:
        self.farge = farge 
        self.x = x
        self.y = y
        self.width = 100
        self.height = 1

    def oppdater(self):
        pos = pg.mouse.get_pos()
        self.x = pos[0] - (self.width/2)

    def tegn(self, vindu):
        pg.draw.rect(vindu, self.farge, (self.x, self.y, self.width, self.height))
        


sirkel = Ball(x=400, y=300, bredde=30, hoyde=30, farge=(255, 0, 0), vx=5, vy=5)
platform = Platform(farge=BLUE, x=500, y=500)

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
    
    platform.oppdater()
    platform.tegn(vindu)

  
    pg.display.flip()
    clock.tick(FPS)

pg.quit()