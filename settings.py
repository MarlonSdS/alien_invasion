class Settings():
    """Armazena todas as configurações do Alien Invasion"""
    def __init__(self):
        #configurações da tela
        self.screen_width = 1280
        self.screen_height = 720
        self.bg_color = (30, 37, 41)
        #configurações da nave do jogador
        self.ship_limit = 3
        #configurações dos projéteis
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (20, 120, 60)
        self.bullets_allowed = 3
        #1 representa direita; -1 representa esquerda
        self.fleet_direction = 1
        #a taxa com que a velocidade da frota aumenta a cada nível
        self.speedup_scale = 1.2
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Inicializa as configurações que mudam ao longo do jogo"""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        #configurações dos alienigenas 
        self.alien_speed_factor = 1
        self.fleet_speed_drop = 10
        #pontuação
        self.alien_points = 10

    def increase_speed(self):
        """Aumenta a volicidade do jogo quando o jogador sobe de nível"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points *= self.speedup_scale
        #self.fleet_speed_drop *= self.speedup_scale