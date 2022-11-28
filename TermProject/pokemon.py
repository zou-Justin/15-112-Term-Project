#Justin Zou (justinzo)
#Pokemon
import random

class Moves():
    def __init__(self,dmg,name,level):
        self.dmg = dmg + (level*3)
        self.moveName = name
    def __repr__(self):
        return self.moveName
    def getMoveName(self):
        return self.moveName
    def getDmg(self):
        return self.dmg

class Pokemon():
    def __init__(self,type,name,level,sprite,moves):
        self.type = type
        self.name = name
        self.dmg = level * 30
        self.defense = level // 1.3
        self.level = level
        self.maxHealth = level * 20 + random.randint(0,130)
        self.health = self.maxHealth
        self.speed = level * random.randint(4,9)
        self.sprite = sprite
        self.expToNextLevel = level * 200
        self.exp = 0
        self.moves = moves
    
    def getSprite(self):
        return self.sprite

    def setSprite(self,newSprite):
        self.sprite = newSprite

    def getType(self):
        return self.type
    
    def getName(self):
        return self.name
    
    def getLevel(self):
        return self.level

    def getHealth(self):
        return self.health
    
    def getMaxHealth(self):
        return self.maxHealth
    
    def setHealthMax(self):
        self.health = self.maxHealth

    def getMoves(self,index):
        return self.moves[index]

    def getAllMoves(self):
        return self.moves

    def setMoves(self,newMoves):
        self.moves = newMoves

    def takeDmg(self,dmg):
        self.health -= abs(dmg - self.defense)

    def gainExp(self,amount):
        self.exp += amount
        if self.exp >= self.expToNextLevel:
            self.level += 1
            self.exp -= self.expToNextLevel
            self.expToNextLevel = self.level * 200
    
    
    
