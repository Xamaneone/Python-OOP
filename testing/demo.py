import unittest

def my_sum(numbers):
    if any(type(x) not in [int, float] for x in numbers):
        raise ValueError('`numbers` should be numbers')
    return sum(numbers)


class SampleTests(unittest.TestCase):
    def test_my_sum__when_numbers__expect_to_be_equal(self):
        numbers = [1, 2, 3, 4]
        actual_result = my_sum(numbers)
        expected_result = 10

        self.assertEqual(expected_result, actual_result)

    def test_my_sum__when_numbers_are_floats__and__expect_to_be_equal(self):
        numbers = [1.0, 2.0, 3.6, 4.5]
        actual_result = my_sum(numbers)
        expected_result = 11.1

        self.assertEqual(expected_result, actual_result)

    def test_my_sum__when_strings__expect_value_exception(self):
        numbers = ['a', 'b', 'c']
        with self.assertRaises(ValueError) as context:
            my_sum(numbers)


