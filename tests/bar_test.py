import unittest
from src.room import Room
from src.guest import Guest
from src.song import Song
from src.bar import Bar


class TestBar(unittest.TestCase):
    def setUp(self):
        self.room1 = Room(1, 10, 8)
        self.room2 = Room(2, 15, 7)
        self.song1 = Song("Whole of the moon", "the Water boys")
        self.song2 = Song("Sex on the Beach", "DJ Assualt")
        self.guest1 = Guest("larry", self.song1, 60)
        self.guest2 = Guest("Barry", self.song2, 70)
        self.guest_poor = Guest("Harry", self.song2, 3)
        self.bar1 = Bar("Jiggies", 100, [self.room1, self.room2])

    def test_bar_can_take_entry_fee(self):
        self.room1.check_in(self.guest1, self.bar1)
        self.bar1.take_entry_fee(self.room1, self.guest1)
        self.assertEqual(108, self.bar1.till)

    def test_bar_entry_when_guest_has_no_money(self):
        self.room1.check_in(self.guest_poor, self.bar1)
        self.bar1.take_entry_fee(self.room1, self.guest_poor)
        self.assertEqual(100, self.bar1.till)

    def test_can_guest_pay(self):
        self.assertEqual(True, self.bar1.can_guest_pay(self.guest1, self.room1))

    def test_can_guest_pay2(self):
        self.assertEqual(False, self.bar1.can_guest_pay(self.guest_poor, self.room1))
