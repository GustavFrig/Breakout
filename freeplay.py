import pygame as pg
from constants import *
from objekt import *

pg.init()

FPS = FPS
clock = pg.time.Clock()


vindu = pg.display.set_mode((VINDU_BREDDE, VINDU_HOYDE))
pg.display.set_caption("Freeplay")


class Rekt:
    def __init__(self, x, y, bredde, hoyde, farge):
        self.rect = pg.Rect(x, y, bredde, hoyde)
        self.farge = farge
        self.aktiv = True  # om klossen fortsatt finnes

    def tegn(self, vindu):
        if self.aktiv:
            pg.draw.rect(vindu, self.farge, self.rect)


ball = Ball(
    x=400,
    y=300,
    bredde=15,
    hoyde=15,
    farge=(255, 0, 0),
    vx=5,
    vy=5
)
platform = Platform(farge=BLUE, x=500, y=500)

for rad in range(ANTALL_RADER):
    for kol in range(ANTALL_KOLONNER):
        x = MARGIN + kol * (KLOSS_BREDDE + MARGIN)
        y = START_Y + rad * (KLOSS_HOYDE + MARGIN)
        klosser.append(
            Rekt(x, y, KLOSS_BREDDE, KLOSS_HOYDE, (0, 150, 255))
        )



running = True
while running:
    for event in pg.event.get():  
        if event.type == pg.QUIT:  
            running = False
        elif event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:  
            running = False

    vindu.fill(WHITE)

    ball.oppdater()
    for kloss in klosser:
        if kloss.aktiv and ball.rect.colliderect(kloss.rect):
            kloss.aktiv = False
            ball.vy *= -1
            break

    ball.tegn(vindu)
    for kloss in klosser:
        kloss.tegn(vindu)
    
    if ball.rect.colliderect(platform.x, platform.y, platform.width, platform.height):
        ball.vy *= -1
    

  
    platform.oppdater()
    platform.tegn(vindu)

  
    pg.display.flip()
    clock.tick(FPS)

pg.quit()