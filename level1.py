import pygame as pg
from constants import *
from objekt import *

def Level_1():
    pg.init()
    
    ball = Ball(
        x=400,
        y=300,
        bredde=15,
        hoyde=15,
        farge=(RED),
        vx=4.5,
        vy=5
    )
    ball2 = Ball(
        x=350,
        y=400,
        bredde=15,
        hoyde=15,
        farge=(PURPLE),
        vx=3,
        vy=4
    )
    platform = Platform(farge=BLUE, x=500, y=500)


    FPS = 60
    clock = pg.time.Clock()
    vindu = pg.display.set_mode((VINDU_BREDDE, VINDU_HOYDE))
    pg.display.set_caption("Level 1")
    FONT = pg.font.SysFont(None, 40)

    def skaperverket():
        klosser = []
        for rad in range(ANTALL_RADER):
            for kol in range(ANTALL_KOLONNER):
                x = MARGIN + kol * (KLOSS_BREDDE + MARGIN)
                y = START_Y + rad * (KLOSS_HOYDE + MARGIN)
                klosser.append(
                    Rekt(x, y, KLOSS_BREDDE, KLOSS_HOYDE, (0, 150, 255))
                )
        return klosser
    klosser = skaperverket()

    poneg = "0"
    running = True
    status = True
    
    meny_rektangel = pg.Rect(160, 220, 275, 50)
    
    
    while running:
        vindu.fill(WHITE)
        for event in pg.event.get():  
            if event.type == pg.QUIT:  
                running = False
            elif event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:  
                running = False
            elif event.type == pg.MOUSEBUTTONDOWN:
                if status == False:
                    if meny_rektangel.collidepoint(event.pos):
                        running = False
                    
       
        
        #Når man vinner
        if poneg == str(len(klosser)*100):
            ball.vx = 0
            ball.vy = 0
            
            ball2.vx = 0
            ball2.vy = 0
            
            status = False
            
            vindu.blit(FONT.render("DU VANT", True, BLACK), ((225),35))
            vindu.blit(FONT.render("Tilbake til menyen", True, BLACK), (175, 235))
            
            pg.draw.rect(vindu, BLACK, meny_rektangel, 2)
            
        ball.oppdater()
        ball2.oppdater()
        #Når man taper
        if ball.rect.bottom >= VINDU_HOYDE or ball2.rect.bottom >= VINDU_HOYDE:
            ball.rect.bottom = VINDU_HOYDE
            ball2.rect.bottom = VINDU_HOYDE
            
            status = False
            
            
            ball.vx = 0
            ball.vy = 0
            ball2.vx = 0
            ball2.vy = 0
            
            vindu.blit(FONT.render("DU TAPTE", True, BLACK), ((225),35))
            vindu.blit(FONT.render("Tilbake til menyen", True, BLACK), (175, 235))
            pg.draw.rect(vindu, BLACK, meny_rektangel, 2)

        teller = FONT.render(poneg,True, (BLACK))
        vindu.blit(teller,(10,10))
        
        #Ødeleggelsen av klosser
        for kloss in klosser:
            if kloss.aktiv and ball.rect.colliderect(kloss.rect):
                poneg = int(poneg)
                poneg+=100
                poneg = str(poneg)
                kloss.aktiv = False
                ball.vy *= -1
                break
            elif kloss.aktiv and ball2.rect.colliderect(kloss.rect):
                poneg = int(poneg)
                poneg+=100
                poneg = str(poneg)
                kloss.aktiv = False
                ball2.vy *= -1
                break
                
            
        #Hvor ballen bouncer
        if ball.rect.colliderect(platform.rect):
            if ball.vy > 0:
                ball.vy *= -1
                ball.rect.bottom = platform.rect.top
            else:
                ball.vx *= -1
        elif ball2.rect.colliderect(platform.rect):
            if ball2.vy > 0:
                ball2.vy *= -1
                ball2.rect.bottom = platform.rect.top
            else:
                ball2.vx *= -1
        
        #Kolisjon mellom ballene
        if ball.rect.colliderect(ball2.rect):
            ball.vx *= -1
            ball.vy *= -1
            ball2.vx *= -1
            ball2.vy *= -1
            
    
    
        #Status av spillet
        if status == True:
            ball.tegn(vindu)
            ball2.tegn(vindu)
            for kloss in klosser:
                kloss.tegn(vindu)
  
            platform.oppdater()
            platform.tegn(vindu)

  
        pg.display.flip()
        clock.tick(FPS)


pg.quit()