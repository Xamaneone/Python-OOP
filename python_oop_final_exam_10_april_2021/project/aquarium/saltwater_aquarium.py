from project.aquarium.base_aquarium import BaseAquarium


class SaltwaterAquarium(BaseAquarium):
    init_capacity = 25

    def __init__(self, name):
        super().__init__(name, self.init_capacity)