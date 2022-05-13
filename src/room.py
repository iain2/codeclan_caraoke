class Room:
    def __innit__(self, room_no, capacity, entry_fee):
        self.room_no = room_no
        self.capacity = capacity
        self.entry_fee = entry_fee
        self.quests = []
        self.songs = []
