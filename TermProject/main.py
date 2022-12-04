#Justin Zou (justinzo)
#Pokemon
from cmu_112_graphics import *
from pokemon import *
from person import *
import random

#images were taken from pokemon game screenshots
# image taken of Route 117 remake by Mucrush https://www.pinterest.com/pin/route-117-remake-by-pokemondiamonddeviantartcom-on-deviantart--133982157648104288/
'''
Relaistically need types
need speed stat
'''
# Start Screen
# gif code from cmu-112 website
def startScreen_redrawAll(app,canvas):
    canvas.create_image(app.width/2,app.height/2, image=ImageTk.PhotoImage(app.startScreenImg2))
    canvas.create_text(app.width/2,app.height-app.width/12, text=f'Press Enter to Start',
                                            fill='black', font='Helvetica 10')
def startScreen_keyPressed(app,event):
    if (event.key == "Enter"):
        app.mode = 'game'
# ========================================================================

# Game Screen
def game_redrawAll(app,canvas):
    x = app.width/2 - app.scrollX 
    y = app.height/2
    canvas.create_image(x,y,image=ImageTk.PhotoImage(app.background))
    if (app.nextImage):
        canvas.create_image(x,y,image=ImageTk.PhotoImage(app.background2))
    #sprite
    newSprite = app.Sprites[app.spriteCounter]
    for i in range(len(app.terrain)):
        for j in range(len(app.terrain[0])):
            newX = app.xScale + i*30 - app.scrollX
            newY = 100 + j *30
            canvas.create_image(newX,newY,image=ImageTk.PhotoImage(app.grass))
    for i in range(len(app.player.getPokemon())):
        app.player.getPokemonIndex(i).setHealthMax()
    if (app.finalRoom):
            canvas.create_image(x,y,image=ImageTk.PhotoImage(app.finalBackground))
            canvas.create_image(100- app.scrollX ,100,image = ImageTk.PhotoImage(app.trainerSprite))
    canvas.create_image(60, 90 + app.player.getY(), image=ImageTk.PhotoImage(newSprite))

def inTerrain(app):
    if app.xScale <= app.player.getX() <= app.xScale +((len(app.terrain)-1) *30)and \
        60  <= app.player.getY() <= 60 + ((len(app.terrain[0])-1) * 30):
        app.inGrass = True
    else:
        app.inGrass = False
        

def game_keyPressed(app,event):
    if (app.nextImage):
        if (app.scrollX >= -530):
            if (event.key == "Left"):
                app.player.moveLeft()
                app.scrollX -= 15
                app.spriteCounter = ((1 + app.spriteCounter) % 3) +6
                if(app.inGrass):
                    encounterPokemon(app)
    else:
        if (app.scrollX >= -420):
            if (event.key == "Left"):
                app.player.moveLeft()
                app.scrollX -= 15
                app.spriteCounter = ((1 + app.spriteCounter) % 3) +6
                if(app.inGrass):
                    encounterPokemon(app)
    if (event.key ==  "Right"):
        app.player.moveRight()
        app.scrollX += 15
        app.spriteCounter = ((1 + app.spriteCounter) % 3) +3
        if(app.inGrass):
            encounterPokemon(app)
    if (event.key == 'Up'):
        app.player.moveUp()
        app.spriteCounter = ((1 + app.spriteCounter) % 3) +9
        if(app.inGrass):
            encounterPokemon(app)
    elif (event.key == "Down"):
        app.player.moveDown()
        app.spriteCounter = ((1 + app.spriteCounter) % 3)
        if(app.inGrass):
            encounterPokemon(app)

def game_timerFired(app):
    print(app.player.getX(),app.player.getY())
    print(app.enemyTrainer.getX(),app.enemyTrainer.getY())
    # print(app.inGrass)
    if (app.finalRoom):
        if (inBound(app.player.getX(),app.player.getY(),app.enemyTrainer.getX(),app.enemyTrainer.getY())):
            trainerAI(app)
    if (app.nextImage):
        app.xScale = 300
        app.grass = app.loadImage('img/rock.png')
    inTerrain(app)
    if (240 >= app.scrollX >= 140):
        app.terrain = [[1] * 5 for i in range(4)]
        app.xScale = 300
    elif (340< app.scrollX <= 440):
        app.terrain = [[1] * app.randomRow for i in range(app.randomCol)]
        app.xScale = 600
    if (app.scrollX >= 880 and app.nextImage):
        app.finalRoom = True
        app.nextImage = False
        app.scrollX = 30
        app.player.setX(60)
        app.player.setY(90)
    elif (app.scrollX >= 880):
        app.nextImage = True
        app.scrollX = 0
        app.player.setX(60)
        app.player.setY(90)
    

def inBound(x1,y1,x2,y2):
    if ((((x2-x1) ** 2) + ((y2-y1) **2))**(1/2)) <= 20:
       return True
    return False

    # if (300 <= app.player.getX() <= 370 and 100 <= app.player.getY() <= 200):
    #     app.inGrass = True
    # else:
    #     app.inGrass = False
    

# ========================================================================

#Bag Screen

def bag_redrawAll(app,canvas):
    canvas.create_image(app.width/2,app.height/2,image=ImageTk.PhotoImage(app.bagImg))
    canvas.create_image(377,70,image=ImageTk.PhotoImage(app.pokeball))
    canvas.create_text(485,75, text=f'Throw a pokeball',fill='black', font='Helvetica 15')

def bag_mousePressed(app,event):
    print(event.x,event.y)
    if (91 - app.xLength*2 <= event.x <= 91 + app.xLength*2 and (311 - app.yLength) <= event.y <= (311 + app.yLength)):
        app.mode = 'combat'
    if (app.inTrainerBattle == False):
        if (485 - app.xLength*2 <= event.x <= 485 + app.xLength*2 and (75 - app.yLength) <= event.y <= (75 + app.yLength)):
            app.battle = False
            app.catching = True
            app.mode = 'combat'
            app.enemyPokemon.setSprite(app.enemyBackSprite)
            app.player.catchPokemon(app.enemyPokemon)
    else:
        app.mode = 'combat'

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
    canvas.create_image(app.width/2 - 140, app.height/2 +20, image=ImageTk.PhotoImage(app.playerPokemon.getSprite()))
    if (app.catching == False):
        canvas.create_image(app.width/2 + 140, app.height/2 -80, image=ImageTk.PhotoImage(app.enemyPokemon.getSprite()))
    canvas.create_text(140,70, text=f'{app.enemyPokemon.getName()}',fill='black', font='Helvetica 10')
    canvas.create_text(430,205, text=f'{app.playerPokemon.getName()}',fill='black', font='Helvetica 10')
    canvas.create_text(159,96, text=f'{app.enemyPokemon.getHealth()} / {app.enemyPokemon.getMaxHealth()}',fill='black', font='Helvetica 10')
    canvas.create_text(525,245, text=f'{app.playerPokemon.getHealth()} / {app.playerPokemon.getMaxHealth()}',fill='black', font='Helvetica 10')
    canvas.create_text(291,71, text=f'Lv: {app.enemyPokemon.getLevel()}',fill='black', font='Helvetica 10')
    canvas.create_text(569,205, text=f'Lv: {app.playerPokemon.getLevel()}',fill='black', font='Helvetica 10')
    if (app.catching == True):
        if(app.time >20):
            canvas.create_text(331,326, text=f'Caught!',fill='black', font='Helvetica 10')
        else:
            canvas.create_text(331,326, text=f'Catching Pokemon',fill='black', font='Helvetica 10')  
            canvas.create_image(app.width/2 + 140, app.height/2 -80, image=ImageTk.PhotoImage(app.pokeball))
    elif (app.Move0 == True):
        canvas.create_text(331,316, text=f'Enemy {app.enemyPokemon.getName()} deals {enemyPokemonAttacksNoDmg(app.moveIndex,app.moveLists)[1]}',fill='black', font='Helvetica 10')
        canvas.create_text(331,336, text=f'Your {app.playerPokemon.getName()} deals {app.playerPokemon.getMoves(0).getDmg()}',fill='black', font='Helvetica 10')
    elif (app.Move1 == True):
        canvas.create_text(331,316, text=f'Enemy {app.enemyPokemon.getName()} deals {enemyPokemonAttacksNoDmg(app.moveIndex,app.moveLists)[1]}',fill='black', font='Helvetica 10')
        canvas.create_text(331,336, text=f'Your {app.playerPokemon.getName()} deals {app.playerPokemon.getMoves(1).getDmg()}',fill='black', font='Helvetica 10')
    elif (app.Move2 == True):
        canvas.create_text(331,316, text=f'Enemy {app.enemyPokemon.getName()} deals {enemyPokemonAttacksNoDmg(app.moveIndex,app.moveLists)[1]}',fill='black', font='Helvetica 10')
        canvas.create_text(331,336, text=f'Your {app.playerPokemon.getName()} deals {app.playerPokemon.getMoves(2).getDmg()}',fill='black', font='Helvetica 10')
    elif (app.Move3 == True):
        canvas.create_text(331,316, text=f'Enemy {app.enemyPokemon.getName()} deals {enemyPokemonAttacksNoDmg(app.moveIndex,app.moveLists)[1]}',fill='black', font='Helvetica 10')
        canvas.create_text(331,336, text=f'Your {app.playerPokemon.getName()} deals {app.playerPokemon.getMoves(3).getDmg()}',fill='black', font='Helvetica 10')
    elif (app.battle == False):
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
        canvas.create_text(187,352, text=f'{app.playerPokemon.getMoves(1).getMoveName()}',fill='black', font='Helvetica 10')
        #move2
        canvas.create_rectangle(483-app.xLength*2 ,352 + app.yLength,483+app.xLength*2,352-app.yLength,fill ='white')
        canvas.create_text(483,352, text=f'{app.playerPokemon.getMoves(0).getMoveName()}',fill='black', font='Helvetica 10')
        #move3
        canvas.create_rectangle(187-app.xLength*2 ,300 + app.yLength,187+app.xLength*2,300-app.yLength,fill ='white')
        canvas.create_text(187,300, text=f'{app.playerPokemon.getMoves(2).getMoveName()}',fill='black', font='Helvetica 10')
        #move4
        canvas.create_rectangle(483-app.xLength*2 ,300 + app.yLength,483+app.xLength*2,300-app.yLength,fill ='white')
        canvas.create_text(483,300, text=f'{app.playerPokemon.getMoves(3).getMoveName()}',fill='black', font='Helvetica 10')



def combat_mousePressed(app,event):
    # print(event.x)
    # print(event.y)
    if (app.catching == True):
        app.mode = 'game'
        app.catching = False
        app.time = 0
    elif (app.battle == False):
        if (187 - app.xLength*2 <= event.x <= 187 + app.xLength*2 and (300 - app.yLength) <= event.y <= (300 + app.yLength)):
            #Top Left
            app.battle = True
        elif (187 - app.xLength*2 <= event.x <= 187 + app.xLength*2 and (352 - app.yLength) <= event.y <= (352 + app.yLength)):
            #bottom Left
            app.mode = 'bag'
        elif (483 - app.xLength*2 <= event.x <= 483 + app.xLength*2 and (300 - app.yLength) <= event.y <= (300 + app.yLength)):
            #Top Right
            app.mode = 'Pokemon'
        elif (483 - app.xLength*2 <= event.x <= 483 + app.xLength*2 and (352 - app.yLength) <= event.y <= (352 + app.yLength)):
            #bottom right
            if (app.inTrainerBattle == False):
                app.mode = 'game'
    else:
        if (app.Move0 == True or app.Move1 == True or app.Move2 == True or app.Move3 == True):
            app.Move0 = False
            app.Move3 = False
            app.Move2 = False
            app.Move1 = False
        elif (187 - app.xLength*2 <= event.x <= 187 + app.xLength*2 and (300 - app.yLength) <= event.y <= (300 + app.yLength)):
            #Top Left
            app.Move2 = True
            app.Move3 = False
            app.Move0 = False
            app.Move1 = False
            app.enemyPokemon.takeDmg(app.playerPokemon.getMoves(2).getDmg())
            enemyPokemonAttacks(app,app.moveIndex)
            app.moveIndex += 1
            # if (app.playerPokemon.getMoves(2).getSpeed() >= app.moveLists[app.moveIndex % len(app.moveLists)].getSpeed()):
            #     app.enemyPokemon.takeDmg(app.playerPokemon.getMoves(2).getDmg())
            #     enemyPokemonAttacks(app,app.moveIndex)
            #     app.moveIndex += 1
            # else:
            #     enemyPokemonAttacks(app,app.moveIndex)
            #     app.enemyPokemon.takeDmg(app.playerPokemon.getMoves(2).getDmg())
            #     app.moveIndex += 1
        elif (187 - app.xLength*2 <= event.x <= 187 + app.xLength*2 and (352 - app.yLength) <= event.y <= (352 + app.yLength)):
            #bottom Left
            app.Move1 = True
            app.Move3 = False
            app.Move2 = False
            app.Move0 = False
            app.enemyPokemon.takeDmg(app.playerPokemon.getMoves(2).getDmg())
            enemyPokemonAttacks(app,app.moveIndex)
            app.moveIndex += 1
            # if (app.playerPokemon.getMoves(1).getSpeed() >= app.moveLists[app.moveIndex % len(app.moveLists)].getSpeed()):
            #     app.enemyPokemon.takeDmg(app.playerPokemon.getMoves(1).getDmg())
            #     enemyPokemonAttacks(app,app.moveIndex)
            #     app.moveIndex += 1
            # else:
            #     enemyPokemonAttacks(app,app.moveIndex)
            #     app.enemyPokemon.takeDmg(app.playerPokemon.getMoves(1).getDmg())
            #     app.moveIndex += 1
        elif (483 - app.xLength*2 <= event.x <= 483 + app.xLength*2 and (300 - app.yLength) <= event.y <= (300 + app.yLength)):
            #Top Right
            app.Move3 = True
            app.Move2 = False
            app.Move0 = False
            app.Move1 = False
            app.enemyPokemon.takeDmg(app.playerPokemon.getMoves(2).getDmg())
            enemyPokemonAttacks(app,app.moveIndex)
            app.moveIndex += 1
        elif (483 - app.xLength*2 <= event.x <= 483 + app.xLength*2 and (352 - app.yLength) <= event.y <= (352 + app.yLength)):
            #bottom right
            app.Move0 = True
            app.Move3 = False
            app.Move2 = False
            app.Move1 = False
            app.enemyPokemon.takeDmg(app.playerPokemon.getMoves(2).getDmg())
            enemyPokemonAttacks(app,app.moveIndex)
            app.moveIndex += 1
            # if (app.playerPokemon.getMoves(0).getSpeed() >= app.moveLists[app.moveIndex % len(app.moveLists)].getSpeed()):
            #     app.enemyPokemon.takeDmg(app.playerPokemon.getMoves(0).getDmg())
            #     enemyPokemonAttacks(app,app.moveIndex % len(app.moveLists))
            #     app.moveIndex += 1
            # else:
            #     enemyPokemonAttacks(app,app.moveIndex % len(app.moveLists))
            #     app.enemyPokemon.takeDmg(app.playerPokemon.getMoves(0).getDmg())
            #     app.moveIndex += 1
            # enemyPokemonAttacks(app)
            
def combat_timerFired(app):
    if (app.inTrainerBattle):
        trainerAI(app)
    if (app.enemyPokemon.getHealth() <= 0 and app.inTrainerBattle == False):
        #something about the game being over message
        app.battle = False
        app.mode = 'game'
    if (app.inTrainerBattle and allPokemonDeadTrainer(app)):
        app.mode = 'winScreen'
    # elif (app.enemyPokemon.getHealth() <= 0 and app.inTrainerBattle == True):
    #     switchPokemonEnemy(app,app.enemyTrainer.getCurrentIndex()+1)
    #     app.enemyTrainer.increaseIndex()
    elif (app.playerPokemon.getHealth() <= 0 and allPokemonDead(app) and app.inTrainerBattle == True):
        app.mode = 'endScreen'
    elif (app.playerPokemon.getHealth() <= 0 and not allPokemonDead(app)):
        app.mode = 'Pokemon'
    if (app.catching):
        app.time = 1 + app.time
            
def combat_keyPressed(app,event):
    if event.key == 'Escape':
        app.battle = False
# ========================================================================

#endScreen
def endScreen_redrawAll(app,canvas):
    canvas.create_rectangle(0,0,app.width,app.height,fill='black')
    canvas.create_text(app.width/2,app.height/2, text=f' Game Over! Press R to restart the Game',fill='White', font='Helvetica 10')

#restarts the entire app
def endScreen_keyPressed(app,event):
    if (event.key == 'r'):
        appStarted(app)
# ========================================================================

#win Screen
def winScreen_redrawAll(app,canvas):
    canvas.create_rectangle(0,0,app.width,app.height,fill='white')
    canvas.create_text(app.width/2,app.height/2, text=f' You are the Champion! Congratulations!',fill='Black', font='Helvetica 10')





# General Functions

#checks if all of your pokemon are dead
def allPokemonDead(app):
    for i in app.player.getPokemon():
        if i.getHealth() > 0:
            return False
    return True

#checks if all of the trainer's pokemons are dead
def allPokemonDeadTrainer(app):
    for i in app.enemyTrainer.getPokemon():
        if i.getHealth() > 0:
            return False
    return True

#Switching to a new Pokemon
def switchPokemon(app,index):
    if (len(app.player.getPokemon()) > index):
        app.playerPokemon = app.player.getPokemonIndex(index)

#enemy pokemon switches out
def switchPokemonEnemy(app,index):
    index = index % 6
    app.enemyPokemon = app.enemyTrainer.getPokemonIndex(index)

#Chance to encounter a pokemon
def encounterPokemon(app):
    # if (app.player.getX() <= )
    chance = random.randrange(1,100)
    if (chance <= 18):
        app.mode = 'combat'
        newPokemon(app)

#creating a new pokemon to face
def newPokemon(app):
    randLevel = random.randint(75,100)
    randEmenyPokemon = random.randint(0,len(app.pokemonSprites)-1)
    enemyPokemon = Pokemon(app.pokemonToType[app.name[randEmenyPokemon]],app.name[randEmenyPokemon],randLevel,app.pokemonImages[randEmenyPokemon],app.moves[randEmenyPokemon])
    app.enemyBackSprite = app.backPokemonImages[randEmenyPokemon]
    enemyCopyMoves = []
    for i in enemyPokemon.getAllMoves():
        enemyCopyMoves.append(Moves(i.getDmg(),i.getMoveName(),enemyPokemon.getLevel()))
    for i in enemyCopyMoves:
        if i.getMoveName() in app.defensiveMoves:
            i.makeDefensive()
        elif i.getMoveName() in app.speedMoves:
            i.isFast(2)
    enemyPokemon.setMoves(enemyCopyMoves)
    app.enemyPokemon = enemyPokemon

#creating a bunch of new Pokemons for the trainer
def newPokemonTrainer(app):
    randLevel = random.randint(60,100)
    randEmenyPokemon = random.randint(0,len(app.pokemonSprites)-1)
    enemyPokemon = Pokemon(None,app.name[randEmenyPokemon],randLevel,app.pokemonImages[randEmenyPokemon],app.moves[randEmenyPokemon])
    enemyCopyMoves = []
    for i in enemyPokemon.getAllMoves():
        enemyCopyMoves.append(Moves(i.getDmg(),i.getMoveName(),enemyPokemon.getLevel()))
    for i in enemyCopyMoves:
        if i.getMoveName() in app.defensiveMoves:
            i.makeDefensive()
        elif i.getMoveName() in app.speedMoves:
            i.isFast(2)
    enemyPokemon.setMoves(enemyCopyMoves)
    return enemyPokemon

# trainer AI
def trainerPokemon(app):
    while(app.enemyTrainer.pokemonAmount() < 6):
        app.enemyTrainer.catchPokemon(newPokemonTrainer(app))

#switches the pokemon out when it is about to die
def trainerAI(app):
    app.mode = 'combat'
    app.inTrainerBattle = True
    # app.enemyTrainer.setCurrentIndex() 
    app.enemyPokemon = app.enemyTrainer.getCurrentPokemon() 
    if (app.enemyTrainer.getCurrentIndex() < 6):
        if (app.enemyPokemon.getHealth() <= ourPokemonMaxDmg(app)):
            switchPokemonEnemy(app,app.enemyTrainer.getCurrentIndex()+1)
            app.enemyTrainer.increaseIndex()
    else:
        switchPokemonEnemy(app,app.enemyTrainer.getCurrentIndex())
        if (app.enemyPokemon.getHealth()) <= 0:
            app.enemyTrainer.increaseIndex()


#just add in maze gen for complexity
# # looked at https://www.cs.cmu.edu/~112/notes/student-tp-guides/Mazes.pdf
# # looked at https://en.wikipedia.org/wiki/Maze_generation_algorithm#Randomized_depth-first_search
# def generateMaze(app):
#     L = [[0] * 6 for i in range(6)]
#     return generateMazeHelper(app,(0,0),L,[])

# def generateMazeHelper(app,cell,L,visitedL):
#     if (isSolution()):
#         return L

# def outOfBounds(index1,index2,L):
#     for i in L:
#         for j in L:
#             if ()


#enemy Pokemon should be doing the maximum dmg at all times
#Looked at AI TP https://www.cs.cmu.edu/~112/notes/student-tp-guides/GameAI.pdf
def enemyPokemonAttacks(app,index):
    app.moveLists = bestPossibleMove(app,app.playerPokemon.getHealth(),[])
    print(app.moveLists)
    index = index % len(app.moveLists)
    app.playerPokemon.takeDmg(app.moveLists[index][1])

def enemyPokemonAttacksNoDmg(index,moveLists):
    index = index % len(moveLists)
    return((moveLists[index][0],moveLists[index][1]))

#max damage that the pokemon can do
def enemyPokemonMaxDmg(app):
    maxDmg = 0
    index = 0
    for i in range(len(app.enemyPokemon.getAllMoves())):
        if (app.enemyPokemon.getMoves(i).getDmg() >= maxDmg):
            maxDmg = app.enemyPokemon.getMoves(i).getDmg()
            index = i
    return (maxDmg,index)
#max damage that our pokemon can do
def ourPokemonMaxDmg(app):
    maxDmg = 0
    for i in range(len(app.playerPokemon.getAllMoves())):
        if (app.playerPokemon.getMoves(i).getDmg() >= maxDmg):
            maxDmg = app.playerPokemon.getMoves(i).getDmg()
    return maxDmg

# gives the move with the most speed
def getSpeedMove(app):
    maxSpeed = 0
    index = 0
    for i in range(len(app.enemyPokemon.getAllMoves())):
        if (app.enemyPokemon.getMoves(i).getSpeed() >= maxSpeed):
            maxSpeed = app.enemyPokemon.getMoves(i).getSpeed()
            index = i
    return (maxSpeed,index)

#recursive backtracking that we learned in class to return a list of moves in best possible order
def bestPossibleMove(app,health,L):
    if (health <= 0):
        return L
    else:
        for i in app.enemyPokemon.getAllMoves():
            if (isBetterMove(i,getSpeedMove(app)[0],enemyPokemonMaxDmg(app)[0],health)):
                moveName = i.getMoveName()
                L.append((moveName,i.getDmg()))
                health -= i.getDmg()
                solution = bestPossibleMove(app,health,L)
                if (solution != None):
                    return solution
                L.pop((moveName,i.getDmg()))
                health += i.getDmg
        return None
    
def isBetterMove(move,speed,dmg,health):
    if (move.getSpeed() >= speed and move.getDmg() >= health) or (move.getDmg() >= dmg):
        return True
    else:
        return False
    
def createRandomMove(app):
    randomDefenseMove = app.defensiveMoves[random.randint(0,len(app.defensiveMoves)-1)]
    randomOffensiveNormalMoves = app.offensiveNormalMoves[random.randint(0,len(app.offensiveNormalMoves)-1)]
    randomSpecialMove = app.specialMove[random.randint(0,len(app.offensiveNormalMoves)-1)]
    randomSpeedMoves = app.speedMoves[random.randint(0,len(app.speedMoves)-1)]
    app.moves2.append(randomDefenseMove)
    app.moves2.append(randomOffensiveNormalMoves)
    app.moves2.append(randomSpeedMoves)
    app.moves2.append(randomSpecialMove)

# ========================================================================
#Spritesheet is taken https://www.deviantart.com/mohammadataya/art/Pokemon-Trainer-Calem-By-Tedbited15-Updated-397076725
#pikachus are from https://www.deviantart.com/koreyriera/art/Pikachu-Custom-Front-And-Back-Sprite-776102670
# Rest of the art are found from screnshots of the game
# Sidescrolling is from Animations Part 4 notes
def appStarted(app):
    #variables
    app.mode = 'startScreen'
    app.scrollX = -100
    app.scrollY = 0
    app.yLength = 20
    app.scrollX = 0
    app.xLength = 50
    app.battle = False
    app.player = Player(60,90)
    app.enemyTrainer = Player(100,10)
    app.inTrainerBattle = False
    app.inGrass =False
    app.nextImage = False
    app.randomRow = random.randint(1,7)
    app.randomCol = random.randint(1,6)
    app.finalRoom = False
    app.time = 0
    app.xScale = 300
    app.text = False
    app.playerPokemon = None
    app.trainerSprite = app.loadImage('img/trainer.png')
    app.startScreenImg = app.loadImage('img/pokemonImg.jpg')
    app.startScreenImg2 = app.scaleImage(app.startScreenImg, 4/7)
    app.background = app.loadImage('img/longRoad3.png')
    app.background = app.scaleImage(app.background, 4/3)
    app.background2 = app.loadImage('img/longRoad4.png')
    app.background2 = app.scaleImage(app.background2, 4/3)
    app.finalBackground = app.loadImage('img/championRoom.png')
    app.grass = app.loadImage('img/grass.png')
    app.bagImg = app.loadImage('img/bag.jpg')
    app.selectionImg = app.loadImage('img/selection.png')
    app.combatScreen = app.loadImage('img/combat.png')
    app.catching = False
    pokeball = app.loadImage('img/pokeball.png')
    app.pokeball = app.scaleImage(pokeball,1/3)
    app.enemyBackSprite = None
    app.pokemonSprites = ['img/pikachu.png','img/bulbasaur.png','img/charmander.png','img/squritle.png',
    'img/slaking.png','img/torchic.png','img/treeko.png','img/swellow.png','img/mudkip.png','img/machamp.png','img/salamence.png']
    app.backSprites = ['img/backPikachu.png','img/backBulbasaur.png','img/backCharmander.png','img/backSquirtle.png',
    'img/backSlaking.png','img/backTorchic.png','img/backTreeko.png','img/backSwellow.png','img/backMudkip.png','img/backMachamp.png','img/backSalamence.png']
    app.imageDictionary = {}
    app.pokemonImageUnscaled = []
    app.pokemonImages = []
    app.backPokemon = []
    app.backPokemonImages = []
    app.moveIndex = 0
    app.moveLists = []
    #terrain
    app.terrain = [[]]

    #load in sprites
    for i in range(len(app.pokemonSprites)):
        img = app.loadImage(app.pokemonSprites[i]) 
        app.pokemonImageUnscaled.append(img)
    for i in range(len(app.backSprites)):
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
    app.type = ['electric','grass','fire','water','normal','flying','fighting','dragon']
    app.typeToMove = {
        'electric':'Thunderbolt',
        'grass':'Vine Whip',
        'fire':'Flamethrower',
        'water':'Hydro Pump',
        'normal':'Pound',
        'flying':'Aerial Ace',
        'fighting':'Close Combat',
        'dragon':'Dragons Breath'
    }
    app.typeToWeakness = {
        'electric':'Thunderbolt',
        'grass':'fire',
        'fire':'water',
        'water':'grass',
        'normal':'fighting',
        'dragon':'dragon'
    }
    app.pokemonToType = {
        'Pikachu':'electric',
        'Bulbasaur':'grass',
        'Charmander':'fire',
        'Squritle':'water',
        'Slaking':'normal',
        'Torchic':'fire',
        'Treeko':'grass',
        'Swellow':'flying',
        'Mudkip':'water',
        "Machamp":'fighting',
        "Salamence":"dragon"
    }
    app.name = ['Pikachu','Bulbasaur','Charmander','Squritle','Slaking','Torchic','Treeko','Swellow','Mudkip','Machamp','Salamence']
    app.defensiveMoves = ['Leer','Growl']
    app.offensiveNormalMoves = ['Tackle','Scratch','Pound','Slam']
    app.specialMove = ['Flamethrower','Thunderbolt','Overgrowth','Hydro Pump','Dragons Breath','Aerial Ace','Close Combat','Body Slam']
    app.speedMoves = ['Quick Attack','Shadow Sneak','SuckerPunch']
    
    app.moveName = [['Leer','Tackle','Quick Attack','Thunderbolt'],
                ['Growl','Tackle','Quick Attack','Overgrowth'],
                ['Leer','Scratch','Quick Attack','Flamethrower'],
                ['Leer','Tackle','Quick Attack','Hydro Pump'],
                ['Leer','Pound','SuckerPunch','Thunderbolt'],
                ['Leer','Slam','Shadow Sneak','Body Slam'],
                ['Growl','Tackle','Quick Attack','Flamethrower'],
                ['Leer','Scratch','Quick Attack','Overgrowth'],
                ['Growl','Pound','SuckerPunch','Aerial Ace'],
                ['Leer','Scratch','Quick Attack','Hydro Pump'],
                ['Growl','Tackle','SuckerPunch','Close Combat'],
                ['Leer','Tackle','Quick Attack','Dragons Breath']
    ]
    app.moves = []
    app.moves2 = []
    createRandomMove(app)
    print(app.moves2)
    for i in app.moveName:
        copyMove = []
        for j in range(len(i)):
            copyMove.append(Moves(10 * j,i[j],1))
        app.moves.append(copyMove)
    
    newCopyMove = []
    for i in range(len(app.moves2)):
        newCopyMove.append(Moves(20 * i,app.moves2[i],1))
    app.moves2 = newCopyMove
    app.enemyPokemon = None
    #move texts
    app.Move0 = False
    app.Move1 = False
    app.Move2 = False
    app.Move3 = False
    #create your pokemon
    randomPokemonIndex = random.randint(0,len(app.pokemonSprites)-1)
    randLevel2 = random.randint(75,100) #this should eventually be a set value
    ourPokemon = Pokemon(app.pokemonToType[app.name[randomPokemonIndex]],app.name[randomPokemonIndex],randLevel2,app.backPokemonImages[randomPokemonIndex],app.moves2)
    copyMoves = []
    for i in ourPokemon.getAllMoves():
        copyMoves.append(Moves(i.getDmg(),i.getMoveName(),ourPokemon.getLevel()))
    for i in range(len(copyMoves)):
        if i == 0:
            copyMoves[i].makeDefensive()
        elif i == 2:
            copyMoves[i].isFast(2)
    ourPokemon.setMoves(copyMoves)
    app.playerPokemon = ourPokemon
    app.player.catchPokemon(app.playerPokemon)
    trainerPokemon(app)
   
    #animations for player; basic structure taken from 15-112 notes
    movement = app.loadImage('img/MoveRight.png')
    app.Sprites = []
    for i in range(12):
        sprite = movement.crop((0 + 32*i, 0, 32+32*i, 30))
        app.Sprites.append(sprite)
    app.spriteCounter = 0

runApp(width=700, height=400)
