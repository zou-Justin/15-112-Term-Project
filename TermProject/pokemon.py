class Pokemon():
    def __init__(self,type,name,level,health,sprite):
        self.type = type
        self.name = name
        self.level = level
        self.health = health
        self.sprite = sprite
        


class Moves(Pokemon):
    def __init__(self):
        super().__init__()