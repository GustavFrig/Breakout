import pygame as pg
from constants import *
from level1 import Level_1

def level_meny():
    pg.init()

    vindu = pg.display.set_mode((VINDU_BREDDE, VINDU_HOYDE))
    clock = pg.time.Clock()

    FONT = pg.font.SysFont(None, 40)

    level1_rektangel = pg.Rect(50, 200, 50, 50)
    level2_rektangel = pg.Rect(250, 200, 50, 50)
    level3_rektangel = pg.Rect(450, 200, 50, 50)

    vindu.fill((BLACK))
    running = True
    while running:
        pg.display.set_caption("Level meny")
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            elif event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:  
                running = False
            elif event.type == pg.MOUSEBUTTONDOWN:
                if level1_rektangel.collidepoint(event.pos):
                    Level_1()
                elif level2_rektangel.collidepoint(event.pos):
                    pass
                elif level3_rektangel.collidepoint(event.pos):
                    pass

        vindu.fill((BLACK))
        
    
        vindu.blit(FONT.render("Level Meny", True, WHITE), (225,125))
        pg.draw.rect(vindu, BLUE, level1_rektangel)
        pg.draw.rect(vindu, RED, level2_rektangel)
        pg.draw.rect(vindu, YELLOW, level3_rektangel)

        vindu.blit(FONT.render("1", True, WHITE), (63, 210))
        vindu.blit(FONT.render("2", True, WHITE), (263, 210))
        vindu.blit(FONT.render("3", True, WHITE), (463, 210))


        pg.display.flip()
        clock.tick(60)

pg.quit()

