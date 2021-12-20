from project.appliances.fridge import Fridge
from project.appliances.laptop import Laptop
from project.appliances.tv import TV
from project.rooms.room import Room


class YoungCouple(Room):
    appliances = [TV(), TV(), Fridge(), Fridge(), Laptop(), Laptop()]

    def __init__(self, name: str, salary_one: float, salary_two: float):
        super().__init__(name, salary_one + salary_two, 2)
        self.room_cost = 20
        self.calculate_expenses(self.appliances)

