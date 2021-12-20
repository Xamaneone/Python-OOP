from project.fish.base_fish import BaseFish


class FreshwaterFish(BaseFish):
    init_eat_increase_size = 3
    init_size = 3
    init_environment = "FreshwaterAquarium"

    def __init__(self, name, species, price):
        super().__init__(name, species, self.init_size, price, self.init_environment)


