import time
from tkinter import *
from random import *
from PIL import ImageTk,Image
global compp
global userp
CompScore = 0
UserScroe = 0
global rnd
roundn=0

def click(event):

    time.sleep(0.7)
    global roundn
    roundn=roundn+1
    global CompScore
    global UserScroe
    gf=["a","b","c"]
    l1=["SNAKE","WATER","GUN"]
    i = 1
    userch = event.widget.cget("text")

    print("Round-", i)
    compchoise =choice(l1)
    if compchoise=="GUN":
        l2.config(image=my_img3)
    elif compchoise=="WATER":
        l2.config(image=my_img2)
    else:
        l2.config(image=my_img)
    print(compchoise)
    print(userch)

    if userch == 'GUN' and compchoise == 'SNAKE':
        print("you Win!")
        UserScroe = UserScroe + 1
        l3['text']="You Win!"
    elif userch == 'WATER' and compchoise == 'GUN':
        print("you win")
        UserScroe = UserScroe + 1
        l3['text'] = "You Win!"
    elif userch == 'SNAKE' and compchoise == 'WATER':
        print("you win")
        UserScroe = UserScroe + 1
        l3['text'] = "You Win!"
    elif compchoise == userch:

        print("round draw")
        l3['text'] = "Same choise!!"
    else:
        print("You Lose!")
        CompScore = CompScore + 1
        l3['text'] = "You Lose!!"
    i =str(roundn)
    rnds="Round "+ i
    rnd.set(rnds)
    l9.update()
    userp.set(UserScroe)
    l6.update()
    compp.set(str(CompScore))
    l7.update()


root=Tk()
root.geometry("500x600")
root.title("Snake-Water-Gun")
root.config(bg="light yellow")
userp=StringVar()
compp=StringVar()
rnd=StringVar()
l1=Label(root,text="Snake Water Gun",bg="light yellow",font=('lucida','24','bold'))
l1.place(x=110,y=10)
l9=Label(text="0",textvar=rnd,font=('Times new roman','18','bold'),fg='red',bg='light yellow')
l9.place(x=200,y=60)

#adding computer choise label
image1 = Image. open('images/question-mark.jpg')
image1 = image1. resize((120, 165), Image. ANTIALIAS)
my_img1= ImageTk. PhotoImage(image1)
l2=Label(root,image=my_img1,width=120,height=165)
l2.place(x=190,y=100)
l3=Label(root,text="user choise",font=('times new roman','26','italic'),bg='light yellow')
l3.place(x=170,y=280)
l4=Label(text="User Points:",font=("lucida",'12','bold'),fg="brown",bg='light yellow')
l4.place(x=25,y=75)
l6=Label(text="0",textvar=userp,font=('Times new roman','100','bold'),fg='red',bg='light yellow')
l6.place(x=25,y=110)
l5=Label(text="Computer Points:",font=("lucida",'12','bold'),fg="brown",bg='light yellow')
l5.place(x=345,y=75)
l7=Label(text="0",textvar=compp,font=('Times new roman','100','bold'),fg='red',bg="light yellow")
l7.place(x=380,y=110)

#adding user selection buttons
#snake
image = Image. open('images/snake.jpg')
# The (450, 350) is (height, width)
image = image. resize((120, 165), Image. ANTIALIAS)
my_img = ImageTk. PhotoImage(image)
b1=Button(root,text="SNAKE",font=('arial','18','bold'),image=my_img,activebackground="red",bg="silver",width=120,height=165)
b1.place(x=25,y=350)
b1.bind("<Button-1>",click)

#water
image2 = Image. open('images/water.jpg')
image2 = image2. resize((120, 165), Image. ANTIALIAS)
my_img2 = ImageTk. PhotoImage(image2)
b2=Button(root,text="WATER",font=('arial','18','bold'),image=my_img2,activebackground="red",bg="silver",width=120,height=165,bd=2)
b2.place(x=190,y=350)
b2.bind("<Button-1>",click)

#gun
image3 = Image. open('images/gun.jpg')
image3 = image3. resize((120, 165), Image. ANTIALIAS)
my_img3 = ImageTk. PhotoImage(image3)
b3=Button(root,text="GUN",font=('arial','18','bold'),image=my_img3,activebackground="red",bg="silver",width=120,height=165)
b3.place(x=350,y=350)
b3.bind("<Button-1>",click)

root.mainloop()