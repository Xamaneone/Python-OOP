from project.card.card import Card


class MagicCard(Card):
    init_dmg = 5
    init_health = 80

    def __init__(self, name):
        super().__init__(name, self.init_dmg, self.init_health)
