class GameStats():
    """Guarda dados estatísticos do jogo"""
    def __init__(self, conf):
        """Inicializa os dados estatísticos"""
        self.conf = conf
        self.reset_stats()
        #inicia o jogo com um estado de game ativo
        self.game_active = True

    def reset_stats(self):
        """Inicializa os dados estatísticos que podem mudar durante o jogo"""
        self.ship_left = self.conf.ship_limit