import random

class Pokemon():
    def __init__(self,type,name,level,sprite):
        self.type = type
        self.name = name
        self.level = level
        self.health = level * random.randint(25,47)
        self.sprite = sprite
    
    def getSprite(self):
        return self.sprite

    def getType(self):
        return self.type
    
    def getName(self):
        return self.name
    
    def getLevel(self):
        return self.level
    
    


class Moves(Pokemon):
    def __init__(self):
        super().__init__()