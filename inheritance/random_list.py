import random

class RandomList(list):
    def get_random_element(self):
        element_index = random.randint(0, len(self) - 1)
        element = self[element_index]
        self.pop(element_index)
        return element



rl = RandomList([1, 2, 3, 4, 5])
print(rl)
rl.append(-1)
print(rl)
while rl:
    print(rl.get_random_element())


# test second zero
import unittest
from unittest import mock
import random

class RandomListTests(unittest.TestCase):
    def test_zero_second(self):
        mocked_choice = lambda x: 6
        with mock.patch('random.choice', mocked_choice):
            li = RandomList()
            li.append(6)
            li.append(1.3)
            li.append(10)
            li.pop()
            li.reverse()
            self.assertEqual(sum(li), 7.3)
            self.assertEqual(li.get_random_element(),6)


if __name__ == '__main__':
    unittest.main()