import pygame
import os
import time
import random


WIDTH, HEIGHT = 1280, 920
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Freeway 2600 - Resmastered")
GREY = (105, 105, 105)
GALINHA_WIDTH, GALINHA_HEIGHT = 55, 55
GALINHA1_START_X, GALINHA1_START_Y = 320,740
GALINHA2_START_X, GALINHA2_START_Y = 890,740

BG = pygame.image.load(os.path.join("assets", "fundoFreeway1280x920.png"))
CARRO_VERMELHO = pygame.image.load(os.path.join("assets", "carro.png"))
IMAGEM_GALINHA = pygame.image.load(os.path.join("assets", "galinha.png"))
GALINHA = pygame.transform.scale(IMAGEM_GALINHA, (GALINHA_WIDTH, GALINHA_HEIGHT))
FPS = 60

def draw_window():
    WINDOW.fill(GREY)
    WINDOW.blit(BG, (0,0))
    pygame.display.update()

def draw_galinhas():
    WINDOW.blit(GALINHA, (GALINHA1_START_X, GALINHA1_START_Y))
    WINDOW.blit(GALINHA, (GALINHA2_START_X, GALINHA2_START_Y))
    pygame.display.update()




def main():
    run = True

    clock = pygame.time.Clock()

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        draw_window()
        draw_galinhas()
        
    pygame.quit()
if __name__ == "__main__":
    main()
