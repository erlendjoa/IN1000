import pygame

pygame.display.set_caption("Pong")      #navn på vindu
BREDDE, HOYDE = 900, 500
vindu = pygame.display.set_mode((BREDDE, HOYDE))        #størrelse på vindu
bakgrunn = (225, 225, 225)
sort = (0, 0, 0)

fart = 5
hoyde, bredde = 180, 400

ball = pygame.image.load("privat/img/sortKvadrat.gif")
ball = pygame.transform.rotate(pygame.transform.scale(ball,(30, 30)), 0)
xHoyre = False
xVenstre = False
yOpp = False
yNed = False
spiller1 = pygame.image.load("privat/img/sortLinje1.png")
spiller1 = pygame.transform.rotate(pygame.transform.scale(spiller1,(hoyde, bredde)), 90)
spiller2 = pygame.image.load("privat/img/sortLinje2.png")
spiller2 = pygame.transform.rotate(pygame.transform.scale(spiller2,(hoyde, bredde)), 90)


def trekk_vindu(rect1, rect2, rect3):
        vindu.blit(spiller1,(rect1.x, rect1.y))
        vindu.blit(spiller2,(rect2.x, rect2.y))
        vindu.blit(ball,(rect3.x, rect3.y))
        pygame.display.update()

def playerMov1(keys, elem):
    if keys[pygame.K_w] and elem.y - fart > 0:
        elem.y -=fart
    elif keys[pygame.K_s] and elem.y + fart + hoyde < HOYDE:
        elem.y +=fart
def playerMov2(keys, elem):
    if keys[pygame.K_p] and elem.y - fart > 0:
        elem.y -=fart
    elif keys[pygame.K_l] and elem.y + fart + hoyde < HOYDE:
        elem.y +=fart



def main():

    linjeRekt1 = pygame.Rect(10, 100, 40, 40)
    linjeRekt2 = pygame.Rect(500, 100, 40, 40)
    ballRekt = pygame.Rect(450, 250, 40, 40)

    klokke = pygame.time.Clock()
    kjør = True
    while kjør == True:
        klokke.tick(60)
        vindu.fill(bakgrunn)
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                kjør = False

        keys = pygame.key.get_pressed()
        playerMov1(keys, linjeRekt1)
        playerMov2(keys, linjeRekt2)
        trekk_vindu(linjeRekt1, linjeRekt2, ballRekt)

    pygame.quit()
if __name__ == "__main__":
    main()