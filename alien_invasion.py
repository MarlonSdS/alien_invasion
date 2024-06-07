import pygame

import game_functions as gf
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

    #laço principal do game
    while True:
        #Observa o teclado e o mouse
        gf.check_events(ship)
        #atualiza a posição da nave
        ship.update()
        #Cor de fundo, desenha a nave e atualiza a tela
        gf.update_screen(conf, screen, ship)
        


run_game()