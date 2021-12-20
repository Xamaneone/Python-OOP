from project.medicine.medicine import Medicine
from project.supply.supply import Supply
from project.survivor import Survivor


class Bunker:
    def __init__(self):
        self.survivors = []
        self.supplies = []
        self.medicine = []

    @property
    def food(self):
        food = []
        for supply in self.supplies:
            if supply.__name__ == 'FoodSupply':
                food.append(supply)
        if not food:
            raise IndexError("There are not food supplies left!")
        return food

    @property
    def water(self):
        water = []
        for supply in self.supplies:
            if supply.__name__ == 'WaterSupply':
                water.append(supply)
        if not water:
            raise IndexError("There are not water supplies left!")
        return water

    @property
    def painkillers(self):
        painkillers = []
        for medicine in self.medicine:
            if medicine.__name__ == "Painkiller":
                painkillers.append(medicine)
        if not painkillers:
            raise IndexError("There are not painkillers left!")
        return painkillers

    @property
    def salves(self):
        salves = []
        for salve in self.medicine:
            if salve.__name__ == 'Salve':
                salves.append(salve)
        if not salves:
            raise IndexError("There are no salves left!")
        return salves

    def add_survivor(self, survivor: Survivor):
        for s in self.survivors:
            if s.name == survivor.name:
                raise ValueError(f'Survivor with name {survivor.name} already exists.')
        self.survivors.append(survivor)

    def add_supply(self, supply: Supply):
        self.supplies.append(supply)

    def add_medicine(self, medicine: Medicine):
        self.medicine.append(medicine)

    def heal(self, survivor: Survivor, medicine_type: str):
        if survivor.needs_healing:
            for index in range(-1, -len(self.medicine) - 1, -1):
                if self.medicine[index].__name__ == medicine_type:
                    medicine = self.medicine.pop(index)
                    medicine.apply(survivor)
                    return f"{survivor.name} healed successfully with {medicine_type}"
        return

    def sustain(self, survivor: Survivor, sustenance_type: str):
        if survivor.needs_sustenance:
            for index in range(-1, -len(self.supplies) - 1, -1):
                if self.supplies[index].__name__ == sustenance_type:
                    needs = self.supplies.pop(index)
                    needs.apply(survivor)
                    return f"{survivor.name} sustained successfully with {sustenance_type}"
        return

    def next_day(self):
        for s in self.survivors:
            s.needs(-(s.age * 2))
        for s in self.survivors:
            for index in range(-1, -len(self.supplies) - 1, -1):
                food = True
                water = True
                if food is True:
                    if self.supplies[index].__name__ == 'FoodSupply':
                        supply = self.supplies.pop(index)
                        supply.apply(s)
                        food = False
                elif water is True:
                    if self.supplies[index].__name__ == 'WaterSupply':
                        supply = self.supplies.pop(index)
                        supply.apply(s)
                        water = False
                if food is False and water is False:
                    return

