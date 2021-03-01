#Import-----------------------------------------------------------------------
import tkinter as tk
import random
# import winsound
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
life = canvas.create_image(30,120 ,image=lf)
soundon =tk.PhotoImage(file="img/soundon.png")
canvas.create_image(650,50 ,image=soundon,tags="on")
soundoff =tk.PhotoImage(file="img/soundoff.png")
life_image= tk.PhotoImage(file="img/life.png")
diamon_image= tk.PhotoImage(file="img/diamon.png")
boom_image= tk.PhotoImage(file="img/boom.png")

diamon = canvas.create_image(30,180,image=diamon_image)

WINDOW_WIDTH = 700
WINDOW_HEIGHT = 800
COIN_SIZE = LIFE_SIZE=BOOM_SIZE=DIAMON_SIZE=30  # height = with
soundX = 650
soundY = 50
#Variable--------------------------------------------- ------------------------
soundCondition = True
gameCondition = True
allCoin =[]
allLife =[]
allDiamon =[]
allBoom =[]

coins = 0
lives = 3
diamons = 0
booms = 0
canvas.create_text(30,90,fill = "darkblue",font="Times 10 italic bold",text="Scores: "+str(coins),tags="inCreaseCoins")
canvas.create_text(30,150,fill = "darkblue",font="Times 10 italic bold",text="Lives: "+str(lives),tags="de&in-CreaseLives")
canvas.create_text(40,210,fill = "darkblue",font="Times 10 italic bold",text="Diamons: "+str(diamons),tags="inCreaseDiamons")

# #Function---------------------------------------------------------------------

# Adding Elements--------------------------------------------------------------

def addLife():
    global allLife
    lifeX = random.randrange(100,600)
    allLife.append(canvas.create_image(lifeX,0,image=life_image,tags="coin"))
    canvas.after(30000,lambda:addLife())
    

def addDiamon():
    global allDiamon
    diamonX = random.randrange(100,600)
    allDiamon.append(canvas.create_image(diamonX,0,image=diamon_image,tags="coin"))
    canvas.after(20000,lambda:addDiamon())
    

def addBoom():
    global allBoom
    boomX = random.randrange(100,600)
    allBoom.append(canvas.create_image(boomX,0,image=boom_image,tags="coin"))
    canvas.after(2000,lambda:addBoom())
    

def addCoin():
    global allCoin
    coinX = random.randrange(100,600)
    allCoin.append(canvas.create_image(coinX,0,image=coin_image,tags="coin"))
    canvas.after(200,lambda:addCoin())
    moveCoin()

# Removing Elements----------------------------------------------------------

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

# Removing Elements----------------------------------------------------------------
def Sound(event):
    global soundCondition,soundX,soundY
    if (event.x >= soundX - 15 and event.x <= soundX + 15) and (event.y >= soundY - 15 and event.y <= soundY + 15)and soundCondition:
        canvas.delete("on")
        canvas.create_image(650,50 ,image=soundoff,tags="on")
        soundCondition = False
    elif (event.x >= soundX - 15 and event.x <= soundX + 15) and (event.y >= soundY - 15 and event.y <= soundY + 15)and not soundCondition:
        canvas.delete("on")
        canvas.create_image(650,50 ,image=soundon,tags="on")
        soundCondition = True
def moveCoin():
    global coins,lives,diamons,booms,gameCondition
    canvas.move("coin",0,20)

    # 1 - Remove the first coin if outside of the window
    firstCoin = allCoin[0]
    coordsFirstCoin = canvas.coords(firstCoin)
    if coordsFirstCoin[1] > WINDOW_HEIGHT - COIN_SIZE:
            removeCoin(0)
    # 2 - If player is on a coin remove the coin
    coinIndexAtPlayer = findCoinIndexAt(getPlayerX(), getPlayerY())
    if coinIndexAtPlayer != -1 :
        removeCoin(coinIndexAtPlayer)
        # if lives != 0 and diamons != 3:
        if gameCondition:
            coins +=1
            canvas.delete("inCreaseCoins")
            canvas.create_text(30,90,fill = "darkblue",font="Times 10 italic bold",text="Scores: "+str(coins),tags="inCreaseCoins")
            print("got coins",coins)
    # Remove Booms
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
                    canvas.create_text(350,400,fill = "red",font="Times 50 italic bold",text="GAME OVER",tags="")
                    gameCondition = False
                if lives >= 0 :   
                    canvas.delete("de&in-CreaseLives")
                    canvas.create_text(30,150,fill = "darkblue",font="Times 10 italic bold",text="Lives: "+str(lives),tags="de&in-CreaseLives")
                    print("got booms",booms)
                    # and diamons != 3
        # Remove Diamons
    if len(allDiamon)>0:
        firstDiamon = allDiamon[0]
        coordsFirstDiamon = canvas.coords(firstDiamon)
        if coordsFirstDiamon[1] > WINDOW_HEIGHT - COIN_SIZE:
                removeDiamon(0)
        diamonIndexAtPlayer = findDiamonIndexAt( getPlayerX(), getPlayerY() )
        if diamonIndexAtPlayer != -1 :
            removeDiamon(diamonIndexAtPlayer)
            if gameCondition:
                diamons +=1
                if diamons == 3:
                    canvas.create_text(350,400,fill = "darkblue",font="Times 50 italic bold",text="YOU WON",tags="")
                    gameCondition  = False
                if diamons <= 3 :
                    canvas.delete("inCreaseDiamons")
                    canvas.create_text(40,210,fill = "darkblue",font="Times 10 italic bold",text="Diamons: "+str(diamons),tags="inCreaseDiamons")
                    print("got diamons",diamons)
                    # and lives > 0
    # Remove Lifes
    if len(allLife)>0:
        firstLife = allLife[0]
        coordsFirstLife = canvas.coords(firstLife)
        if coordsFirstLife[1] > WINDOW_HEIGHT - COIN_SIZE:
                removeLife(0)
        lifeIndexAtPlayer = findLifeIndexAt( getPlayerX(), getPlayerY() )
        if lifeIndexAtPlayer != -1 :
            removeLife(lifeIndexAtPlayer)
            if gameCondition:
                # if lives <  3 and lives > 0 and diamons != 3 :
                lives +=1
                canvas.delete("de&in-CreaseLives")
                canvas.create_text(30,150,fill = "darkblue",font="Times 10 italic bold",text="Lives: "+str(lives),tags="de&in-CreaseLives")
                print("got lives",lives)

# Moving position player-----------------------------------------   
        
def Right(event):
    if getPlayerX() < 650:
        canvas.move(player,50,0)

def Left(event):
    if getPlayerX() > 50:
        canvas.move(player,-50,0)

# Get position of Player

def getPlayerX():
    return canvas.coords(player)[0]

def getPlayerY():
    return canvas.coords(player)[1]

addCoin()
canvas.after(5000,lambda:addBoom())
canvas.after(10000,lambda:addDiamon())
canvas.after(20000,lambda:addLife())

canvas.tag_bind("on","<Button-1>",Sound)
root.bind("<Right>",Right)
root.bind("<Left>",Left)

#Main--------------------------------------------------------------------------

canvas.pack(expand=True, fill='both')
frame.pack(expand=True, fill='both')
root.mainloop()

