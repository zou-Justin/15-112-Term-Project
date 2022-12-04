#Justin Zou (justinzo)
#Pokemon
import random


class Pokemon():
    def __init__(self,type,name,level,sprite,moves):
        self.type = type
        self.name = name
        self.defense = 0 #level//10
        self.level = level
        self.maxHealth = int((level * 10) + random.randint(0,130))
        self.health = self.maxHealth
        self.speed = level * random.randint(4,9)
        self.sprite = sprite
        self.expToNextLevel = level * 200
        self.exp = 0
        self.moves = moves
    
    def getSprite(self):
        return self.sprite

    def __repr__(self):
        return self.name

    def setDefense(self,newDefense):
        self.defense = newDefense

    def getDefense(self):
        return self.defense

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
        if (dmg > self.defense):
            self.health -= abs(dmg - self.defense)

    def healDmg(self,dmg):
        self.health += dmg

    def gainExp(self,amount):
        self.exp += amount
        if self.exp >= self.expToNextLevel:
            self.level += 1
            self.exp -= self.expToNextLevel
            self.expToNextLevel = self.level * 200
    

class Moves(Pokemon):
    def __init__(self,dmg,name,level):
        self.dmg = dmg + (level * 3)
        self.moveName = name
        self.isDefensive = False
        self.priority = 0

    def makeDefensive(self):
        self.isDefensive = True
        self.dmg = 0

    def getPokemonName(self):
        return super().getName()

    def increaseDmg(self,other):
        if (self.isDefensive):
            other.dmg *= 1.2

    def isFast(self,index):
        self.priority += index
    
    def getSpeed(self):
        return self.priority
    
    def __repr__(self):
        return self.moveName

    def getMoveName(self):
        return self.moveName

    def minusDmg(self,amount):
        self.dmg -= amount

    def getDmg(self):
        return self.dmg
    
    
