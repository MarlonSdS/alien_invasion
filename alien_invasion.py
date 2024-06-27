import pygame
from pygame.sprite import Group

import game_functions as gf
from settings import Settings
from ship import Ship
from game_stats import GameStats
from button import Button

def run_game():
    #Inicializa o jogo, as configurações e cria um objeto para a tela
    pygame.init()
    conf = Settings()
    screen = pygame.display.set_mode((conf.screen_width, conf.screen_height))
    pygame.display.set_caption("Alien Invasion")
    #Cria o botão play
    play_button = Button(conf, screen, "Play")
    #Cria uma nave
    ship = Ship(conf, screen)
    #Cria um grupo de projéteis e um de aliens
    bullets = Group()
    aliens = Group()
    #cria uma frota de alienigenas
    gf.create_fleet(conf, screen, aliens)
    #statisticas do jogo
    stats = GameStats(conf)

    #laço principal do game
    while True:
        #Observa o teclado e o mouse
        gf.check_events(conf, screen, ship, aliens, bullets, play_button, stats)
        #executa essas ações apenas se o jogador ainda tiver vidas
        if stats.game_active:
            #atualiza a posição da nave e os projéteis
            ship.update()
            gf.update_bullets(conf, screen, aliens, bullets)
            gf.update_aliens(conf, stats, screen,  ship, aliens, bullets)

        gf.update_screen(conf, screen, ship, bullets, aliens, play_button, stats)
        


run_game()