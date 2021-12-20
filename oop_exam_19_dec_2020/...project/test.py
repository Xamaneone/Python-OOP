from unittest import TestCase

from project.bunker import Bunker
from project.medicine.painkiller import Painkiller
from project.medicine.salve import Salve
from project.supply.food_supply import FoodSupply
from project.supply.water_supply import WaterSupply
from project.survivor import Survivor


class TestMyProject(TestCase):
    def test_init__correct(self):
        bunker = Bunker()
        s1 = Survivor("Pesho", 12)
        s2 = Survivor("Gosho", 16)
        s3 = Survivor("Kocko", 19)

        bunker.add_survivor(s1)
        bunker.add_survivor(s2)
        bunker.add_survivor(s3)


        pk1 = Painkiller()
        pk2 = Painkiller()
        salve1 = Salve()
        salve2 = Salve()

        bunker.add_medicine(pk1)
        bunker.add_medicine(pk2)
        bunker.add_medicine(salve1)
        bunker.add_medicine(salve2)


        food1 = FoodSupply()
        food2 = FoodSupply()
        water1 = WaterSupply()
        water2 = WaterSupply()

        bunker.add_supply(food1)
        bunker.add_supply(food2)
        bunker.add_supply(water1)
        bunker.add_supply(water2)

        self.assertEqual(3, len(bunker.survivors))
        self.assertEqual(4, len(bunker.medicine))
        self.assertEqual(4, len(bunker.supplies))

