import sys
import pygame
from time import sleep

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

def check_play_button(mouse_x, mouse_y, screen, aliens, bullets, ship, conf, play_button, stats):
    """Responde ao clique no botão play"""
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        #ocultar o cursor do mouse
        pygame.mouse.set_visible(False)
        #reinicia as estaísticas
        stats.reset_stats()
        stats.game_active = True
        #esvazia a lista de alienígenas e projéteis
        aliens.empty()
        bullets.empty()
        #cria uma nova frota e centraliza a nave do jogador
        create_fleet(conf, screen, aliens)
        ship.center_ship()

def check_events(conf, screen, ship, aliens, bullets, play_button, stats):
    """Responde a eventos de mouse e teclado"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown(event, conf, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup(event, ship) 
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(mouse_x, mouse_y, screen, aliens, bullets, ship, conf, play_button, stats)
            

def update_screen(conf, screen, ship, bullets, aliens, play_button, stats):
    """Redesenha a tela a cada atualização e exibe a nova tela"""
    #redesenha a cada passagem do laço
    screen.fill(conf.bg_color)
    #redesenha a nave, os aliens e todos os projéteis
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)
    #desenha o botão play na tela se o jogo estiver inativo
    if stats.game_active == False:
        play_button.draw_button()
    #deixa a tela mais recente visível
    pygame.display.flip()

def update_bullets(conf, screen, aliens, bullets):
    """Atualiza os projéteis na tela e apaga os que saíram dela"""
    #atualiza o grupo de projéteis
    bullets.update()
    #verifica se houve colisão com aliens e os remove da tela caso sim
    pygame.sprite.groupcollide(bullets, aliens, True, True)
    #verifica se todos os aliens foram mortos e recria a frota caso sim
    if len(aliens) == 0:
        create_fleet(conf, screen, aliens)
    #apaga os projéteis que saíram da tela
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
def update_aliens(conf, stats, screen, ship, aliens, bullets):
    """Atualiza a posição dos alienígenas"""
    #checa se alguém bateu na borda
    check_fleet_edges(conf, aliens)
    aliens.update()
    #checa se algum alienígena bateu na espaçonava
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(conf, stats, screen, ship, aliens, bullets)
    #checa se algum alien bateu na borda inferior
    check_aliens_bottom(conf, stats, screen, ship, aliens, bullets)

def fire_bullets(conf, screen, ship, bullets):
    """Dispara um projétil se o limite ainda não foi alcançado"""
    #Cria um novo projétil e o adiciona ao grupo de projéteis
    new_bullet = Bullet(conf, screen, ship)
    if len(bullets) < conf.bullets_allowed:
        bullets.add(new_bullet)

def ship_hit(conf, stats, screen, ship, aliens, bullets):
    """Responde a uma colisão da nave com algum alien"""
    #decrementa as naves restantes
    stats.ship_left -= 1
    #esvazia a lista de aliens e projéteis
    aliens.empty()
    bullets.empty()
    #cria uma nova frota e centraliza a espaçonave
    create_fleet(conf, screen, aliens)
    ship.center_ship()
    #faz uma pausa
    sleep(0.5)
    #Define o jogo como inativo caso o jogador fique sem vidas
    if stats.ship_left == 0:
        stats.game_active = False
        #reexibe o cursor do mouse
        pygame.mouse.set_visible(True)

def check_aliens_bottom(conf,  stats,  screen,  ship,  aliens,  bullets):
    """Verifica se algum alien atingiu a borda inferior da tela"""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            #trata esse caso do mesmo modo de quando a nave é atingida
            ship_hit(conf, stats, screen, ship, aliens, bullets)
            break

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
    conf.fleet_direction *= -1
    for alien in aliens.sprites():
        alien.rect.y += conf.fleet_speed_drop
        
    

