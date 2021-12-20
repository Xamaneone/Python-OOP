from project.appliances.fridge import Fridge
from project.appliances.stove import Stove
from project.appliances.tv import TV
from project.rooms.room import Room


class OldCouple(Room):
    appliances = [TV(), TV(), Fridge(), Fridge(), Stove(), Stove()]

    def __init__(self, name: str, pension_one: float, pension_two: float):
        super().__init__(name, pension_one + pension_two, 2)
        self.room_cost = 10
        self.calculate_expenses(self.appliances)

