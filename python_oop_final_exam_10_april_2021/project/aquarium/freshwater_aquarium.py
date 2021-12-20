from project.aquarium.base_aquarium import BaseAquarium
from project.fish.freshwater_fish import FreshwaterFish


class FreshwaterAquarium(BaseAquarium):
    init_capacity = 50

    def __init__(self, name):
        super().__init__(name, self.init_capacity)


f = FreshwaterAquarium("Pesho's")

print(f.name)
print(f.__class__.__name__)
fish = FreshwaterFish("Pesho", "Freshwater", 10)
print(fish)
print(f.add_fish(fish))

print(f.__class__.__name__)
print(fish.__class__.__name__)
