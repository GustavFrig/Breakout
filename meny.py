import pygame as pg
from constants import *
from freeplay import freeplay

pg.init()

vindu = pg.display.set_mode((VINDU_BREDDE, VINDU_HOYDE))
pg.display.set_caption("Meny")
clock = pg.time.Clock()

FONT = pg.font.SysFont(None, 40)

freeplay_rektangel = pg.Rect(200, 120, 200, 50)
level_rektangel = pg.Rect(200, 200, 200, 50)

running = True
while running:
    pg.display.set_caption("Meny")
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.MOUSEBUTTONDOWN:
            if freeplay_rektangel.collidepoint(event.pos):
                freeplay()
            if level_rektangel.collidepoint(event.pos):
                pass

    
    vindu.fill((BLACK))
    

    pg.draw.rect(vindu, BLUE, freeplay_rektangel)
    pg.draw.rect(vindu, RED, level_rektangel)

    vindu.blit(FONT.render("Breakout", True, WHITE), (225,35))
    vindu.blit(FONT.render("Freeplay", True, WHITE), (250, 135))
    vindu.blit(FONT.render("Levels", True, WHITE), (250, 215))


    pg.display.flip()
    clock.tick(60)

pg.quit()
