import unittest
from src.room import Room
from src.guest import Guest
from src.song import Song
from src.bar import Bar


class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room1 = Room(1, 10, 5)
        self.song1 = Song("Whole of the moon", "the Water boys")
        self.song2 = Song("Sex on the Beach", "DJ Assualt")
        self.guest1 = Guest("larry", self.song1, 60)
        self.guest2 = Guest("Barry", self.song2, 70)
        self.guest_poor = Guest("Harry", self.song2, 3)
        self.bar1 = Bar("Jiggies", 100, [self.room1])

    def test_room_can_check_in_guest(self):
        self.room1.check_in(self.guest1, self.bar1)
        self.assertEqual([self.guest1], self.room1.guest)

    def test_room_can_check_out_guest(self):
        self.room1.check_in(self.guest1, self.bar1)
        self.room1.check_out(self.guest1)
        self.assertEqual([], self.room1.guest)

    def test_room_check_out_with_no_guest(self):

        self.room1.check_out(self.guest1)
        self.assertEqual([], self.room1.guest)

    def test_room_check_out_wrong_guest(self):
        self.room1.check_in(self.guest1, self.bar1)
        self.room1.check_out(self.guest2)
        self.assertEqual([self.guest1], self.room1.guest)

    def test_song_can_add_to_room(self):
        self.room1.add_song(self.song1)
        self.assertEqual([self.song1], self.room1.songs)

    def test_room_capacity(self):
        counter = 0
        while counter <= 12:
            self.room1.check_in(self.guest1, self.bar1)
            counter += 1
        self.assertEqual(10, len(self.room1.guest))

    def test_reject_poor_guest(self):
        self.room1.check_in(self.guest_poor, self.bar1)
        self.assertEqual([], self.room1.guest)
