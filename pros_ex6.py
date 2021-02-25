#Import-----------------------------------------------------------------------
import tkinter as tk
import random
#Windows----------------------------------------------------------------------
root = tk.Tk() 
root.geometry("600x600")
frame = tk.Frame() 
frame.master.title("pros.nob")
canvas = tk.Canvas(frame)
#Constants--------------------------------------------------------------------

#Variable---------------------------------------------------------------------
oval = canvas.create_oval(50,50,100,100, fill = "blue")
rectangle = canvas.create_rectangle(235,530,365,550,fill="black")
myImage = tk.PhotoImage(file="img/images.png")
canvas.create_image(10,10,image=myImage)
x = 10
y =0

# x=0
# y = 0
# condition = True
# #Function---------------------------------------------------------------------
# def myEventTrigger():
# #    print("User have clicked at position:",event.x,event.y)
#    global x,y,condition
#    if x<550 and y<550 and condition:
#       x +=50
#       y+=50
#    else:
#       condition = False
#       x -=50
#       y -=50
#       if x==0 and y==0:
#          condition = True
#    randomColor = random.choice(colors)
#    canvas.itemconfig(oval, fill = randomColor)
#    canvas.moveto(oval,x,y)
#    canvas.after(100,lambda:myEventTrigger())

def moverectangle(event):
    global x,y,positionrectangle
    myImage = canvas.create_image(100,100,image=myImage)
    positionrectangle=canvas.coords(rectangle)
    if positionrectangle[0]<460:
        canvas.move(myImage,x,y)
def Left(event):
    global x,y
    myImage = canvas.create_image(100,100,image=myImage)
    positionrectangle=canvas.coords(rectangle)
    if positionrectangle[0]>0:
        canvas.move(myImage,-x,y)

# canvas.tag_bind("PNCTarget","<Button-1>",myEventTrigger)
# root.bind("<Button-1>",myEventTrigger)
root.bind("<Right>",moverectangle)
root.bind("<Left>",Left)

#Main--------------------------------------------------------------------------
# myEventTrigger()

canvas.pack(expand=True, fill='both')
frame.pack(expand=True, fill='both')
root.mainloop()