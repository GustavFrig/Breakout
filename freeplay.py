import pygame as pg
from constants import *
from objekt import *

def freeplay():
    pg.init()

    FPS = 60
    clock = pg.time.Clock()
    vindu = pg.display.set_mode((VINDU_BREDDE, VINDU_HOYDE))
    pg.display.set_caption("Freeplay")
    FONT = pg.font.SysFont(None, 40)


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


    poneg = "0"
    running = True
    while running:
        
        for event in pg.event.get():  
            if event.type == pg.QUIT:  
                running = False
            elif event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:  
                running = False
            elif str(len(klosser)*100) == poneg:
                ball.vx = 0
                ball.vy = 0
                # VIl at det skal komme en skjerm som sier at du vant og at man kan fortsetter/start nytt og back to lobby
        

        vindu.fill(WHITE)

        ball.oppdater()

        teller = FONT.render(poneg,True, (BLACK))
        vindu.blit(teller,(10,10))
        
        for kloss in klosser:
            if kloss.aktiv and ball.rect.colliderect(kloss.rect):
                poneg = int(poneg)
                poneg+=100
                poneg = str(poneg)
                kloss.aktiv = False
                ball.vy *= -1
                break
    
        if ball.rect.colliderect(platform.rect):
            if ball.rect.centerx < platform.rect.left or ball.rect.centerx > platform.rect.right:
                ball.vx *= -1
            elif ball.rect.centery < platform.rect.centery:
                ball.vy *= -1
                ball.rect.bottom = platform.rect.top
            else:
                ball.vy *= -1
    
    
        ball.tegn(vindu)
        for kloss in klosser:
            kloss.tegn(vindu)
  
        platform.oppdater()
        platform.tegn(vindu)

  
        pg.display.flip()
        clock.tick(FPS)

pg.quit()