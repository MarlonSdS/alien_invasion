import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """Representa um alinígena da frota"""
    def __init__(self, conf, screen):
        """Inicializa o alien e define sua posição inicial"""
        super().__init__()
        self.screen = screen
        self.conf = conf
        #carrega o sprite do alien e seu rect
        self.image = pygame.image.load('images/enemyRed1.bmp')
        self.rect = self.image.get_rect()
        #inicia cada novo alien próximo ao canto superior esquerdo
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        #armazena a posição exata do alien
        self.x = float(self.rect.x)

    def check_edge(self):
        """Checa se o alien está na borda da tela e devolve true caso sim"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def update(self):
        """Move o alien para a direita e para a esquerda"""
        self.x += self.conf.alien_speed_factor * self.conf.fleet_direction
        self.rect.x = self.x 

    def blitme(self):
        """Desenha o alien na posição atual"""
        self.screen.blit(self.image, self.rect)
