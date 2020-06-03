# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, position):
        self.name = name
        self.position = position
        self.won = False

    def move(self, direction):
        if getattr(self.position, f"{direction}_to") is not None:
            self.position = getattr(self.position, f"{direction}_to")
        else:
            print("There is nothing in that direction")
