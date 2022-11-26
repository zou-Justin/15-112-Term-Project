#Justin Zou (justinzo)
#Pokemon
from cmu_112_graphics import *
from pokemon import *
from person import *
import random

'''
Relaistically need types
need speed stat

'''




# Start Screen
def startScreen_redrawAll(app,canvas):
    canvas.create_image(app.width/2, app.height/2, image=ImageTk.PhotoImage(app.startScreenImg2))
    canvas.create_text(app.width/2,app.height-app.width/12, text=f'Press Enter to Start',
                                            fill='black', font='Helvetica 10')
def startScreen_keyPressed(app,event):
    if (event.key == "Enter"):
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

# ========================================================================

#Bag Screen

def bag_redrawAll(app,canvas):
    canvas.create_image(app.width/2,app.height/2,image=ImageTk.PhotoImage(app.bagImg))

def bag_mousePressed(app,event):
    print(event.x,event.y)
    if (91 - app.xLength*2 <= event.x <= 91 + app.xLength*2 and (311 - app.yLength) <= event.y <= (311 + app.yLength)):
        app.mode = 'combat'

# ========================================================================

#Pokemon Screen

def Pokemon_redrawAll(app,canvas):
    canvas.create_image(app.width/2,app.height/2,image=ImageTk.PhotoImage(app.bagImg))

def Pokemon_mousePressed(app,event):
    print(event.x,event.y)
    if (91 - app.xLength*2 <= event.x <= 91 + app.xLength*2 and (311 - app.yLength) <= event.y <= (311 + app.yLength)):
        app.mode = 'combat'

# ========================================================================




# combat Screen
def combat_redrawAll(app,canvas):
    canvas.create_image(app.width/2, app.height/2, image=ImageTk.PhotoImage(app.combatScreen))
    canvas.create_image(app.width/2 + 140, app.height/2 -80, image=ImageTk.PhotoImage(app.enemyPokemon.getSprite()))
    canvas.create_image(app.width/2 - 140, app.height/2 + 30, image=ImageTk.PhotoImage(app.playerPokemon.getSprite()))
    canvas.create_text(140,70, text=f'{app.enemyPokemon.getName()}',fill='black', font='Helvetica 10')
    canvas.create_text(430,205, text=f'{app.playerPokemon.getName()}',fill='black', font='Helvetica 10')
    canvas.create_text(129,96, text=f'{app.enemyPokemon.getHealth()} / {app.enemyPokemon.getMaxHealth()}',fill='black', font='Helvetica 10')
    canvas.create_text(525,245, text=f'{app.playerPokemon.getHealth()} / {app.playerPokemon.getMaxHealth()}',fill='black', font='Helvetica 10')
    canvas.create_text(291,71, text=f'Lv: {app.enemyPokemon.getLevel()}',fill='black', font='Helvetica 10')
    canvas.create_text(569,205, text=f'Lv: {app.playerPokemon.getLevel()}',fill='black', font='Helvetica 10')
    if (app.battle == False):
        #item
        canvas.create_rectangle(187-app.xLength*2 ,352 + app.yLength,187+app.xLength*2,352-app.yLength,fill ='white')
        canvas.create_text(187,352, text=f'Item',fill='black', font='Helvetica 10')
        #run
        canvas.create_rectangle(483-app.xLength*2 ,352 + app.yLength,483+app.xLength*2,352-app.yLength,fill ='white')
        canvas.create_text(483,352, text=f'Run',fill='black', font='Helvetica 10')  
        #fight
        canvas.create_rectangle(187-app.xLength*2 ,300 + app.yLength,187+app.xLength*2,300-app.yLength,fill ='white')
        canvas.create_text(187,300, text=f'Fight',fill='black', font='Helvetica 10')
        #bag
        canvas.create_rectangle(483-app.xLength*2 ,300 + app.yLength,483+app.xLength*2,300-app.yLength,fill ='white')
        canvas.create_text(483,300, text=f'Bag',fill='black', font='Helvetica 10')
    elif (app.battle == True):
        #move1
        canvas.create_rectangle(187-app.xLength*2 ,352 + app.yLength,187+app.xLength*2,352-app.yLength,fill ='white')
        canvas.create_text(187,352, text=f'{app.playerPokemon.getMoves(2).getMoveName()}',fill='black', font='Helvetica 10')
        #move2
        canvas.create_rectangle(483-app.xLength*2 ,352 + app.yLength,483+app.xLength*2,352-app.yLength,fill ='white')
        canvas.create_text(483,352, text=f'{app.playerPokemon.getMoves(1).getMoveName()}',fill='black', font='Helvetica 10')
        #move3
        canvas.create_rectangle(187-app.xLength*2 ,300 + app.yLength,187+app.xLength*2,300-app.yLength,fill ='white')
        canvas.create_text(187,300, text=f'{app.playerPokemon.getMoves(3).getMoveName()}',fill='black', font='Helvetica 10')
        #move4
        canvas.create_rectangle(483-app.xLength*2 ,300 + app.yLength,483+app.xLength*2,300-app.yLength,fill ='white')
        canvas.create_text(483,300, text=f'{app.playerPokemon.getMoves(0).getMoveName()}',fill='black', font='Helvetica 10')
    elif (app.text == True):
        pass

def combat_mousePressed(app,event):
    print(event.x)
    print(event.y)
    if (app.battle == False):
        if (187 - app.xLength*2 <= event.x <= 187 + app.xLength*2 and (300 - app.yLength) <= event.y <= (300 + app.yLength)):
            #Top Left
            app.battle = True
            pass
        elif (187 - app.xLength*2 <= event.x <= 187 + app.xLength*2 and (352 - app.yLength) <= event.y <= (352 + app.yLength)):
            #bottom Left
            app.mode = 'bag'
            pass
        elif (483 - app.xLength*2 <= event.x <= 483 + app.xLength*2 and (300 - app.yLength) <= event.y <= (300 + app.yLength)):
            #Top Right
            app.mode = 'Pokemon'
            pass
        elif (483 - app.xLength*2 <= event.x <= 483 + app.xLength*2 and (352 - app.yLength) <= event.y <= (352 + app.yLength)):
            #bottom right
            app.mode = 'game'
    else:
        if (187 - app.xLength*2 <= event.x <= 187 + app.xLength*2 and (300 - app.yLength) <= event.y <= (300 + app.yLength)):
            #Top Left
            app.enemyPokemon.takeDmg(app.playerPokemon.getMoves(2).getDmg())
            enemyPokemonAttacks(app)
            print(f'{app.enemyPokemon.getName()} deals {app.enemyPokemon.getMoves(2).getDmg()} enemy has {app.playerPokemon.getHealth()} heath left')
            print(f'Enemy {app.playerPokemon.getName()} deals {app.playerPokemon.getMoves(2).getDmg()} enemy has {app.enemyPokemon.getHealth()} heath left')

        elif (187 - app.xLength*2 <= event.x <= 187 + app.xLength*2 and (352 - app.yLength) <= event.y <= (352 + app.yLength)):
            #bottom Left
            app.enemyPokemon.takeDmg(app.playerPokemon.getMoves(1).getDmg())
            enemyPokemonAttacks(app)
            print(f'{app.enemyPokemon.getName()} deals {app.enemyPokemon.getMoves(1).getDmg()} enemy has {app.playerPokemon.getHealth()} heath left')
            print(f'Enemy {app.playerPokemon.getName()} deals {app.playerPokemon.getMoves(1).getDmg()} enemy has {app.enemyPokemon.getHealth()} heath left')
        elif (483 - app.xLength*2 <= event.x <= 483 + app.xLength*2 and (300 - app.yLength) <= event.y <= (300 + app.yLength)):
            #Top Right
            print(app.playerPokemon.getMoves(3).getDmg())
            app.enemyPokemon.takeDmg(app.playerPokemon.getMoves(3).getDmg())
            enemyPokemonAttacks(app)
            print(f'{app.enemyPokemon.getName()} deals {app.enemyPokemon.getMoves(3).getDmg()} enemy has {app.playerPokemon.getHealth()} heath left')
            print(f'Enemy {app.playerPokemon.getName()} deals {app.playerPokemon.getMoves(3).getDmg()} enemy has {app.enemyPokemon.getHealth()} heath left')
        elif (483 - app.xLength*2 <= event.x <= 483 + app.xLength*2 and (352 - app.yLength) <= event.y <= (352 + app.yLength)):
            #bottom right
            app.enemyPokemon.takeDmg(app.playerPokemon.getMoves(0).getDmg())
            enemyPokemonAttacks(app)
            print(f'{app.playerPokemon.getName()} deals {app.playerPokemon.getMoves(0).getDmg()} enemy has {app.enemyPokemon.getHealth()} heath left')
            print(f'Enemy {app.enemyPokemon.getName()} deals {app.enemyPokemon.getMoves(0).getDmg()} enemy has {app.playerPokemon.getHealth()} heath left')

def combat_timerFired(app):
    if (app.enemyPokemon.getHealth() <= 0 or app.playerPokemon.getHealth() <= 0):
        #something about the game being over message
        app.battle = False
        app.mode = 'game'

def combat_keyPressed(app,event):
    if event.key == 'Escape':
        app.battle = False
# ========================================================================

# General Functions

def encounterPokemon(app):
    chance = random.randrange(1,100)
    if (chance <= 54):
        app.mode = 'combat'
        newPokemon(app,5,10)

def newPokemon(app,levelMin,levelMax):
    randLevel = random.randint(75,100)
    randEmenyPokemon = random.randint(0,len(app.pokemonSprites)-1)
    randomPokemonIndex = random.randint(0,len(app.name)-1)
    randLevel2 = random.randint(75,100) #this should eventually be a set value
    for i in app.moveName:
        copyMove = []
        for j in range(len(i)):
            copyMove.append(Moves(30 * (j+1),i[j],1))
        app.moves.append(copyMove)
    enemyPokemon = Pokemon(app.type[randEmenyPokemon],app.name[randEmenyPokemon],randLevel,app.pokemonImages[randEmenyPokemon],app.moves[randEmenyPokemon])
    ourPokemon = Pokemon(app.type[randomPokemonIndex],app.name[randomPokemonIndex],randLevel2,app.backPokemonImages[randomPokemonIndex],app.moves[randomPokemonIndex])
    enemyCopyMoves = []
    for i in enemyPokemon.getAllMoves():
        enemyCopyMoves.append(Moves(i.getDmg(),i.getMoveName(),enemyPokemon.getLevel()))
    enemyPokemon.setMoves(enemyCopyMoves)
    copyMoves = []
    for i in ourPokemon.getAllMoves():
        copyMoves.append(Moves(i.getDmg(),i.getMoveName(),ourPokemon.getLevel()))
    ourPokemon.setMoves(copyMoves)
    app.enemyPokemon = enemyPokemon
    app.playerPokemon = ourPokemon


#enemy Pokemon should be doing the maximum dmg at all times
def enemyPokemonAttacks(app):
    damage = enemyPokemonMaxDmg(app)
    app.playerPokemon.takeDmg(damage)

def enemyPokemonMaxDmg(app):
    maxDmg = 0
    for i in range(len(app.enemyPokemon.getAllMoves())):
        if (app.enemyPokemon.getMoves(i).getDmg() >= maxDmg):
            maxDmg = app.enemyPokemon.getMoves(i).getDmg()
    print(f'{maxDmg} this is being returned')
    return maxDmg
    

# ========================================================================
#Spritesheet is taken https://www.deviantart.com/mohammadataya/art/Pokemon-Trainer-Calem-By-Tedbited15-Updated-397076725
#pikachus are from https://www.deviantart.com/koreyriera/art/Pikachu-Custom-Front-And-Back-Sprite-776102670
def appStarted(app):
    app.mode = 'startScreen'
    app.yLength = 20
    app.xLength = 50
    app.battle = False
    app.player = Player(0,0)
    app.playerPokemon = None
    app.startScreenImg = app.loadImage('img/pokemonImg.jpg')
    app.startScreenImg2 = app.scaleImage(app.startScreenImg, 4/7)
    app.background = app.loadImage('img/pokemonTestBackground.png')
    app.bagImg = app.loadImage('img/bag.jpg')
    app.selectionImg = app.loadImage('img/selection.png')
    app.combatScreen = app.loadImage('img/combat.png')
    app.pokemonSprites = ['img/pikachu.png','img/bulbasaur.png','img/charmander.png','img/squritle.png']
    app.backSprites = ['img/backPikachu.png','img/backBulbasaur.png','img/backCharmander.png','img/backSquirtle.png']
    app.pokemonImageUnscaled = []
    app.pokemonImages = []
    app.backPokemon = []
    app.backPokemonImages = []
    for i in range(len(app.pokemonSprites)):
        pokemon = app.loadImage(app.pokemonSprites[i]) 
        app.pokemonImageUnscaled.append(pokemon)
    for i in range(len(app.pokemonSprites)):
        pokemon = app.loadImage(app.backSprites[i]) 
        app.backPokemon.append(pokemon)
    for i in range(len(app.pokemonImageUnscaled)):
        pokemons = app.scaleImage(app.pokemonImageUnscaled[i], 1/3)
        app.pokemonImages.append(pokemons)
    for i in range(len(app.backPokemon)):
        pokemons = app.scaleImage(app.backPokemon[i], 1/3)
        app.backPokemonImages.append(pokemons)
    app.sprite = app.loadImage('img/player.png') 
    app.type = ['electric','grass','fire','water']
    app.name = ['pikachu','bulbasaur','charmander','squritle']
    app.moveName = [['Thunderbolt','Tackle','Scratch','Leer'],
                ['Vine Whip','Tackle','Scratch','Leer'],
                ['Ember','Tackle','Scratch','Leer'],
                ['Water Gun','Tackle','Scratch','Leer'],
    ]
    app.moves = []
    app.enemyPokemon = None
    # app.sprites = [ ]
    # for i in range(4):
    #     for j in range(4):
    #         sprite = sprite.crop((30+160*j, 30+160*i, 230+160*j, 250+160*i))
    #         app.sprites.append(sprite)
    # app.spriteCounter = 0

runApp(width=700, height=400)
