import pygame.font

class Button():
    """Inicia os atributos do botão"""
    def __init__(self, conf, screen, msg):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        #dimensõe e propriedades do botão
        self.width = 200
        self.height = 50
        self.button_color = (0, 0, 255)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)
        #constrói o rect do botão e o centraliza
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center
        #a mensagem do botão deve ser preparada apenas uma vez
        self.prep_msg(msg)

    def prep_msg(self, msg):
        """Transforma msg em uma imagem e a renderiza no centro do botão"""
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        """Desenha um botão na tela e em seguida o preenche com a mensage"""
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)