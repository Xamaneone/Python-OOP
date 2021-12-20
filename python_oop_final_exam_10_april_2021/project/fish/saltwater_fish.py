from project.fish.base_fish import BaseFish


class SaltwaterFish(BaseFish):
    init_eat_increase_size = 2
    init_size = 5
    init_environment = "SaltwaterAquarium"

    def __init__(self, name, species, price):
        super().__init__(name, species, self.init_size, price, self.init_environment)



