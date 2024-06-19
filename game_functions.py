import sys
import pygame

from bullet import Bullet
from alien import Alien
from ship import Ship

def check_keydown(event, conf, screen, ship, bullets):
    """Responde a pressionamentos de tecla"""
    #move a nave para a direita ou para esquerda
    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullets(conf, screen, ship, bullets)
    elif event.key == pygame.K_ESCAPE:
        sys.exit()
       
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
            

def update_screen(conf, screen, ship, bullets, aliens):
    """Redesenha a tela a cada atualização e exibe a nova tela"""
    #redesenha a cada passagem do laço
    screen.fill(conf.bg_color)
    #redesenha a nave, os aliens e todos os projéteis
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)
    #deixa a tela mais recente visível
    pygame.display.flip()

def update_bullets(bullets):
    """Atualiza os projéteis na tela e apaga os que saíram dela"""
    #atualiza o grupo de projéteis
    bullets.update()
    #apaga os projéteis que saíram da tela
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
def update_aliens(conf, aliens):
    """Atualiza a posição dos alienígenas"""
    #checa se alguém bateu na borda
    check_fleet_edges(conf, aliens)
    aliens.update()

def fire_bullets(conf, screen, ship, bullets):
    """Dispara um projétil se o limite ainda não foi alcançado"""
    #Cria um novo projétil e o adiciona ao grupo de projéteis
    new_bullet = Bullet(conf, screen, ship)
    if len(bullets) < conf.bullets_allowed:
        bullets.add(new_bullet)

def get_number_aliens_x(conf, alien_width):
    """Determina o número de aliens que cabem numa linha"""
    available_space_x = conf.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2* alien_width))
    return number_aliens_x

def get_number_aliens_y(conf,ship_height,alien_height):
    """Determina quantas linhas de aliens cabem na tela"""
    available_space_y = conf.screen_height - alien_height - ship_height
    number_aliens_y = int(available_space_y / (2 * alien_height))
    return number_aliens_y

def create_alien(conf, screen, alien_number, row, aliens):
    """Cria um alienígena e o posiciona na linha"""
    alien = Alien(conf, screen)
    alien_width = alien.rect.width
    alien_height = alien.rect.height
    alien.x = alien_width + 2 * alien_number * alien_width
    alien.y = 2 * row * alien_height
    alien.rect.x = alien.x 
    alien.rect.y = alien.y
    aliens.add(alien)

def create_fleet(conf, screen, aliens):
    """Cria uma frota de alienígenas"""
    #regras sobre a disposição de aliens na tela
    alien = Alien(conf, screen)
    ship = Ship(conf, screen)
    alien_width = alien.rect.width
    alien_height = alien.rect.height
    ship_height = ship.rect.height
    number_aliens_x = get_number_aliens_x(conf, alien_width)
    number_aliens_y = get_number_aliens_y(conf, ship_height, alien_height)
    #laço para criação de linhas uma embaixo da outra
    for row in range(number_aliens_y):
        #cria uma linha de aliens
        for alien_number in range(number_aliens_x):
            create_alien(conf, screen, alien_number, row, aliens)

def check_fleet_edges(conf, aliens):
    """Checa se algum alien da frota alcançou a borda da tela"""
    for alien in aliens.sprites():
        if alien.check_edge():
            change_fleet_direction(conf, aliens)
            break

def change_fleet_direction(conf, aliens):
    """Faz toda a frota descer e muda a sua direção"""
    for alien in aliens.sprites():
        alien.rect.y += conf.fleet_speed_drop * conf.alien_speed_factor
        conf.fleet_direction *= -1

