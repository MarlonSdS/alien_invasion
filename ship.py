import pygame

class Ship():
    def __init__(self, conf, screen):
        """Inicializa a nave e define sua posição atual"""
        self.screen = screen
        self.conf = conf
        #Carrega a imagem da nave e obtém seu rect
        self.image = pygame.image.load("images/playerShip1_blue.bmp")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        #Inicia cada nova nave na parte inferior central da tela
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        #Flags de movimento
        self.moving_right = False
        self.moving_left = False
        #Valor decimal para o centro da nave
        self.center = float(self.rect.centerx)

    def update(self):
        """Atualiza a posição da nave de acordo com a flag de movimento"""
        #Atualiza o centro da nave e não o rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.conf.ship_speed_factor
        elif self.moving_left and self.rect.left > 0:
            self.center -= self.conf.ship_speed_factor
        self.rect.centerx = self.center

    def blitme(self):
        """Desenha a nave na sua posição atual"""
        self.screen.blit(self.image, self.rect)