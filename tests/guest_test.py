import unittest
from src.room import Room
from src.guest import Guest
from src.song import Song
from src.bar import Bar


class TestGuest(unittest.TestCase):
    def setUp(self):
        self.room1 = Room(1, 10, 5)
        self.song1 = Song("Whole of the moon", "the Water boys")
        self.song2 = Song("Sex on the Beach", "DJ Assualt")
        self.guest1 = Guest("larry", self.song1, 60)
        self.guest2 = Guest("Barry", self.song2, 70)
        self.guest_poor = Guest("Harry", self.song2, 3)
        self.bar1 = Bar("Jiggies", 100, [self.room1])

    def test_guest_cheer_for_favorite_song(self):
        pass

    def test_guest_can_pay(self):
        self.room1.check_in(self.guest1, self.bar1)
        self.bar1.take_entry_fee(self.room1, self.guest1)
        self.guest1.pay_entry_fee(self.room1)
        self.assertEqual(55, self.guest1.wallet)

    def test_room_has_favorite_song(self):
        self.room1.add_song(self.song1)
        self.assertEqual("Whooo!!", self.guest1.favorite_song(self.room1))

    def test_room_has_favorite_song(self):
        self.room1.add_song(self.song2)
        self.assertEqual(None, self.guest1.favorite_song(self.room1))
