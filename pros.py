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
bg = tk.PhotoImage(file = "img/bg.png")
bg_win = canvas.create_image(350,400,image=bg)
pl = tk.PhotoImage(file = "img/player.png")
player = canvas.create_image(350,650,image=pl)
#Variable---------------------------------------------------------------------

# winsound.PlaySound("sound/playing.wav",winsound.SND_FILENAME) 
# rectangle = canvas.create_rectangle(235,650,365,670,fill="black")
x = 0
y =10

# x=0
# y = 0
# condition = True
# IMG 

# #Function---------------------------------------------------------------------
def red():
    size3 = random.randrange(100,600)
    canvas.create_oval(size3,0,size3+20,20, fill = "red",tags="life")
def black():
    size2 = random.randrange(100,600)
    canvas.create_oval(size2,0,size2+20,20, fill = "black",tags="boom")

def ball():
    canvas.move("ball",x,y)

def boom():
    black()
    canvas.move("boom",x,y)

def life():
    red()
    canvas.move("life",x,y)

def myRectangle():
#    print("User have clicked at position:",event.x,event.y)
   global x,y,condition
   
#    if x<550 and y<550 and condition:
#       x +=50
#       y+=50
#    else:
#       condition = False
#       x -=50
#       y -=50
#       if x==0 and y==0:
#          condition = True
   size1 = random.randrange(100,600)
#    size2 = random.randrange(100,600)
#    size3 = random.randrange(100,600)
   canvas.create_oval(size1,0,size1+20,20, fill = "blue",tags="ball")
#    canvas.create_oval(size2,0,size2+20,20, fill = "black",tags="boom")
#    canvas.create_oval(size3,0,size3+20,20, fill = "red",tags="life")
   ball()
   canvas.after(1000,lambda:boom())
   canvas.after(5000,lambda:life())
#    canvas.after(200,lambda:ball())
   canvas.after(200,lambda:myRectangle())
   

def Right(event):
    positionplayer=canvas.coords(player)
    if positionplayer[0]<650:
        canvas.move(player,30,0)
def Left(event):
    positionplayer=canvas.coords(player)
    if positionplayer[0]>50:
        canvas.move(player,-30,0)

# canvas.tag_bind("PNCTarget","<Button-1>",myEventTrigger)
# root.bind("<Button-1>",myEventTrigger)
myRectangle()
root.bind("<Right>",Right)
root.bind("<Left>",Left)


#Main--------------------------------------------------------------------------
# myEventTrigger()

canvas.pack(expand=True, fill='both')
frame.pack(expand=True, fill='both')
root.mainloop()

