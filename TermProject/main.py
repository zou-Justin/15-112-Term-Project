#Justin Zou (justinzo)
#Pokemon
from cmu_112_graphics import *
from pokemon import *
from person import *
import random

#images were taken from pokemon game screenshots
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
    canvas.create_image(app.width/2,app.height/2,image=ImageTk.PhotoImage(app.background))
    #sprite
    newSprite = app.Sprites[app.spriteCounter]
    canvas.create_image(app.width/2 + app.player.getX(), app.height/2 + app.player.getY(), image=ImageTk.PhotoImage(newSprite))
    for i in range(len(app.terrain)):
        for j in range(len(app.terrain[0])):
            # app.terrain[i][j] = (i*30,j*30)
            canvas.create_image(i*30,j*30,image=ImageTk.PhotoImage(app.grass))
    for i in range(len(app.player.getPokemon())):
        app.player.getPokemonIndex(i).setHealthMax()

def game_keyPressed(app,event):
    if (event.key == "Left"):
        app.player.moveLeft()
        app.spriteCounter = ((1 + app.spriteCounter) % 3) +6
        encounterPokemon(app)
    elif (event.key ==  "Right"):
        app.player.moveRight()
        app.spriteCounter = ((1 + app.spriteCounter) % 3) +3
        encounterPokemon(app)
    elif (event.key == 'Up'):
        app.player.moveUp()
        app.spriteCounter = ((1 + app.spriteCounter) % 3) +9
        encounterPokemon(app)
    elif (event.key == "Down"):
        app.player.moveDown()
        app.spriteCounter = ((1 + app.spriteCounter) % 3)
        encounterPokemon(app)

# ========================================================================

#Bag Screen

def bag_redrawAll(app,canvas):
    canvas.create_image(app.width/2,app.height/2,image=ImageTk.PhotoImage(app.bagImg))
    canvas.create_text(480,62, text=f'Throw a pokeball',fill='black', font='Helvetica 10')

def bag_mousePressed(app,event):
    print(event.x,event.y)
    if (91 - app.xLength*2 <= event.x <= 91 + app.xLength*2 and (311 - app.yLength) <= event.y <= (311 + app.yLength)):
        app.mode = 'combat'
    if (480 - app.xLength*2 <= event.x <= 480 + app.xLength*2 and (62 - app.yLength) <= event.y <= (62 + app.yLength)):
        app.battle = False
        app.mode = 'game'
        # app.enemyPokemon.setSprite(app.imageDictionary[app.enemyPokemon.getSprite()])
        app.player.catchPokemon(app.enemyPokemon)

# ========================================================================

#Pokemon Screen

def Pokemon_redrawAll(app,canvas):
    canvas.create_image(app.width/2,app.height/2,image=ImageTk.PhotoImage(app.selectionImg))
    for i in range(0,len(app.player.getPokemon())):
        if i % 2 == 0:
            if (i == 0):
                canvas.create_image(131,29,image=ImageTk.PhotoImage(app.player.getPokemon()[i].getSprite()))
                canvas.create_text(293,36,text=f'Lv: {app.player.getPokemon()[i].getLevel()}',fill='black', font='Helvetica 10')
                canvas.create_text(215,33,text=f'{app.player.getPokemon()[i].getName()}',fill='black', font='Helvetica 10')
            elif (i == 2):
                canvas.create_image(131,129,image=ImageTk.PhotoImage(app.player.getPokemon()[i].getSprite()))
                canvas.create_text(293,136,text=f'Lv: {app.player.getPokemon()[i].getLevel()}',fill='black', font='Helvetica 10')
                canvas.create_text(215,133,text=f'{app.player.getPokemon()[i].getName()}',fill='black', font='Helvetica 10')
            elif (i == 4):
                canvas.create_image(131,229,image=ImageTk.PhotoImage(app.player.getPokemon()[i].getSprite()))
                canvas.create_text(293,236,text=f'Lv: {app.player.getPokemon()[i].getLevel()}',fill='black', font='Helvetica 10')
                canvas.create_text(215,233,text=f'{app.player.getPokemon()[i].getName()}',fill='black', font='Helvetica 10')
        elif i % 2 == 1:
            if (i == 1):
                canvas.create_image(380,43,image=ImageTk.PhotoImage(app.player.getPokemon()[i].getSprite()))
                canvas.create_text(539,50,text=f'Lv: {app.player.getPokemon()[i].getLevel()}',fill='black', font='Helvetica 10')
                canvas.create_text(450,47,text=f'{app.player.getPokemon()[i].getName()}',fill='black', font='Helvetica 10')
            elif (i == 3):
                canvas.create_image(380,143,image=ImageTk.PhotoImage(app.player.getPokemon()[i].getSprite()))
                canvas.create_text(539,150,text=f'Lv: {app.player.getPokemon()[i].getLevel()}',fill='black', font='Helvetica 10')
                canvas.create_text(450,147,text=f'{app.player.getPokemon()[i].getName()}',fill='black', font='Helvetica 10')
            elif (i == 5):
                canvas.create_image(380,243,image=ImageTk.PhotoImage(app.player.getPokemon()[i].getSprite()))
                canvas.create_text(539,250,text=f'Lv: {app.player.getPokemon()[i].getLevel()}',fill='black', font='Helvetica 10')
                canvas.create_text(450,247,text=f'{app.player.getPokemon()[i].getName()}',fill='black', font='Helvetica 10')

def Pokemon_mousePressed(app,event):
    print(event.x,event.y)
    if (545 - app.xLength*2 <= event.x <= 545 + app.xLength*2 and (365 - app.yLength) <= event.y <= (365 + app.yLength)):
        app.mode = 'combat'
    elif (201 - app.xLength*2 <= event.x <= 201 + app.xLength*2 and (57 - app.yLength) <= event.y <= (57 + app.yLength)):
        switchPokemon(app,0)
        app.mode = 'combat'
    elif (468 - app.xLength*2 <= event.x <= 468 + app.xLength*2 and (61 - app.yLength) <= event.y <= (61 + app.yLength)):
        switchPokemon(app,1)
        app.mode = 'combat'
    elif (215 - app.xLength*2 <= event.x <= 215 + app.xLength*2 and (148 - app.yLength) <= event.y <= (148 + app.yLength)):
        switchPokemon(app,2)
        app.mode = 'combat'
    elif (491 - app.xLength*2 <= event.x <= 491 + app.xLength*2 and (166 - app.yLength) <= event.y <= (166 + app.yLength)):
        switchPokemon(app,3)
        app.mode = 'combat'
    elif (214 - app.xLength*2 <= event.x <= 214 + app.xLength*2 and (257 - app.yLength) <= event.y <= (257 + app.yLength)):
        switchPokemon(app,4)
        app.mode = 'combat'
    elif (482 - app.xLength*2 <= event.x <= 482 + app.xLength*2 and (274 - app.yLength) <= event.y <= (274 + app.yLength)):
        switchPokemon(app,5)
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
        canvas.create_text(187,352, text=f'Bag',fill='black', font='Helvetica 10')
        #run
        canvas.create_rectangle(483-app.xLength*2 ,352 + app.yLength,483+app.xLength*2,352-app.yLength,fill ='white')
        canvas.create_text(483,352, text=f'Run',fill='black', font='Helvetica 10')  
        #fight
        canvas.create_rectangle(187-app.xLength*2 ,300 + app.yLength,187+app.xLength*2,300-app.yLength,fill ='white')
        canvas.create_text(187,300, text=f'Fight',fill='black', font='Helvetica 10')
        #bag
        canvas.create_rectangle(483-app.xLength*2 ,300 + app.yLength,483+app.xLength*2,300-app.yLength,fill ='white')
        canvas.create_text(483,300, text=f'Pokemon',fill='black', font='Helvetica 10')
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
def switchPokemon(app,index):
    app.playerPokemon = app.player.getPokemonIndex(index)

def encounterPokemon(app):
    # if (app.player.getX() <= )
    chance = random.randrange(1,100)
    print(chance)
    if (chance <= 4):
        app.mode = 'combat'
        newPokemon(app,5,10)

def newPokemon(app,levelMin,levelMax):
    randLevel = random.randint(75,100)
    randEmenyPokemon = random.randint(0,len(app.pokemonSprites)-1)
    enemyPokemon = Pokemon(app.type[randEmenyPokemon],app.name[randEmenyPokemon],randLevel,app.pokemonImages[randEmenyPokemon],app.moves[randEmenyPokemon])
    enemyCopyMoves = []
    for i in enemyPokemon.getAllMoves():
        enemyCopyMoves.append(Moves(i.getDmg(),i.getMoveName(),enemyPokemon.getLevel()))
    enemyPokemon.setMoves(enemyCopyMoves)
    app.enemyPokemon = enemyPokemon

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
#sidescrolling is from Animations Part 4 notes
def appStarted(app):
    #variables
    app.mode = 'startScreen'
    app.scrollX = 0
    app.yLength = 20
    app.xLength = 50
    app.battle = False
    app.player = Player(0,0)
    app.text = False
    app.playerPokemon = None
    app.startScreenImg = app.loadImage('img/pokemonImg.jpg')
    app.startScreenImg2 = app.scaleImage(app.startScreenImg, 4/7)
    app.background = app.loadImage('img/pokemonTestBackground.png')
    app.grass = app.loadImage('img/grass.png')
    app.bagImg = app.loadImage('img/bag.jpg')
    app.selectionImg = app.loadImage('img/selection.png')
    app.combatScreen = app.loadImage('img/combat.png')
    app.pokemonSprites = ['img/pikachu.png','img/bulbasaur.png','img/charmander.png','img/squritle.png']
    app.backSprites = ['img/backPikachu.png','img/backBulbasaur.png','img/backCharmander.png','img/backSquirtle.png']
    app.imageDictionary = {}
    app.pokemonImageUnscaled = []
    app.pokemonImages = []
    app.backPokemon = []
    app.backPokemonImages = []
    #terrain
    app.terrain = [[1] * 5 for i in range(4)]
    #load in sprites
    for i in range(len(app.pokemonSprites)):
        img = app.loadImage(app.pokemonSprites[i]) 
        app.pokemonImageUnscaled.append(img)
    for i in range(len(app.pokemonSprites)):
        img = app.loadImage(app.backSprites[i]) 
        app.backPokemon.append(img)
    for i in range(len(app.pokemonImageUnscaled)):
        img = app.scaleImage(app.pokemonImageUnscaled[i], 1/3)
        app.pokemonImages.append(img)
    for i in range(len(app.backPokemon)):
        img = app.scaleImage(app.backPokemon[i], 1/3)
        app.backPokemonImages.append(img)
    for i in app.pokemonSprites:
        for j in app.backSprites:
            app.imageDictionary[i] = j
    app.sprite = app.loadImage('img/player.png') 
    app.type = ['electric','grass','fire','water']
    app.name = ['pikachu','bulbasaur','charmander','squritle']
    app.moveName = [['Thunderbolt','Tackle','Scratch','Leer'],
                ['Vine Whip','Tackle','Scratch','Leer'],
                ['Ember','Tackle','Scratch','Leer'],
                ['Water Gun','Tackle','Scratch','Leer'],
    ]
    #Some animation involving moves
    app.moves = []
    for i in app.moveName:
        copyMove = []
        for j in range(len(i)):
            copyMove.append(Moves(30 * (j+1),i[j],1))
        app.moves.append(copyMove)
    app.enemyPokemon = None
    app.Move1 = False
    app.Move2 = False
    app.Move3 = False
    app.Move4 = False
    #create your pokemon
    randomPokemonIndex = random.randint(0,len(app.name)-1)
    randLevel2 = random.randint(75,100) #this should eventually be a set value
    ourPokemon = Pokemon(app.type[randomPokemonIndex],app.name[randomPokemonIndex],randLevel2,app.backPokemonImages[randomPokemonIndex],app.moves[randomPokemonIndex])
    copyMoves = []
    for i in ourPokemon.getAllMoves():
        copyMoves.append(Moves(i.getDmg(),i.getMoveName(),ourPokemon.getLevel()))
    ourPokemon.setMoves(copyMoves)
    app.playerPokemon = ourPokemon
    app.player.catchPokemon(app.playerPokemon)
   
    #animations for player
    movement = app.loadImage('img/MoveRight.png')
    app.Sprites = []
    for i in range(12):
        sprite = movement.crop((0 + 32*i, 0, 32+32*i, 30))
        app.Sprites.append(sprite)
    app.spriteCounter = 0

runApp(width=700, height=400)
