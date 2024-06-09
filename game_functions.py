import sys
import pygame

from bullet import Bullet

def check_keydown(event, conf, screen, ship, bullets):
    """Responde a pressionamentos de tecla"""
    #move a nave para a direita ou para esquerda
    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        #Cria um novo projétil e o adiciona ao grupo de projéteis
        new_bullet = Bullet(conf, screen, ship)
        if len(bullets) < conf.bullets_allowed:
            bullets.add(new_bullet)
       
def check_keyup(event, ship):
    """Responde quando a tecla é solta"""
    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
        ship.moving_left = False

def check_events(conf, screen, ship, bullets):
    """Responde a eventos de mouse e teclado"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown(event, conf, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup(event, ship) 
            

def update_screen(conf, screen, ship, bullets):
    """Redesenha a tela a cada atualização e exibe a nova tela"""
    #redesenha a cada passagem do laço
    screen.fill(conf.bg_color)
    #redesenha a nave e todos os projéteis
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    #deixa a tela mais recente visível
    pygame.display.flip()