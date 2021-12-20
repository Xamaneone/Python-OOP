from project.card.card import Card


class CardRepository:
    def __init__(self):
        self.count = 0
        self.cards = []

    def add(self, card: Card):
        self.check_if_card_already_exist(card)
        self.cards.append(card)
        self.count += 1

    def remove(self, card: str):
        if card == "":
            raise ValueError("Card cannot be an empty string!")
        for c in self.cards:
            if c == card:
                self.cards.remove(c)
                self.count -= 1
                return

    def find(self, name: str):
        for c in self.cards:
            if c.name == name:
                return c


    def check_if_card_already_exist(self, card: Card):
        for p in self.cards:
            if p.name == card.name:
                raise ValueError(f"Card {card.name} already exists!")
