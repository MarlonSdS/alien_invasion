class Settings():
    """Armazena todas as configurações do Alien Invasion"""
    def __init__(self):
        #configurações da tela
        self.screen_width = 1280
        self.screen_height = 720
        self.bg_color = (30, 37, 41)
        #configurações da nave do jogador
        self.ship_speed_factor = 1.5
        self.ship_limit = 3
        #configurações dos projéteis
        self.bullet_speed_factor = 3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (20, 120, 60)
        self.bullets_allowed = 3
        #configurações dos alienigenas 
        self.alien_speed_factor = 1
        self.fleet_speed_drop = 50
        #1 representa direita; -1 representa esquerda
        self.fleet_direction = 1