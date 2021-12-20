import unittest

from project.card.card_repository import CardRepository
from project.player.advanced import Advanced


class TestAdvancedPlayer(unittest.TestCase):
    def test_init__when_all_values_legit__except_init(self):
        ap = Advanced("Test")
        self.assertEqual("Test", ap.username)
        self.assertEqual(250, ap.health)

    def test_init__when_name_empty_str__except_exception(self):
        with self.assertRaises(ValueError) as ex:
            ap = Advanced("")
        self.assertEqual("Player's username cannot be an empty string.", str(ex.exception))




    def test_player_is_dead__when_alive__except_False(self):
        ap = Advanced("Test")
        self.assertEqual(False, ap.is_dead)

    def test_player_is_dead__when_0__except_True(self):
        ap = Advanced("Test")
        ap.health = 0
        self.assertEqual(True, ap.is_dead)

    def test_player_health__when_positive__except_to_be_changed(self):
        ap = Advanced("Test")
        self.assertEqual(250, ap.health)
        ap.health = 200
        self.assertEqual(200, ap.health)

    def test_player_health__when_negative__except_exception(self):
        ap = Advanced("Test")
        with self.assertRaises(ValueError) as ex:
            ap.health = -50
            self.assertEqual("Player's health bonus cannot be less than zero.", str(ex.exception))

    def test_take_dmg__when_positive__except_health_to_be_lowered(self):
        ap = Advanced("Test")
        ap.take_damage(20)
        self.assertEqual(230, ap.health)

    def test_take_dmg__when_edge_case__except_health_to_be_0(self):
        ap = Advanced("Test")
        ap.take_damage(250)
        self.assertEqual(0, ap.health)

    def test_take_dmg__when_negative__except_exception(self):
        ap = Advanced("Test")
        with self.assertRaises(ValueError) as ex:
            ap.take_damage(-10)
        self.assertEqual("Damage points cannot be less than zero.", str(ex.exception))





if __name__ == '__main__':
    unittest.main()