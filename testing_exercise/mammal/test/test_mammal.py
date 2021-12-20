import unittest

from project.mammal import Mammal


class MammalTests(unittest.TestCase):
    NAME = "Cat"
    TYPE = "Mammal"
    SOUND = "Meow"
    name = 'Mammal'
    type = 'Wild'
    sound = 'Malll'


    def test_mammal_init__when_initialing__expect_to_initialize(self):
        mammal = Mammal(self.name, self.type, self.sound)
        self.assertEqual(self.name, mammal.name)
        self.assertEqual(self.type, mammal.type)
        self.assertEqual(self.sound, mammal.sound)
        self.assertEqual("animals", mammal.get_kingdom())

    def test_mammal_make_sound__when_called___expect_sound(self):
        mammal = Mammal(self.name, self.type, self.sound)
        expect = "Mammal makes Malll"
        self.assertEqual(expect, mammal.make_sound())


    def test_mammal_get_kingdom__when_called___expect_kingdom(self):
        mammal = Mammal(self.name, self.type, self.sound)
        excpect = "animals"
        self.assertEqual(excpect, mammal.get_kingdom())

    def test_mammal_info__when_called___expect_info(self):
        mammal = Mammal(self.name, self.type, self.sound)
        excpect = f"Mammal is of type Wild"
        self.assertEqual(excpect, mammal.info())

    def test_mammal_name(self):
        mammal = Mammal(self.NAME, self.TYPE, self.SOUND)
        expected_result = self.NAME
        self.assertEqual(self.NAME, mammal.name)

    def test_mammal_type(self):
        mammal = Mammal(self.NAME, self.TYPE, self.SOUND)
        expected_result = self.TYPE
        self.assertEqual(expected_result, mammal.type)

    def test_mammal_sound(self):
        mammal = Mammal(self.NAME, self.TYPE, self.SOUND)
        expected_result = self.SOUND
        self.assertEqual(expected_result, mammal.sound)

    def test_mammal_kingdom_initial(self):
        mammal = Mammal(self.NAME, self.TYPE, self.SOUND)
        result = mammal._Mammal__kingdom
        expected_result = "animals"
        self.assertEqual(result, expected_result)

    def test_mammal_make_sound__expect_make_sound_message(self):
        mammal = Mammal(self.NAME, self.TYPE, self.SOUND)
        expected_result = f"{self.NAME} makes {self.SOUND}"
        actual_result = mammal.make_sound()
        self.assertEqual(expected_result, actual_result)

    def test_mammal_info__expect_info_message(self):
        mammal = Mammal(self.NAME, self.TYPE, self.SOUND)
        expected_result = f"{self.NAME} is of type {self.TYPE}"
        actual_result = mammal.info()
        self.assertEqual(expected_result, actual_result)

    def test_mammal__get_kingdom__expect_get_kingdom(self):
        mammal = Mammal(self.NAME, self.TYPE, self.SOUND)
        expected_result = "animals"
        actual_result = mammal.get_kingdom()
        self.assertEqual(expected_result, actual_result)





if __name__ == '__main__':
    unittest.main()