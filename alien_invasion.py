import pygame
from pygame.sprite import Group

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
    ship = Ship(conf, screen)
    #Cria um grupo de projéteis e um de aliens
    bullets = Group()
    aliens = Group()
    #cria uma frota de alienigenas
    gf.create_fleet(conf, screen, aliens)

    #laço principal do game
    while True:
        #Observa o teclado e o mouse
        gf.check_events(conf, screen, ship, bullets)
        #atualiza a posição da nave e os projéteis
        ship.update()
        gf.update_bullets(bullets)
        gf.update_aliens(conf, aliens)

        gf.update_screen(conf, screen, ship, bullets, aliens)
        


run_game()