import pygame
import os
import time
import random

#window settings
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 920
WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Freeway 2600 - Resmastered")
GREY = (105, 105, 105)
FPS = 60
#galinhas settings
GALINHA_WIDTH, GALINHA_HEIGHT = 48, 48
GALINHA1_START_X, GALINHA1_START_Y = 320,840
GALINHA2_START_X, GALINHA2_START_Y = 890,840
#carro settings
CARRO_WIDTH, CARRO_HEIGHT = 40, 60
CARRO1_XSTART, CARRO1_YSTART = 1218, 128
CARRO2_XSTART, CARRO2_YSTART = 1218, 196
CARRO3_XSTART, CARRO3_YSTART = 1218, 262
CARRO4_XSTART, CARRO4_YSTART = 1218, 330
CARRO5_XSTART, CARRO5_YSTART = 1218, 400
CARRO6_XSTART, CARRO6_YSTART = 1218, 488
CARRO7_XSTART, CARRO7_YSTART = 1218, 555
CARRO8_XSTART, CARRO8_YSTART = 1218, 618
CARRO9_XSTART, CARRO9_YSTART = 1218, 680
CARRO10_XSTART, CARRO10_YSTART = 1218, 744

#load images
BG = pygame.image.load(os.path.join("assets", "fundoFreeway1280x920.png"))
IMAGEM_CARRO_VERMELHO = pygame.image.load(os.path.join("assets", "carro.png"))
IMAGEM_GALINHA = pygame.image.load(os.path.join("assets", "galinha.png"))
GALINHA = pygame.transform.scale(IMAGEM_GALINHA, (GALINHA_WIDTH, GALINHA_HEIGHT))
CARRO_VERMELHO = pygame.transform.rotate(pygame.transform.scale(IMAGEM_CARRO_VERMELHO,(CARRO_WIDTH, CARRO_HEIGHT)), 270)

#função que desenha a janela do jogo
def draw_window():
    WINDOW.fill(GREY)
    WINDOW.blit(BG, (0,0))
    pygame.display.update()

#função que desenha as galinhas
def draw_galinhas(userGalinha1, userGalinha2):
    WINDOW.blit(GALINHA, (userGalinha1.x, userGalinha1.y))
    WINDOW.blit(GALINHA, (userGalinha2.x, userGalinha2.y))
    pygame.display.update()

#função que desenha os carros 
def draw_carros():
    WINDOW.blit(CARRO_VERMELHO,(CARRO1_XSTART, CARRO1_YSTART))
    WINDOW.blit(CARRO_VERMELHO,(CARRO2_XSTART, CARRO2_YSTART))
    WINDOW.blit(CARRO_VERMELHO,(CARRO3_XSTART, CARRO3_YSTART))
    WINDOW.blit(CARRO_VERMELHO,(CARRO4_XSTART, CARRO4_YSTART))
    WINDOW.blit(CARRO_VERMELHO,(CARRO5_XSTART, CARRO5_YSTART))
    WINDOW.blit(CARRO_VERMELHO,(CARRO6_XSTART, CARRO6_YSTART))
    WINDOW.blit(CARRO_VERMELHO,(CARRO7_XSTART, CARRO7_YSTART))
    WINDOW.blit(CARRO_VERMELHO,(CARRO8_XSTART, CARRO8_YSTART))
    WINDOW.blit(CARRO_VERMELHO,(CARRO9_XSTART, CARRO9_YSTART))
    WINDOW.blit(CARRO_VERMELHO,(CARRO10_XSTART, CARRO10_YSTART))
    pygame.display.update()

#função que inicia o loop de execução do jogo, limita a quantidade de quadros exibidos na 
# tela a cada segundo e cria o evento de encerramento  voluntáio da execução:
def main():

    userGalinha1 = pygame.Rect(GALINHA1_START_X, GALINHA1_START_Y,GALINHA_WIDTH, GALINHA_HEIGHT)
    userGalinha2 = pygame.Rect(GALINHA2_START_X, GALINHA2_START_Y,GALINHA_WIDTH, GALINHA_HEIGHT)


    run = True

    clock = pygame.time.Clock()

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        draw_window()
        draw_galinhas(userGalinha1,userGalinha2)
        draw_carros()
        
    pygame.quit()
if __name__ == "__main__":
    main()
