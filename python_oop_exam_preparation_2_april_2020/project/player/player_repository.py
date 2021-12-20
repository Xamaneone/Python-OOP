from abc import ABC

from project.player.player import Player


class PlayerRepository(ABC):
    def __init__(self):
        self.count = 0
        self.players = []

    def add(self, player: Player):
        self.check_if_player_already_exist(player)
        self.players.append(player)
        self.count += 1

    def remove(self, player: str):
        if player == "":
            raise ValueError("Player cannot be an empty string!")
        for p in self.players:
            if p == player:
                self.players.remove(p)
                self.count -= 1
                return

    def find(self, username: str):
        for p in self.players:
            if p.username == username:
                return p

    def check_if_player_already_exist(self, player: Player):
        for p in self.players:
            if p.username == player.username:
                raise ValueError(f"Player {player.username} already exists!")






