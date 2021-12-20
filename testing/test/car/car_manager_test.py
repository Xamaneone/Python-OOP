import unittest

from car_manager import Car


class CarTests(unittest.TestCase):
    make = 'make'
    model = 'model'
    fuel_consumption = 10
    fuel_capacity = 100

    def test_car_make_setter__when_None__expect_exception(self):
        car = Car(self.make, self.model, self.fuel_consumption, self.fuel_capacity)
        with self.assertRaises(Exception) as context:
            car.make = None

        self.assertEqual('Make cannot be null or empty!', str(context.exception))

    def test_car_make_setter__when_empty__expect_exception(self):
        car = Car(self.make, self.model, self.fuel_consumption, self.fuel_capacity)
        with self.assertRaises(Exception) as context:
            car.make("")

        self.assertEqual('Make cannot be null or empty!', str(context.exception))


    def test_car_make_setter__when_provided_test__expect_make_to_be_changed(self):
        car = Car(self.make, self.model, self.fuel_consumption, self.fuel_capacity)
        expect = "test"
        car.make(expect)
        self.assertEqual(expect, car.make)

    def test_car_model_setter__when_None__expect_exception(self):
        car = Car(self.make, self.model, self.fuel_consumption, self.fuel_capacity)
        with self.assertRaises(Exception) as context:
            car.model = None

        self.assertEqual('Model cannot be null or empty!', str(context.exception))

    def test_car_model_setter__when_empty__expect_exception(self):
        car = Car(self.make, self.model, self.fuel_consumption, self.fuel_capacity)
        with self.assertRaises(Exception) as context:
            car.model('')

        self.assertEqual('Model cannot be null or empty!', str(context.exception))


    def test_car_model_setter__when_provided_test__expect_model_to_be_changed(self):
        car = Car(self.make, self.model, self.fuel_consumption, self.fuel_capacity)
        expect = "test"
        car.model(expect)
        self.assertEqual(expect, car.model)

    def test_car_fuel_consumption_getter__when_changed__expect_to_be_changed(self):
        car = Car(self.make, self.model, self.fuel_consumption, self.fuel_capacity)
        car.fuel_consumption(5)
        self.assertEqual(5, car.fuel_consumption)

    def test_car_fuel_consumption_getter__when_changed_with_negative__expect_exception(self):
        car = Car(self.make, self.model, self.fuel_consumption, self.fuel_capacity)
        with self.assertRaises(Exception):
            car.fuel_consumption(-5)


    def test_car_fuel_consumption_setter__when_None__expect_exception(self):
        car = Car(self.make, self.model, self.fuel_consumption, self.fuel_capacity)
        with self.assertRaises(Exception):
            car.fuel_consumption(None)

    def test_car_fuel_consumption_setter__when_changing__expect_to_be_changed(self):
        car = Car(self.make, self.model, self.fuel_consumption, self.fuel_capacity)
        car.fuel_consumption(14)
        self.assertEqual(14, car.fuel_consumption)

    def test_car_refuel__when_provided_fuel_is_0__expect_exception(self):
        car = Car(self.make, self.model, self.fuel_consumption, self.fuel_capacity)
        with self.assertRaises(Exception):
            car.refuel(0)

    def test_car_refuel__when_provided_fuel_is_negative__expect_exception(self):
        car = Car(self.make, self.model, self.fuel_consumption, self.fuel_capacity)
        with self.assertRaises(Exception):
            car.refuel(-1)

    def test_car_refuel__when_provided_fuel_is_correct__expect_to_increase_fuel_amount_by_provided_fuel(self):
        car = Car(self.make, self.model, self.fuel_consumption, self.fuel_capacity)
        fuel = 50
        car.refuel(fuel)
        self.assertEqual(fuel, car.fuel_amount)

    def test_car_refuel__when_provided_fuel_is_more_than_fuel_capacity__expect_to_increase_fuel_amount_to_fuel_capacity(self):
        car = Car(self.make, self.model, self.fuel_consumption, self.fuel_capacity)
        fuel = 50
        car.refuel(car.fuel_capacity * 3)
        self.assertEqual(100, car.fuel_amount)


    def test_car_fuel_amount_setter__when_changed__expect_to_be_changed(self):
        car = Car(self.make, self.model, self.fuel_consumption, self.fuel_capacity)
        car.fuel_amount(5)
        self.assertEqual(5, car.fuel_amount)

    def test_car_fuel_amount_setter__when_changed_with_negative__expect_exception(self):
        car = Car(self.make, self.model, self.fuel_consumption, self.fuel_capacity)
        with self.assertRaises(Exception):
            car.fuel_amount(-50)

    def test_car_fuel_amount_setter__when_None__expect_exception(self):
        car = Car(self.make, self.model, self.fuel_consumption, self.fuel_capacity)
        with self.assertRaises(Exception):
            car.fuel_amount(None)

    def test_car_fuel_amount_setter__when_negative__expect_exception(self):
        car = Car(self.make, self.model, self.fuel_consumption, self.fuel_capacity)
        with self.assertRaises(Exception):
            car.fuel_amount(-50)

    def test_car_drive__when_enough_fuel__expect_lowered_fuel(self):
        car = Car(self.make, self.model, self.fuel_consumption, self.fuel_capacity)
        car.fuel_capacity = 50
        car.drive(100)
        self.assertEqual(40, car.fuel_amount)

    def test_car_drive__when_not_enough_fuel__expect_exception(self):
        car = Car(self.make, self.model, self.fuel_consumption, self.fuel_capacity)
        car.fuel_capacity = 50
        with self.assertRaises(Exception):
            car.drive(1000)

    def test_car_fuel_capacity_setter__when_None__except_exception(self):
        car = Car(self.make, self.model, self.fuel_consumption, self.fuel_capacity)
        with self.assertRaises(Exception):
            car.fuel_capacity(None)

    def test_car_fuel_capacity_setter__when_changed__except_to_be_changed(self):
        car = Car(self.make, self.model, self.fuel_consumption, self.fuel_capacity)
        car.fuel_capacity(60)
        self.assertEqual(60, car.fuel_capacity)

    def test_car_fuel_capacity_setter__when_negative__except_exception(self):
        car = Car(self.make, self.model, self.fuel_consumption, self.fuel_capacity)
        with self.assertRaises(Exception):
            car.fuel_capacity(-16)






if __name__ == '__main__':
    unittest.main()
