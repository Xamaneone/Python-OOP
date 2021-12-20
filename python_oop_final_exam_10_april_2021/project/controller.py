from project.aquarium.freshwater_aquarium import FreshwaterAquarium
from project.aquarium.saltwater_aquarium import SaltwaterAquarium
from project.decoration.decoration_repository import DecorationRepository
from project.decoration.ornament import Ornament
from project.decoration.plant import Plant
from project.fish.freshwater_fish import FreshwaterFish
from project.fish.saltwater_fish import SaltwaterFish


class Controller:
    def __init__(self):
        self.decorations_repository = DecorationRepository()
        self.aquariums = []

    def add_aquarium(self, aquarium_type: str, aquarium_name: str):
        if aquarium_type == "FreshwaterAquarium":
            self.aquariums.append(FreshwaterAquarium(aquarium_name))
            return f"Successfully added {aquarium_type}."
        elif aquarium_type == "SaltwaterAquarium":
            self.aquariums.append(SaltwaterAquarium(aquarium_name))
            return f"Successfully added {aquarium_type}."
        else:
            return "Invalid aquarium type."

    def add_decoration(self, decoration_type: str):
        if decoration_type == "Ornament":
            self.decorations_repository.decorations.add(Ornament())
            return f"Successfully added {decoration_type}."
        elif decoration_type == "Plant":
            self.decorations_repository.decorations.add(Plant())
            return f"Successfully added {decoration_type}."
        else:
            return "Invalid decoration type."

    def insert_decoration(self, aquarium_name: str, decoration_type: str):
        aquarium = self.get_aquarium_by_name(aquarium_name)
        data = ""
        for decor in self.decorations_repository.decorations:
            if decor.__name__ == decoration_type:
                data = self.decorations_repository.decorations.pop(decor)
                break
        if not data:
            return f"There isn't a decoration of type {decoration_type}."
        aquarium.add_decoration(data)
        return f"Successfully added {decoration_type} to {aquarium_name}."


    def add_fish(self, aquarium_name: str, fish_type: str, fish_name: str, fish_species: str, price: float):
        aquarium = self.get_aquarium_by_name(aquarium_name)
        fish = ""
        if fish_type == "FreshwaterFish":
            fish = FreshwaterFish(fish_name, fish_species, price)
        elif fish_type == "SaltwaterFish":
            fish = SaltwaterFish(fish_name, fish_species, price)
        if not fish:
            return f"There isn't a fish of type {fish_type}."
        return aquarium.add_fish(fish)


    def feed_fish(self, aquarium_name: str):
        aquarium = self.get_aquarium_by_name(aquarium_name)
        return f"Fish fed: {aquarium.feed()}"

    def calculate_value(self, aquarium_name: str):
        aquarium = self.get_aquarium_by_name(aquarium_name)
        value = 0
        for fish in aquarium.fish:
            value += fish.price
        for decor in aquarium.decorations:
            value += decor.price
        return f"The value of Aquarium {aquarium.name} is {value}"

    def report(self):
        result = ""
        for aquarium in self.aquariums:
            result += str(aquarium)
        return result


    def get_aquarium_by_name(self, name: str):
        result = ""
        for aquarium in self.aquariums:
            if aquarium.name == name:
                result = aquarium
                break
        return result

a = Controller()

print(a.add_aquarium("FreshwaterAquarium", "Pesho"))
print(a.report())
print(a.add_fish("Pesho", "FreshwaterFish", "Pesho", "Freshwater", 10))
print(a.report())




