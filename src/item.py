class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def get(self):
        print(f'You now have {self.name}')
        
    def drop(self):
        print(f'{self.name} was dropped')