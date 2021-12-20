import unittest

from project.factory.paint_factory import PaintFactory


class Test_Paint_Factory(unittest.TestCase):
    def test_init__when_all__legit(self):
        pf = PaintFactory("Test", 10)
        self.assertEqual('Test', pf.name)
        self.assertEqual(10, pf.capacity)
        self.assertEqual(["white", "yellow", "blue", "green", "red"], pf.valid_ingredients)

    def test_add_ingredient__when_adding_5(self):
        pf = PaintFactory("Test", 10)
        pf.add_ingredient('white', 5)
        self.assertEqual({'white': 5}, pf.ingredients)

    def test_add_ingredient__when_adding_to_the_limit(self):
        pf = PaintFactory("Test", 10)
        pf.add_ingredient('white', 10)
        self.assertEqual({'white': 10}, pf.ingredients)

    def test_add_ingerdiend__when_not_enough_space__expect_exception(self):
        pf = PaintFactory("Test", 10)
        with self.assertRaises(ValueError) as ex:
            pf.add_ingredient('white', 11)
        self.assertEqual("Not enough space in factory", str(ex.exception))

    def test_add_ingerdiend__when_not_valid_type__expect_exception(self):
        pf = PaintFactory("Test", 10)
        with self.assertRaises(TypeError) as ex:
            pf.add_ingredient('purple', 5)
        self.assertEqual("Ingredient of type purple not allowed in PaintFactory", str(ex.exception))

    def test_remove_ingredient__when_happy_case(self):
        pf = PaintFactory("Test", 10)
        pf.add_ingredient('white', 5)
        pf.remove_ingredient('white', 5)
        self.assertEqual(0, len(pf.ingredients))




if __name__ == '__main__':
    unittest.main()