# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, position):
        self.name = name
        self.position = position
        self.items = []

    def move(self, direction):
        if getattr(self.position, f"{direction}_to") is not None:
            self.position = getattr(self.position, f"{direction}_to")
        else:
            print("There is nothing in that direction")

    def get_item(self, item):
        if self.position.items.count(item) > 0:
            self.items.append(item)
            self.position.items.remove(item)
            item.get()
        else:
            print('There is nothing to take')

    def drop_item(self, item):
        if self.items.count(item) > 0:
            self.position.items.append(item)
            self.items.remove(item)
            item.drop()
        else:
            print('There is nothing to drop')

    def check_inv(self):
        if not self.items:
            print('You are poor and alone. Good luck.')
        else:
            print("You have: ")
            for item in self.items:
                print(item.name)