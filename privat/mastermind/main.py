import time
import pygame
pygame.init()

pygame.display.set_caption("Mastermind")      #navn på vindu
BREDDE, HOYDE = 900, 600
screen = pygame.display.set_mode((BREDDE, HOYDE))        #størrelse på vindu
bakgrunn = (255, 209, 200)

player_scale = 60,60
gp = 400
lp = 200
up = 50
ri = 100
pos01 = lp,gp
pos02 = lp+ri,gp
pos03 = lp+ri*2,gp
pos04 = lp+ri*3,gp

pos11 = gp+up,gp+up
pos12 = gp+up+ri,gp+up+ri
pos13 = gp+up+ri*2,gp+up+ri*2
pos14 = gp+up+ri*3,gp+up+ri*3

b1 = pygame.image.load('privat/mastermind/img/brikke1.webp').convert()
b1 = pygame.transform.scale(b1,player_scale)
b2 = pygame.image.load('privat/mastermind/img/brikke2.png').convert()
b2 = pygame.transform.scale(b2,player_scale)
b3 = pygame.image.load('privat/mastermind/img/brikke3.png').convert()
b3 = pygame.transform.scale(b3,player_scale)
b4 = pygame.image.load('privat/mastermind/img/brikke4.png').convert()
b4 = pygame.transform.scale(b4,player_scale)

def playerpros():

    screen.blit(b1, pos01)
    screen.blit(b2, pos02)
    screen.blit(b3, pos03)
    screen.blit(b4, pos04)

    map = [b1, b2, b3, b4]
    
def main():

    klokke = pygame.time.Clock()
    kjør = True
    while kjør == True:
        klokke.tick(60)
        pygame.display.flip()
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                kjør = False
        screen.fill(bakgrunn)
        playerpros()

    pygame.quit()
if __name__ == "__main__":
    main()