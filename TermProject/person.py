#Justin Zou (justinzo)
#Pokemon
import random

#class for the player character and its x and y positions and pokemon
class Player():
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.currentIndex = 0
        self.pokemons = []

    def getX(self):
        return self.x
    
    def getY(self):
        return self.y

    def setX(self,newX):
        self.x = newX
    
    def setY(self,newY):
        self.y = newY

    def catchPokemon(self,pokemon):
        if (len(self.pokemons) < 6):
            self.pokemons.append(pokemon)

    def pokemonAmount(self):
        return len(self.pokemons)

    def increaseIndex(self):
        self.currentIndex += 1

    def getPokemon(self):
        return self.pokemons

    def getCurrentPokemon(self):
        index = self.currentIndex
        index = index % 6
        return self.pokemons[index]

    def getCurrentIndex(self):
        return self.currentIndex

    def setCurrentIndex(self):
        self.currentIndex = self.currentIndex % 6

    def getPokemonIndex(self,index):
        return self.pokemons[index]

    def moveLeft(self):
        self.x -= 15
    
    def moveRight(self):
        self.x += 15
    
    def moveUp(self):
        self.y -= 15

    def moveDown(self):
        self.y += 15
