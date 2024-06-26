import pygame.font

class Scoreboard():
    """Uma classe para mostrar a pontuação"""
    def __init__(self, conf, screen, stats):
        """Inicia os atributos da pontuação"""
        self.screen = screen 
        self.screen_rect = screen.get_rect() 
        self.conf = conf 
        self.stats = stats
        # Configurações de fonte para as informações de pontuação 
        self.text_color = (219,222,229)
        self.font = pygame.font.SysFont(None, 48)
        # Prepara a imagem da pontuação inicial
        self.prep_score(stats.score)

    def prep_score(self, score):
        """Transforma a pontuação em uma imagem renderizada.""" 
        score_str = str(int(score))
        self.score_image = self.font.render(score_str, True, self.text_color)
        # Exibe a pontuação na parte superior direita da tela
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20 

    def show_score(self):
        """Desenha a pontuação na tela.""" 
        self.screen.blit(self.score_image, self.score_rect)