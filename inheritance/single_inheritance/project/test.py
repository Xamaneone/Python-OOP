from single_inheritance.project.animal import Animal
from single_inheritance.project.dog import Dog
import unittest


class Tests(unittest.TestCase):
    def test_animal(self):
        a = Animal()
        res = a.eat()
        self.assertEqual(res, "eating...")

    def test_dog(self):
        d = Dog()
        res = d.bark()
        self.assertEqual(res, "barking...")
        self.assertEqual(d.__class__.__bases__[0].__name__, "Animal")


if __name__ == "__main__":
    unittest.main()
