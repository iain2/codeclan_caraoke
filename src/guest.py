class Guest:
    def __init__(self, name, fav_song, wallet):
        self.name = name
        self.fav_song = fav_song
        self.wallet = wallet

    def pay_entry_fee(self, room):
        self.wallet -= room.entry_fee

    def favorite_song(self, room):
        for song in room.songs:
            if self.fav_song == song:
                return "Whooo!!"
