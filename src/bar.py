class Bar:
    def __init__(self, name, till, room_list):
        self.name = name
        self.till = till
        self.rooms = room_list

    def take_entry_fee(self, room, guest):
        if guest.wallet >= room.entry_fee and self.can_guest_pay(guest, room):
            self.till += room.entry_fee

    def can_guest_pay(self, guest, room):
        if guest.wallet >= room.entry_fee:
            return True
        return False
