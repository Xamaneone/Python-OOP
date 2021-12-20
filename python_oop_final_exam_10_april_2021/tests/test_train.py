import unittest

from project.train.train import Train


class TestTrain(unittest.TestCase):
    def test_init__when_correct__except_to_be_inited(self):
        train = Train("test", 100)

        self.assertEqual("test", train.name)
        self.assertEqual(100, train.capacity)
        self.assertEqual([], train.passengers)

    def test_add__when_correct__except_to_be_added(self):
        train = Train("test", 100)

        self.assertEqual(0, len(train.passengers))
        train.add("Test")
        self.assertEqual(1, len(train.passengers))
        train.add("Pesho")
        self.assertEqual(2, len(train.passengers))
        self.assertEqual("Added passenger Test2", train.add("Test2"))

    def test_add__when_out_of_capacity__except_exception(self):
        train = Train("test", 1)

        train.add("Test1")
        with self.assertRaises(ValueError) as ex:
            train.add("Test2")
        self.assertEqual("Train is full", str(ex.exception))

    def test_add__when_passenger_exist__except_exception(self):
        train = Train("test", 100)

        train.add("Test")
        with self.assertRaises(ValueError) as ex:
            train.add("Test")
        self.assertEqual("Passenger Test Exists", str(ex.exception))

    def test_remove__when_passenger_exist__except_to_be_removed(self):
        train = Train("test", 100)

        train.add("Test")
        self.assertEqual(1, len(train.passengers))
        train.remove("Test")
        self.assertEqual(0, len(train.passengers))

    def test_remove__when_passenger_not_exist__except_exception(self):
        train = Train("test", 100)

        train.add("Test")
        self.assertEqual(1, len(train.passengers))
        with self.assertRaises(ValueError) as ex:
            train.remove("Pesho")
        self.assertEqual("Passenger Not Found", str(ex.exception))
        self.assertEqual(1, len(train.passengers))