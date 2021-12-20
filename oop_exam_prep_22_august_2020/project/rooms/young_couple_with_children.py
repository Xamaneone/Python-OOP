from project.appliances.fridge import Fridge
from project.appliances.laptop import Laptop
from project.appliances.tv import TV
from project.rooms.room import Room


class YoungCoupleWithChildren(Room):


    def __init__(self, name: str, salary_one: float, salary_two: float, *children):
        self.members_count = 2 + len(children)
        super().__init__(name, salary_one + salary_two, self.members_count)
        self.children = list(children)
        self.room_cost = 30
        self.appliances = self.__generate_appliances()
        self.calculate_expenses(self.appliances)

    def __generate_appliances(self):
        appliances = []
        for x in range(self.members_count):
            appliances.append(TV())
            appliances.append(Fridge())
            appliances.append(Laptop())
        return appliances

