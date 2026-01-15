import pygame as pg
from constants import *

pg.init()


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

    def tegn(self, vindu):
        pg.draw.rect(vindu, self.farge, self.rect)

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
    vx=1,
    vy=1
)
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

  
    pg.display.update()

pg.quit()