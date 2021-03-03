#Import-----------------------------------------------------------------------
import tkinter as tk
import random
import os.path
from os import path 
#Windows----------------------------------------------------------------------
root = tk.Tk()
root.geometry("700x800")
frame = tk.Frame() 
frame.master.title("pros.nob")
canvas = tk.Canvas(frame)
#Constants--------------------------------------------------------------------

position=[]
positionplayer=[]
bg = tk.PhotoImage(file = "img/bg.png")
bg_win = canvas.create_image(350,400,image=bg)  
pl = tk.PhotoImage(file = "img/player.png")
player = canvas.create_image(350,650,image=pl)
coin_image = tk.PhotoImage(file = "img/coin.png")
coin = canvas.create_image(30,50,image=coin_image)
lf =tk.PhotoImage(file="img/life.png")
life = canvas.create_image(30,110 ,image=lf)
soundon =tk.PhotoImage(file="img/soundon.png")
canvas.create_image(650,50 ,image=soundon,tags="sound")
soundoff =tk.PhotoImage(file="img/soundoff.png")
life_image= tk.PhotoImage(file="img/life.png")
diamon_image= tk.PhotoImage(file="img/diamon.png")
boom_image= tk.PhotoImage(file="img/boom.png")

diamon = canvas.create_image(30,170,image=diamon_image)

pause = tk.PhotoImage(file="img/pause.png")
canvas.create_image(650,90,image=pause,tags="pause")
unpause = tk.PhotoImage(file="img/unpause.png")
over = tk.PhotoImage(file="img/overgame.png")
won = tk.PhotoImage(file="img/wongame.png")
WINDOW_WIDTH = 700
WINDOW_HEIGHT = 800
COIN_SIZE = LIFE_SIZE=BOOM_SIZE=DIAMON_SIZE=30  # height = with
SHOOT_SIZE = 20
soundX = 650
soundY = 50
pauseX = 650
pauseY = 90
#Variable--------------------------------------------- ------------------------
soundCondition = True
gameCondition = True
pauseCondition = True
startGame = True
allCoin =[]
allLife =[]
allDiamon =[]
allBoom =[]
allShoot=[]

shoot = tk.PhotoImage(file="img/shoot.png")

monster = tk.PhotoImage(file="img/monster.png")
canvas.create_image(130,50,image=monster)
canvas.create_image(350,50,image=monster)
canvas.create_image(580,50,image=monster)


coins = 0
lives = 3
diamons = 0
booms = 0
shoots = 0
canvas.create_text(30,85,fill = "white",font="Times 15 italic bold",text=str(coins),tags="inCreaseCoins")
canvas.create_text(30,140,fill = "white",font="Times 15 italic bold",text=str(lives),tags="de&in-CreaseLives")
canvas.create_text(30,200,fill = "white",font="Times 15 italic bold",text=str(diamons),tags="inCreaseDiamons")

# #Function---------------------------------------------------------------------

# Adding Elements--------------------------------------------------------------
def changePosition1():
    
    allShoot.append(canvas.create_image(130,80,image=shoot,tags="coin"))
    if gameCondition and pauseCondition:
        canvas.after(6000,lambda:changePosition1())


def changePosition2():
    
    allShoot.append(canvas.create_image(580,80,image=shoot,tags="coin"))
    if gameCondition and pauseCondition:
        canvas.after(6000,lambda:changePosition2())



def addShoot():
    global allShoot
    allShoot.append(canvas.create_image(350,80,image=shoot,tags="coin"))
    if gameCondition and pauseCondition:
        canvas.after(4000,lambda:addShoot())



def addLife():
    global allLife
    lifeX = random.randrange(100,600)
    allLife.append(canvas.create_image(lifeX,-20,image=life_image,tags="coin"))
    if gameCondition and pauseCondition: 
        canvas.after(30000,lambda:addLife())
    

def addDiamon():
    global allDiamon
    diamonX = random.randrange(100,600)
    allDiamon.append(canvas.create_image(diamonX,-20,image=diamon_image,tags="coin"))
    if gameCondition and pauseCondition:
        canvas.after(20000,lambda:addDiamon())
    

def addBoom():
    global allBoom
    boomX = random.randrange(100,600)
    allBoom.append(canvas.create_image(boomX,-20,image=boom_image,tags="coin"))
    if gameCondition and pauseCondition:
        canvas.after(2000,lambda:addBoom())
    

def addCoin():
    global allCoin
    coinX = random.randrange(100,600)
    allCoin.append(canvas.create_image(coinX,-20,image=coin_image,tags="coin"))
    if gameCondition and pauseCondition:
        canvas.after(300,lambda:addCoin())
        moveCoin()

# Removing Elements----------------------------------------------------------
def removeShoot(index):
    shootId = allShoot[index]
    canvas.delete(shootId)
    allShoot.pop(index)

def removeCoin(index):
    coinId = allCoin[index]
    canvas.delete(coinId)
    allCoin.pop(index)

def removeLife(index):
    lifeId = allLife[index]
    canvas.delete(lifeId)
    allLife.pop(index)

def removeDiamon(index):
    diamonId = allDiamon[index]
    canvas.delete(diamonId)
    allDiamon.pop(index)

def removeBoom(index):
    boomId = allBoom[index]
    canvas.delete(boomId)
    allBoom.pop(index)

# Finding the index of Elements to remove----------------------------

# regturn -1 if no coin at this position or the coin index if any coin
def findCoinIndexAt(posX, posY):
    for n in range (len( allCoin)):
        coordCoin = canvas.coords(allCoin[n])
        coinX = coordCoin[0]
        coinY = coordCoin[1]
        if coinX + 15 > posX-45 and coinX-15 < posX+45 and  coinY +15 > posY-45 and coinY -15  < posY +45:  
            return n
    return -1 # no coin found

def findLifeIndexAt(posX, posY):
    for n in range (len( allLife)): 
        coordLife = canvas.coords(allLife[n])
        lifeX = coordLife[0]
        lifeY = coordLife[1]
        if lifeX + 15 > posX-45 and lifeX-15 < posX+45 and  lifeY +15 > posY-45 and lifeY -15  < posY +45:
            return n
    return -1 # no life found

def findDiamonIndexAt(posX, posY):
    for n in range (len( allDiamon)):
        coordDiamon = canvas.coords(allDiamon[n])
        diamonX = coordDiamon[0]
        diamonY = coordDiamon[1]
        if diamonX + 15 > posX-45 and diamonX-15 < posX+45 and  diamonY +15 > posY-45 and diamonY -15  < posY +45:
            return n
    return -1 # no diamon found

def findBoomIndexAt(posX, posY):
    for n in range (len( allBoom)):
        coordBoom = canvas.coords(allBoom[n])
        boomX = coordBoom[0]
        boomY = coordBoom[1]
        if boomX + 15 > posX-45 and boomX-15 < posX+45 and  boomY +15 > posY-45 and boomY -15  < posY +45:
            return n
    return -1 # no diamon found
def findShootIndexAt(posX, posY):
    for n in range (len( allShoot)):
        coordShoot = canvas.coords(allShoot[n])
        shootX = coordShoot[0]
        shootY = coordShoot[1]
        if shootX + 10 > posX-45 and shootX-10 < posX+45 and  shootY +10 > posY-45 and shootY -10  < posY +45:
            return n
    return -1 # no diamon found

# Removing Elements----------------------------------------------------------------
def Sound(event):
    global soundCondition,soundX,soundY
    if (event.x >= soundX - 15 and event.x <= soundX + 15) and (event.y >= soundY - 15 and event.y <= soundY + 15)and soundCondition:
        canvas.delete("sound")
        canvas.create_image(650,50 ,image=soundoff,tags="sound")
        soundCondition = False
    elif (event.x >= soundX - 15 and event.x <= soundX + 15) and (event.y >= soundY - 15 and event.y <= soundY + 15)and not soundCondition:
        canvas.delete("sound")
        canvas.create_image(650,50 ,image=soundon,tags="sound")
        soundCondition = True
        

def Pause(event):
    global gameCondition,pauseCondition,pauseX,pauseY
    if (event.x >= pauseX - 15 and event.x <= pauseX + 15) and (event.y >= pauseY - 15 and event.y <= pauseY + 15)and pauseCondition:
        pauseCondition = False
        canvas.delete("pause")
        canvas.create_image(650,90 ,image=unpause,tags="pause")
    elif (event.x >= pauseX - 15 and event.x <= pauseX + 15) and (event.y >= pauseY - 15 and event.y <= pauseY + 15)and not pauseCondition:
        pauseCondition = True
        if gameCondition:
            moveCoin()
            canvas.after(200,lambda:addCoin())
            canvas.after(2000,lambda:addBoom())
            canvas.after(30000,lambda:addDiamon())
            canvas.after(50000,lambda:addLife())
        canvas.delete("pause")
        canvas.create_image(650,90 ,image=pause,tags="pause")
        pauseCondition = True
        
def moveCoin():
    global coins,lives,diamons,booms,gameCondition,shoots
    if gameCondition and pauseCondition:
        canvas.move("coin",0,20)

    # 1 - Remove the first coin if outside of the window-----------------------------------

    firstCoin = allCoin[0]
    coordsFirstCoin = canvas.coords(firstCoin)
    if coordsFirstCoin[1] > WINDOW_HEIGHT - COIN_SIZE:
            removeCoin(0)

    # 2 - If player is on a coin remove the coin----------------------------

    coinIndexAtPlayer = findCoinIndexAt(getPlayerX(), getPlayerY())
    if coinIndexAtPlayer != -1 :
        removeCoin(coinIndexAtPlayer)
        if gameCondition:
            coins +=30
            canvas.delete("inCreaseCoins")
            canvas.create_text(30,85,fill = "white",font="Times 15 italic bold",text=str(coins),tags="inCreaseCoins")
            
            if diamons == 3 and coins >= 1800:
                canvas.create_image(350,350,image=won)
                canvas.create_rectangle(200,470,500,520,fill= "white")
                canvas.create_text(350,500,fill = "darkblue",font="Times 20 italic bold",text="Scores: "+str(coins)+"   Diamons: "+str(diamons))
                gameCondition  = False

    # Remove Booms---------------------------

    if len(allBoom)>0:
        firstBoom = allBoom[0]
        coordsFirstBoom = canvas.coords(firstBoom)
        if coordsFirstBoom[1] > WINDOW_HEIGHT - COIN_SIZE:
                removeBoom(0)
        boomIndexAtPlayer = findBoomIndexAt( getPlayerX(), getPlayerY() )
        if boomIndexAtPlayer != -1 :
            removeBoom(boomIndexAtPlayer)
            if gameCondition:
                lives -=1
                if lives == 0 :
                    canvas.create_image(350,350,image=over)
                    gameCondition = False
                if lives >= 0 :   
                    canvas.delete("de&in-CreaseLives")
                    canvas.create_text(30,140,fill = "white",font="Times 15 italic bold",text=str(lives),tags="de&in-CreaseLives")

        # Remove Diamons-------------------------------

    if len(allDiamon)>0:
        firstDiamon = allDiamon[0]
        coordsFirstDiamon = canvas.coords(firstDiamon)
        if coordsFirstDiamon[1] > WINDOW_HEIGHT - COIN_SIZE:
                removeDiamon(0)
        diamonIndexAtPlayer = findDiamonIndexAt( getPlayerX(), getPlayerY() )
        if diamonIndexAtPlayer != -1 :
            removeDiamon(diamonIndexAtPlayer)
            if gameCondition:
                if diamons < 3 : 
                    diamons +=1
                    canvas.delete("inCreaseDiamons")
                    canvas.create_text(30,200,fill = "white",font="Times 15 italic bold",text=str(diamons),tags="inCreaseDiamons")
                if diamons == 3 and coins >= 1800:
                    canvas.create_image(350,350,image=won)
                    canvas.create_rectangle(200,470,500,520,fill= "white")
                    canvas.create_text(350,500,fill = "darkblue",font="Times 20 italic bold",text="Scores: "+str(coins)+"   Diamons: "+str(diamons))
                    gameCondition  = False
    # Remove Shoots-------------------------------
                
    if len(allShoot)>0:
        firstShoot = allShoot[0]
        coordsFirstShoot = canvas.coords(firstShoot)
        if coordsFirstShoot[1] > WINDOW_HEIGHT - SHOOT_SIZE:
                removeShoot(0)
        shootIndexAtPlayer = findShootIndexAt( getPlayerX(), getPlayerY() )
        if shootIndexAtPlayer != -1 :
            removeShoot(shootIndexAtPlayer)
            if gameCondition:
                lives -=1
                if lives == 0 :
                    canvas.create_image(350,350,image=over)
                    gameCondition = False
                if lives >= 0 :   
                    canvas.delete("de&in-CreaseLives")
                    canvas.create_text(30,140,fill = "white",font="Times 15 italic bold",text=str(lives),tags="de&in-CreaseLives")
    # Remove Lifes----------------------------------

    if len(allLife)>0:
        firstLife = allLife[0]
        coordsFirstLife = canvas.coords(firstLife)
        if coordsFirstLife[1] > WINDOW_HEIGHT - COIN_SIZE:
                removeLife(0)
        lifeIndexAtPlayer = findLifeIndexAt( getPlayerX(), getPlayerY() )
        if lifeIndexAtPlayer != -1 :
            removeLife(lifeIndexAtPlayer)
            if gameCondition:
                if lives <  3 and lives > 0 :
                    lives +=1
                    canvas.delete("de&in-CreaseLives")
                    canvas.create_text(30,140,fill = "white",font="Times 15 italic bold",text=str(lives),tags="de&in-CreaseLives")
                    

# Moving position player-----------------------------------------   
        
def Right(event):
    if gameCondition and pauseCondition:
        if getPlayerX() < 650:
            canvas.move(player,50,0)

def Left(event):
    if gameCondition and pauseCondition:
        if getPlayerX() > 50:
            canvas.move(player,-50,0)

# Get position of Player-------------------

def getPlayerX():
    return canvas.coords(player)[0]

def getPlayerY():
    return canvas.coords(player)[1]

def entered(event):
    global startGame
    if startGame:
        startGame = False
        canvas.delete("start")
        addCoin()
        canvas.after(5000,lambda:addBoom())
        canvas.after(10000,lambda:addDiamon())
        canvas.after(40000,lambda:addLife())

if startGame:
    canvas.create_rectangle(200,230,500,280,fill= "white",tags="start")
    canvas.create_text(350,260,fill= "red",font="Times 15 italic bold",text="Find :  1800+ points    3 diamons",tags="start")
    playGame =tk.PhotoImage(file="img/play.png")
    canvas.create_image(350,350 ,image=playGame,tags="start")
    root.bind("<Key>",entered)
canvas.after(4000,lambda:addShoot()) 
canvas.after(60000,lambda:changePosition2())
canvas.after(60000,lambda:changePosition1())
canvas.tag_bind("sound","<Button-1>",Sound)
canvas.tag_bind("pause","<Button-1>",Pause)
root.bind("<Right>",Right)
root.bind("<Left>",Left)

#Main--------------------------------------------------------------------------

canvas.pack(expand=True, fill='both')
frame.pack(expand=True, fill='both')
root.mainloop()
 