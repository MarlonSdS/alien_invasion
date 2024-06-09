import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """Administra os objetos projéteis disparados pelo jogador"""
    def __init__(self, conf, screen, ship):
        """Cria um objeto para o projétil na posição atual da nave"""
        super().__init__()
        self.screen = screen
        #Cria um retângulo para o projétil em 0,0 e em seguida o põe na posição da nave
        self.rect = pygame.Rect(0, 0, conf.bullet_width, conf.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        #Armazena a posição do projétil em valor decimal
        self.y = float(self.rect.y)
        self.color = conf.bullet_color
        self.speed_factor = conf.bullet_speed_factor

    def update(self):
        """Move o projétil para cima da tela"""
        #atualiza a poisção decimal do projétil
        self.y -= self.speed_factor
        #atualiza a posição do rect
        self.rect.y = self.y 

    def draw_bullet(self):
        """Desenha o projétil na tela"""
        pygame.draw.rect(self.screen, self.color, self.rect)