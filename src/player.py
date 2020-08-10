# Write a class to hold player information, e.g. what room they are in
# currently.
class Creature:
    def __init__(self,name,health,size):
        self.name = name
        self.health = health
        self.size = size

       
class Monster(Creature):
    def __init__(self,family,name,size,health):
        self.family = family

        super(Monster,self).__init__(name, health, size)

    def __str__(self):
        return f"I am {self.name} of family {self.family}, i am size {self.size} and I have {self.health} HP"
greg = Monster("Goblin","Greg"," Large", "54")



class Player(Creature):
    def __init__(self,name,health,size,level,xp,location,inventory):
        self.level = level
        self.xp = xp
        self.location = location
        self.inventory = [inventory]

        super(Player,self).__init__(name, health, size)
    def __str__(self):
        return f"I am {self.name} a level {self.level} adventurer. I am {self.size}, I have {self.xp} xp, and I am currently in {self.location}. I have {self.health} hp and my inventory is {self.inventory}"

