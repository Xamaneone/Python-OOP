from abc import ABC, abstractmethod

from project.decoration.base_decoration import BaseDecoration
from project.fish.base_fish import BaseFish


class BaseAquarium(ABC):
    @abstractmethod
    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.decorations = []
        self.fish = []

    def calculate_comfort(self):
        result = 0
        for decor in self.decorations:
            result += decor.comfort
        return result

    def add_fish(self, fish: BaseFish):
        if len(self.fish) >= self.capacity:
            return "Not enough capacity."
        if fish.environment != self.__class__.__name__:
            return "Water not suitable."
        self.capacity += fish.size
        self.fish.append(fish)
        return f"Successfully added {fish.__class__.__name__} to {self.name}."

    def remove_fish(self, fish):
        if fish in self.fish:
            self.fish.remove(fish)
            self.capacity -= fish.size

    def add_decoration(self, decoration: BaseDecoration):
        self.decorations.append(decoration)

    def feed(self):
        counter = 0
        for fish in self.fish:
            fish.eat()
            counter += 1
        return counter

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value == "":
            raise ValueError("Aquarium name cannot be an empty string.")
        self.__name = value

    def __str__(self):
        result = f"{self.name}\n"
        result += "Fish: "
        if self.fish:
            result += f"{' '.join([fish.name for fish in self.fish])}\n"
        else:
            result += "none\n"
        result += f"Decorations: {len(self.decorations)}\n"
        if self.decorations:
            result += f"Comfort: {self.calculate_comfort()}\n"
        else:
            result += "Comfort: 0\n"
        return result

