from project.player.player import Player


class BattleField:
    def fight(self, attacker: Player, enemy: Player):
        if self.check_if_players_are_dead(attacker, enemy):
            raise ValueError("Player is dead!")
        self.extra_power_up_players(attacker, enemy)
        self.battle(attacker, enemy)


    def battle(self, p1: Player, p2: Player):
        while True:
            if self.check_if_players_are_dead(p1, p2):
                break
            for card in p1.card_repository.cards:
                # dmg = p2.health - card.damage_points
                # if dmg < 0:
                #     dmg = 0
                # p2.health = dmg
                p2.take_damage(card.damage_points)
            if self.check_if_players_are_dead(p1, p2):
                break
            for card in p2.card_repository.cards:
                # dmg = p1.health - card.damage_points
                # if dmg < 0:
                #     dmg = 0
                # p1.health = dmg
                p1.take_damage(card.damage_points)

    @staticmethod
    def check_if_players_are_dead(attacker, enemy):
        if attacker.is_dead:
            return True
        if enemy.is_dead:
            return True
        return False

    def check_if_players_are_beginners(self, attacker, enemy):
        if attacker.__name__ == "Beginner":
            self.power_up_player(attacker)
        if enemy.__name__ == "Beginner":
            self.power_up_player(enemy)

    @staticmethod
    def power_up_player(player: Player):
        player.health = (player.health + 40)
        for card in player.card_repository.cards:
            card.damage_points = card.damage_points + 30


    @staticmethod
    def extra_power_up_players(p1: Player, p2: Player):
        p1_extra_health = 0
        p2_extra_health = 0

        for card in p1.card_repository.cards:
            p1_extra_health += card.health_points
        for card in p2.card_repository.cards:
            p2_extra_health += card.health_points

        p1.health = (p1.health + p1_extra_health)
        p2.health = (p2.health + p2_extra_health)

