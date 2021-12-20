import unittest

from worker import Worker


class WorkerTests(unittest.TestCase):
    name = 'Test Worker'
    salary = 1000
    energy = 3

    def setUp(self):
        self.worker = Worker(self.name, self.salary, self.energy)

    def test_initializing_with_correct_name_salary_energy(self):
        #  Test if the worker is initialized with correct name, salary and energy

        self.assertEqual(self.name, self.worker.name)
        self.assertEqual(self.salary, self.worker.salary)
        self.assertEqual(self.energy, self.worker.energy)

    def test_worker__when_rest_is_called_expect_energy_to_be_incremented(self):
        #  Test if the worker is initialized with correct name, salary and energy
        self.worker.rest()
        self.assertEqual(self.energy + 1, self.worker.energy)

    def test_worker_work__when_energy_is_0__expect_expection(self):
        #  Test if an error is raised if the worker tries to work with negative energy or equal to 0
        self.worker.energy = 0
        with self.assertRaises(Exception):
            self.worker.work()

    def test_worker_work__when_energy_is_above_0__expect_money_to_be_incrased_by_salary(self):
        #  Test if the worker's money is increased by his salary correctly after the work method is called
        self.worker.work()
        self.assertEqual(self.salary, self.worker.money)

    def test_worker_work__when_energy_is_above_0__expect_energy_to_be_decremented(self):
        #  Test if the worker's energy is decreased after the work method is called
        self.worker.work()
        self.assertEqual(self.energy - 1, self.worker.energy)

    def test_worker_get_info__expect_correct_values(self):
        #  Test if the get_info method returns the proper string with correct values
        expected_info = f'{self.name} has saved 0 money.'
        actual_info = self.worker.get_info()
        self.assertEqual(expected_info, actual_info)


if __name__ == '__main__':
    unittest.main()