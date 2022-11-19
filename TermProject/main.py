# #Justin Zou
# #Pokemon

from cmu_112_graphics import *
from pokemon import *
from person import *
import random


# Start Screen
def startScreen_redrawAll(app,canvas):
    canvas.create_image(app.player.x, app.player.y, image=ImageTk.PhotoImage(app.startScreenImg2))

def startScreen_keyPressed(app,event):
    app.mode = 'game'
# ========================================================================

# Game Screen
def game_redrawAll(app,canvas):
    sprite = app.sprites[app.spriteCounter]
    canvas.create_image(app.width/2, app.height/2, image=ImageTk.PhotoImage(app.background))
    canvas.create_image(200, 200, image=ImageTk.PhotoImage(sprite))
    

def game_keyPressed(app,event):
    if (event.key == "Left"):
        #move player left
        pass
    
    elif (event.key ==  "Right"):
        #move player right
        pass

def game_timerFired(app):
    app.spriteCounter = (1 + app.spriteCounter) % len(app.sprites)
    chance = random.randrange(1/10)
    if (chance % 3 == 0):
        encounterPokemon(app)
# ========================================================================


# combat Screen
def combat_redrawAll(app,canvas):
    sprite = app.sprites[app.spriteCounter]
    canvas.create_image(app.width/2, app.height/2, image=ImageTk.PhotoImage(app.background))
    canvas.create_image(200, 200, image=ImageTk.PhotoImage(sprite))
    

def combat_keyPressed(app,event):
    if (event.key == "Left"):
        #move player left
        pass
    
    elif (event.key ==  "Right"):
        #move player right
        pass

def combat_timerFired(app):
    app.spriteCounter = (1 + app.spriteCounter) % len(app.sprites)
    chance = random.randrange(1/10)
    if (chance % 3 == 0):
        encounterPokemon(app)
# ========================================================================

def encounterPokemon(app):
    app.mode = 'combat'




# ========================================================================
#Spritesheet is taken https://www.deviantart.com/mohammadataya/art/Pokemon-Trainer-Calem-By-Tedbited15-Updated-397076725
def appStarted(app):
    app.mode = 'startScreen'
    app.player = Player(app.width/2,app.height/2)
    app.startScreenImg = app.loadImage('pokemonImg.jpg')
    app.startScreenImg2 = app.scaleImage(app.startScreenImg, 4/7)
    app.background = app.loadImage('pokemonTestBackground.png')
    app.combatScreen = app.loadImage('pokemonTestBackground.png')
    sprite = app.loadImage('spriteSheet.png') 
    app.sprites = [ ]
    for i in range(4):
        for j in range(4):
            sprite = sprite.crop((30+160*j, 30+160*i, 230+160*j, 250+160*i))
            app.sprites.append(sprite)
    app.spriteCounter = 0


runApp(width=700, height=400)


    

# def keyPressed(app, event):
#     pass


# def redrawAll(app,canvas):
#     canvas.create_image(200, 300, image=ImageTk.PhotoImage(app.image1))
#     canvas.create_image(500, 300, image=ImageTk.PhotoImage(app.image2))



