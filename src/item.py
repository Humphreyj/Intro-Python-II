from player import Player

class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return f"{self.name} - {self.description}"
    
    def on_take(self):
        print(f'\nYOU HAVE PICKED UP {self.name.upper()}\n')

    def on_drop(self):
        print(f'\nYOU HAVE DROPPED {self.name.upper()}\n')