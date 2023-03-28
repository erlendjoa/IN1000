import pygame
from random import randint

pygame.display.set_caption("Pong")     
BREDDE, HOYDE = 900, 500
vindu = pygame.display.set_mode((BREDDE, HOYDE))       
bakgrunn = (225, 225, 225)
sort = (0, 0, 0)

pkort1 = pygame.Rect()


def main():
    klokke = pygame.time.Clock()
    kjør = True
    while kjør == True:
        klokke.tick(60)
        vindu.fill(bakgrunn)
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                kjør = False

        keys = pygame.key.get_pressed()

    pygame.quit()
if __name__ == "__main__":
    main()