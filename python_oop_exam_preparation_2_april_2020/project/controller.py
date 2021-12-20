from project.battle_field import BattleField
from project.card.card_repository import CardRepository
from project.card.magic_card import MagicCard
from project.card.trap_card import TrapCard
from project.player.advanced import Advanced
from project.player.beginner import Beginner
from project.player.player_repository import PlayerRepository


class Controller:
    def __init__(self):
        self.player_repository = PlayerRepository()
        self.deck_repository = CardRepository()

    def add_player(self, Type, username):
        if Type == "Beginner":
            self.player_repository.add(Beginner(username))
            return self.__succ_player_creation(Type, username)
        elif Type == "Advanced":
            self.player_repository.add(Advanced(username))
            return self.__succ_player_creation(Type, username)

    def add_card(self, Type: str, name: str):
        if Type == "Magic":
            self.deck_repository.add(MagicCard(name))
            return self.__succ_card_creation(Type, name)
        elif Type == "Trap":
            self.deck_repository.add(TrapCard(name))
            return self.__succ_card_creation(Type, name)

    def add_player_card(self, username: str, card_name: str):
        player = self.get_player_by_username(username)
        card = self.get_card_by_name(card_name)
        if player == None or card == None:
            return
        player.card_repository.cards.append(card)
        return f"Successfully added card: {card_name} to user: {username}"

    def fight(self, attack_name: str, enemy_name: str):
        attacker = self.get_player_by_username(attack_name)
        enemy = self.get_player_by_username(enemy_name)
        BattleField().battle(attacker, enemy)
        return f"Attack user health {attacker.health} - Enemy user health {enemy.health}"

    def report(self):
        str_to_return = ""
        for player in self.player_repository.players:
            str_to_return += f"Username: {player.username} - Health: {player.health} - Cards {player.card_repository.count}\n"
            for card in player.card_repository.cards:
                str_to_return += f"### Card: {card.name} - Damage: {card.damage_points}\n"

    def get_player_by_username(self, username):
        player = None
        for p in self.player_repository.players:
            if p.username == username:
                player = p
        return player

    def get_card_by_name(self, card_name):
        card = None
        for c in self.deck_repository.cards:
            if c.name == card_name:
                card = c
        return card

    @staticmethod
    def __succ_player_creation(Type, username):
        return f"Successfully added player of type {Type} with username: {username}"

    @staticmethod
    def __succ_card_creation(Type, name):
        return f"Successfully added card of type {Type}Card with name: {name}"
