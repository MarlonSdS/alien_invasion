import sys
import pygame

def check_events(ship):
    """Responde a eventos de mouse e teclado"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            sys.exit()
        elif event.type == pygame.KEYDOWN:
                #move a nave para a direita
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                ship.moving_right = True
            elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                ship.moving_left = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                ship.moving_right = False
            elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                ship.moving_left = False

def update_screen(conf, screen, ship):
    """Redesenha a tela a cada atualização e exibe a nova tela"""
    #redesenha a cada passagem do laço
    screen.fill(conf.bg_color)
    ship.blitme()
    #deixa a tela mais recente visível
    pygame.display.flip()