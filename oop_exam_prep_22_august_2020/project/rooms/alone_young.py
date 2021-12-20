from project.appliances.tv import TV
from project.rooms.room import Room


class AloneYoung(Room):
    appliances = [TV()]

    def __init__(self, name: str, salary: float):
        super().__init__(name, salary, 1)
        self.room_cost = 10
        self.calculate_expenses(self.appliances)
