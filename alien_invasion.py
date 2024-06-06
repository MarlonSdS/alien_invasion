import sys
import pygame

from settings import Settings
from ship import Ship

def run_game():
    #Inicializa o jogo, as configurações e cria um objeto para a tela
    pygame.init()
    conf = Settings()
    screen = pygame.display.set_mode((conf.screen_width, conf.screen_height))
    pygame.display.set_caption("Alien Invasion")
    #Cria uma nave
    ship = Ship(screen)

    while True:
        #Observa o teclado e o mouse
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        #Cor de fundo
        screen.fill(conf.bg_color)
        #Desenha a nave na tela
        ship.blitme()
        #Deixa a tela mais recente visível
        pygame.display.flip()


run_game()