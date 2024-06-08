#!/usr/bin/env python

######################################################################
## Desenvolvido por Gabriel Miranda Pedrosa (2010)
## Jogo baseado no SkiFree
######################################################################

import pygame, random, sys, os
from pygame.locals import *

WINDOWWIDTH = 640
WINDOWHEIGHT = 480
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FPS = 40
ANG = 2
game = 0
MAXSCENERY = 8
SCENERYCOUNTER = 0
RINGCOUNTER = 0
MAXRING = 30
ratedown = rateside = 0
moveRight = moveLeft = moveUp = moveDown = False
ringtest = 0
score = 0
rings = []
# o tempo do objetivo
seg = 0
count = 0


def terminate():
    pygame.quit()
    sys.exit()


def drawText(text, font, surface, x, y):
    textobj = font.render(text, 1, BLACK)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


def menuprincipal():
    while True:
        windowSurface.blit(telainicialImage, telainicialRect)
        windowSurface.blit(botao1Image, botao1Rect)
        windowSurface.blit(botao2Image, botao2Rect)
        windowSurface.blit(botao3Image, botao3Rect)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            # fazer o teste de colisao com cada botao com o mouse
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                if Rect.collidepoint(botao1Rect, (event.pos[0], event.pos[1])):
                    jogo()
                if Rect.collidepoint(botao2Rect, (event.pos[0], event.pos[1])):
                    instrucao()
                if Rect.collidepoint(botao3Rect, (event.pos[0], event.pos[1])):
                    terminate()


def telascore(score):
    while True:
        windowSurface.blit(telascoreImage, telascoreRect)
        windowSurface.blit(botaovoltarImage, botaovoltarRect)
        drawText("%s" % (score), fonte3, windowSurface, 330, 180)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == QUIT:
                return
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                if Rect.collidepoint(
                    botaovoltarRect, (event.pos[0], event.pos[1])
                ):
                    return


def telahighscore(score):
    while True:
        windowSurface.blit(telahighscoreImage, telahighscoreRect)
        windowSurface.blit(botaovoltarImage, botaovoltarRect)
        drawText("%s" % (score), fonte3, windowSurface, 270, 180)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == QUIT:
                return
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                if Rect.collidepoint(
                    botaovoltarRect, (event.pos[0], event.pos[1])
                ):
                    return


def instrucao():
    while True:
        windowSurface.blit(telainstrucaoImage, telainstrucaoRect)
        windowSurface.blit(botaovoltarImage, botaovoltarRect)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == QUIT:
                return
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                if Rect.collidepoint(
                    botaovoltarRect, (event.pos[0], event.pos[1])
                ):
                    return


def jogo():
    if not os.path.exists('topscore.txt'):
        highscore = 0
    else:
        doc = open("topscore.txt", "r")  # le arquivo de maiorpont
        highscore = int(doc.readline())

    WINDOWWIDTH = 640
    WINDOWHEIGHT = 480
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    FPS = 40
    ANG = 2
    game = 0
    MAXSCENERY = 8
    SCENERYCOUNTER = 0
    RINGCOUNTER = 0
    MAXRING = 30
    ratedown = rateside = 0
    moveRight = moveLeft = moveUp = moveDown = False
    ringtest = 0
    score = 0
    rings = []
    # o tempo do objetivo
    seg = 0
    count = 0
    tempo = 60
    while True:
        count += 1
        if count > 40:
            count = 0
            tempo -= 1

        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()

            if event.type == KEYDOWN:  # controles do ski
                if event.key == K_LEFT:
                    if ANG - 1 >= 0:
                        ANG -= 1

                if event.key == K_RIGHT:
                    if ANG + 1 <= 4:
                        ANG += 1

                if event.key == K_DOWN:
                    ANG = 2

            if event.type == KEYUP:
                if event.key == K_ESCAPE:
                    return

                if event.key == K_LEFT:
                    moveLeft = False
                if event.key == K_RIGHT:
                    moveRight = False
                if event.key == K_DOWN:
                    moveDown = False

        if tempo <= 0:
            ANG = 2

        if ANG == 0:
            ratedown = 0
            rateside = -2
        if ANG == 4:
            ratedown = 0
            rateside = 2
        if ANG == 1:
            ratedown = -5
            rateside = -4
        if ANG == 3:
            ratedown = -5
            rateside = 4
        if ANG == 2:
            ratedown = -7
            rateside = 0

        if tempo >= 0:
            skiRect.move_ip(rateside, 0)

            # pra nao deixar o ski passar da janela
            if skiRect.left < 0:
                skiRect.topleft = (0, 50)
                ANG = 2
            if skiRect.right > WINDOWWIDTH:
                skiRect.topright = (WINDOWWIDTH, 50)
                ANG = 2

            # Add new SCENERY IMAGES.
            if ratedown < 0:
                SCENERYCOUNTER += 1
            if SCENERYCOUNTER == MAXSCENERY:
                SCENERYCOUNTER = 0
                SCENERYINDICE = random.randint(0, 6)
                newSCENERYRect = scenery[SCENERYINDICE].get_rect()
                newSCENERYRect.topleft = (
                    random.randint(0, WINDOWWIDTH - 66),
                    480,
                )
                newSCENERY = {
                    "rect": newSCENERYRect,
                    "surface": scenery[SCENERYINDICE],
                    "indice": SCENERYINDICE,
                }

                sceneries.append(newSCENERY)

            # add new rings
            if ratedown < 0:
                RINGCOUNTER += 1
            if RINGCOUNTER == MAXRING:
                RINGCOUNTER = 0
                newRINGRect = ringImage.get_rect()
                newRINGRect.topleft = (
                    random.randint(0, WINDOWWIDTH - 66),
                    480,
                )
                newRING = {
                    "rect": newRINGRect,
                    "surface": ringImage,
                }
                rings.append(newRING)

        if tempo >= 4:
            # Move and remove scenery images.
            for s in sceneries[:]:
                s["rect"].move_ip(0, ratedown)
                if s["rect"].bottom < 0:
                    sceneries.remove(s)

            # Move and remove broken scenery images.
            for b in bsceneries[:]:
                b["rect"].move_ip(0, ratedown)
                if b["rect"].bottom < 0:
                    bsceneries.remove(b)

            # move and remove the rings
            for r in rings[:]:
                r["rect"].move_ip(0, ratedown)
                if r["rect"].bottom < 0:
                    rings.remove(r)

            # operacoes do score e quanto as imagens do cenario quebradas (exclui a que o player bateu e poe a quebrada 	no lugar)
            for s in sceneries[:]:
                if Rect.colliderect(s["rect"], skiRect):
                    bSCENERYRect = scenery[s["indice"] + 7].get_rect()
                    bSCENERYRect.bottomleft = s["rect"].bottomleft
                    newbSCENERY = {
                        "rect": bSCENERYRect,
                        "surface": scenery[s["indice"] + 7],
                        "indice": SCENERYINDICE,
                    }
                    bsceneries.append(newbSCENERY)
                    sceneries.remove(s)
                    if tempo > 0:
                        score -= 50
                for r in rings:
                    if Rect.colliderect(r["rect"], skiRect):
                        rings.remove(r)
                        if tempo > 0:
                            score += 100

            # Draw the game world on the window.
            windowSurface.fill(WHITE)

            # Draw each scenery image
            for s in sceneries:
                windowSurface.blit(s["surface"], s["rect"])

            # Draw each broken scenery image
            for b in bsceneries:
                windowSurface.blit(b["surface"], b["rect"])

            # Draw each ring
            for r in rings:
                windowSurface.blit(r["surface"], r["rect"])

            # Draw the player
            windowSurface.blit(skiImages[ANG], skiRect)

            drawText(
                "Top Score: %s" % (highscore), fonte2, windowSurface, 15, 10
            )
            drawText("Score: %s" % (score), fonte2, windowSurface, 15, 34)

            if tempo >= 0:
                drawText(
                    "Tempo: %s seg" % (tempo),
                    fonte2,
                    windowSurface,
                    WINDOWWIDTH - 210,
                    8,
                )

            pygame.display.update()

        else:
            if score - 1 > highscore:
                doc = open("topscore.txt", "w")  # escreve no arquivo
                doc.write(str(score))
                telahighscore(score)
            else:
                telascore(score)
            windowSurface.fill(WHITE)
            pygame.display.update()
            return
        mainClock.tick(FPS)


# set up pygame, the window
pygame.init()
mainClock = pygame.time.Clock()
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
pygame.display.set_caption("SkiFree..o")
# setting up the mouse cursor
pygame.mouse.set_visible(True)

# fonte de neve
fonte1 = pygame.font.Font("fonts/almosnow.ttf", 32)
fonte2 = pygame.font.Font("fonts/Press Start K.ttf", 16)
fonte3 = pygame.font.Font("fonts/Press Start K.ttf", 32)
# the menu images
telainicialImage = pygame.image.load("images/tela inicial.png")
telainicialRect = telainicialImage.get_rect()
telainicialRect.topleft = (0, 0)
telainstrucaoImage = pygame.image.load("images/instrucoes.png")
telainstrucaoRect = telainstrucaoImage.get_rect()
telainstrucaoRect.topleft = (0, 0)
telascoreImage = pygame.image.load("images/score.png")
telascoreRect = telascoreImage.get_rect()
telahighscoreImage = pygame.image.load("images/highscore.png")
telahighscoreRect = telahighscoreImage.get_rect()


# the button image
botao1Image = pygame.image.load("images/botao1.png")

botao1Rect = botao1Image.get_rect()
botao1Rect.topleft = (345, 257)
botao2Image = pygame.image.load("images/botao3.png")
botao2Rect = botao2Image.get_rect()
botao2Rect.topleft = (345, 307)
botao3Image = pygame.image.load("images/botao2.png")
botao3Rect = botao3Image.get_rect()
botao3Rect.topleft = (345, 357)
botaovoltarImage = pygame.image.load("images/botaovoltar.png")
botaovoltarRect = botaovoltarImage.get_rect()
botaovoltarRect.bottomleft = (90, WINDOWHEIGHT - 60)


# setting up the scenery images
arvoreImage = pygame.image.load("images/arvore.png")
arvorealtaImage = pygame.image.load("images/arvorealta.png")
arvoresecaImage = pygame.image.load("images/arvoreseca.png")
pedraImage = pygame.image.load("images/pedra.png")
torreImage = pygame.image.load("images/torre.png")

# the broken scenery images
barvoreImage = pygame.image.load("images/barvore.png")
barvorealtaImage = pygame.image.load("images/barvorealta.png")
barvoresecaImage = pygame.image.load("images/barvoreseca.png")
bpedraImage = pygame.image.load("images/bpedra.png")
btorreImage = pygame.image.load("images/btorre.png")

scenery = [
    arvoreImage,
    arvorealtaImage,
    arvoresecaImage,
    arvoreImage,
    pedraImage,
    pedraImage,
    torreImage,
    barvoreImage,
    barvorealtaImage,
    barvoresecaImage,
    barvoreImage,
    bpedraImage,
    bpedraImage,
    btorreImage,
]

# ring image
ringImage = pygame.image.load("images/ring.png")

# setting up the player images
ski0Image = pygame.image.load("images/ski0.png")
skiRect = ski0Image.get_rect()
ski1Image = pygame.image.load("images/ski1.png")
ski2Image = pygame.image.load("images/ski2.png")
ski3Image = pygame.image.load("images/ski3.png")
ski4Image = pygame.image.load("images/ski4.png")
skiImages = [ski0Image, ski1Image, ski2Image, ski3Image, ski4Image]

sceneries = []
skis = []
bsceneries = []


# setting up the inicial position of the player
skiRect.topleft = (WINDOWWIDTH / 2 - 12, 50)
tempo = 60


while True:
    menuprincipal()
    mainClock.tick(FPS)
