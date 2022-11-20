#Justin Zou
#Pokemon
# import linter
from cmu_112_graphics import *
from pokemon import *
from person import *
import random


# Start Screen
def startScreen_redrawAll(app,canvas):
    canvas.create_image(app.width/2, app.height/2, image=ImageTk.PhotoImage(app.startScreenImg2))

def startScreen_keyPressed(app,event):
    app.mode = 'game'
# ========================================================================

# Game Screen
def game_redrawAll(app,canvas):
    # sprite = app.sprites[app.spriteCounter]
    canvas.create_image(app.width/2,app.height/2,image=ImageTk.PhotoImage(app.background))
    #sprite
    canvas.create_image(app.width/2 + app.player.getX(), app.height/2 + app.player.getY(), image=ImageTk.PhotoImage(app.sprite))
    

def game_keyPressed(app,event):
    if (event.key == "Left"):
        app.player.moveLeft()
        encounterPokemon(app)
    elif (event.key ==  "Right"):
        app.player.moveRight()
        encounterPokemon(app)
    elif (event.key == 'Up'):
        app.player.moveUp()
        encounterPokemon(app)
    elif (event.key == "Down"):
        app.player.moveDown()
        encounterPokemon(app)

    

def game_timerFired(app):
    pass
# ========================================================================


# combat Screen
def combat_redrawAll(app,canvas):
    canvas.create_image(app.width/2, app.height/2, image=ImageTk.PhotoImage(app.combatScreen))
    canvas.create_image(app.width/2, app.height/2, image=ImageTk.PhotoImage(app.enemyPokemon.getSprite()))



def combat_keyPressed(app,event):
    if (event.key == 'r'):
        app.mode = 'game'
   
# ========================================================================

# General Functions

def encounterPokemon(app):
    chance = random.randrange(1,100)
    if (chance <= 4):
        app.mode = 'combat'
        fightPokemon(app)

def fightPokemon(app):
    randomIndex = random.randint(0,len(app.type)-1)
    randomPokemonIndex = random.randint(0,len(app.name)-1)
    randLevel = random.randint(5,100)
    randSprite = random.randint(0,len(app.pokemonSprites)-1)
    enemyPokemon = Pokemon(app.type[randomIndex],app.name[randomPokemonIndex],randLevel,app.pokemonImages[randSprite])
    app.enemyPokemon = enemyPokemon

# ========================================================================
#Spritesheet is taken https://www.deviantart.com/mohammadataya/art/Pokemon-Trainer-Calem-By-Tedbited15-Updated-397076725
def appStarted(app):
    app.mode = 'startScreen'
    app.player = Player(0,0)
    app.startScreenImg = app.loadImage('img/pokemonImg.jpg')
    app.startScreenImg2 = app.scaleImage(app.startScreenImg, 4/7)
    app.background = app.loadImage('img/pokemonTestBackground.png')
    app.combatScreen = app.loadImage('img/combat.png')
    app.pokemonSprites = ['img/pikachu.jpg','img/bulbasaur.png','img/charmander.jpg','img/squritle.png']
    app.pokemonImages = []
    for i in range(len(app.pokemonSprites)):
        pokemon = app.loadImage( app.pokemonSprites[i]) 
        app.pokemonImages.append(pokemon)
    print(app.pokemonImages)

    app.sprite = app.loadImage('img/player.png') 
    app.type = ['fire','water','grass','electric','flying','normal']
    app.name = ['pikachu','bulbasaur','charmander','squritle']
    app.enemyPokemon = None
    # app.sprites = [ ]
    # for i in range(4):
    #     for j in range(4):
    #         sprite = sprite.crop((30+160*j, 30+160*i, 230+160*j, 250+160*i))
    #         app.sprites.append(sprite)
    # app.spriteCounter = 0


runApp(width=700, height=400)


# def main():
#     linter.lint()


# if __name__ == '__main__':
#     main()
