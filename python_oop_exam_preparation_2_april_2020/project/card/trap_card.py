from project.card.card import Card


class TrapCard(Card):
    init_dmg = 120
    init_health = 5

    def __init__(self, name):
        super().__init__(name, self.init_dmg, self.init_health)