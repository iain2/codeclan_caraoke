class Room:
    def __init__(self, room_no, capacity, entry_fee):
        self.room_no = room_no
        self.capacity = capacity
        self.entry_fee = entry_fee
        self.guest = []
        self.songs = []

    def check_in(self, guest, bar):
        if len(self.guest) < self.capacity and bar.can_guest_pay(guest, self):
            self.guest.append(guest)

    def check_out(self, guest):
        for customer in self.guest:
            if customer == guest:
                self.guest.remove(guest)

    def add_song(self, song):
        self.songs.append(song)
