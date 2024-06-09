class Settings():
    """Armazena todas as configurações do Alien Invasion"""
    def __init__(self):
        #configurações da tela
        self.screen_width = 1100
        self.screen_height = 720
        self.bg_color = (30, 32, 48)
        #velocidade da nave
        self.ship_speed_factor = 1.5
        #configurações dos projéteis
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (20, 120, 60)
        self.bullets_allowed = 3