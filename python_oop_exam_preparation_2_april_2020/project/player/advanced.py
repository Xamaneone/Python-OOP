from project.player.player import Player


class Advanced(Player):
    init_health = 250

    def __init__(self, username):
        super().__init__(username, self.init_health)