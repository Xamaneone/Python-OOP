from project.player.player import Player


class Beginner(Player):
    init_health = 50

    def __init__(self, username):
        super().__init__(username, self.init_health)

