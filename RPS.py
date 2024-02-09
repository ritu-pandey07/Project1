from tkinter import *
from PIL import Image, ImageTk
from random import randint
#main window
root=Tk()
root.title("ROCK PAPER SCISSOR")
root.configure(background="black")

#picture
rock_image=ImageTk.PhotoImage(Image.open("rock_user.png"))
paper_image=ImageTk.PhotoImage(Image.open("paper_user.png"))
scissor_image=ImageTk.PhotoImage(Image.open("scissor_user.png"))
rock_image_computer=ImageTk.PhotoImage(Image.open("rock.png"))
paper_image_computer=ImageTk.PhotoImage(Image.open("paper.png"))
scissor_image_computer=ImageTk.PhotoImage(Image.open("scissor.png"))

#insert picture
user_label= Label(root,image=scissor_image, bg="black")
computer_label= Label(root,image=scissor_image_computer, bg="black")
computer_label.grid(row=1,column=0)
user_label.grid(row=1,column=4)




#scores
playerscore=Label(root,text=0,font=100,bg="black",fg="white")
computerscore=Label(root,text=0,font=100,bg="black",fg="white")
computerscore.grid(row=1,column=1)
playerscore.grid(row=1,column=3)

#indicators
user_indicator=Label(root,font=50,text="USER",bg="black",fg="white")
computer_indicator=Label(root,font=50,text="COMPUTER",bg="black",fg="white")
user_indicator.grid(row=0,column=3)
computer_indicator.grid(row=0,column=1)
#messages
msg=Label(root,font=50,bg="black",fg="white")
msg.grid(row=3,column=2)

#updating message
def updatemessage(x):
    msg['text']= x

#update user score
def updateuserscore():
    score=int(playerscore['text'])
    score+=1
    playerscore["text"]=str(score)
#update computer score
def updatecomputerscore():
    score=int(computerscore['text'])
    score+=1
    computerscore["text"]=str(score)

#check winner
def checkwin(player,computer):
    if player==computer:
        updatemessage("TIE!")
    elif player=="rock":
        if computer=="paper":
            updatemessage("YOU LOOSE")
            updatecomputerscore()
        else:
            updatemessage("YOU WIN")
            updateuserscore()
    elif player=="paper":
        if computer=="scissor":
            updatemessage("YOU LOOSE")
            updatecomputerscore()
        else:
            updatechoice("YOU WIN")
            updateuserscore()
    elif player=="scissor":
        if computer=="paper":
            updatemessage("YOU LOOSE")
            updatecomputerscore()
        else:
            updatemessage("YOU WIN")
            updateuserscore()

    else:
        pass



#update choices
choices=["rock","paper","scissor"]
def updatechoice(x):
#computer choice    
    computer_choice=choices[randint(0,2)]
    if computer_choice=="rock":
        computer_label.configure(image=rock_image_computer)
    elif computer_choice=="paper":
        computer_label.configure(image=paper_image_computer)
    else:
        computer_label.configure(image=scissor_image_computer)

 #for user   
    if x=="rock":
        user_label.configure(image=rock_image)
    elif x=="paper":
        user_label.configure(image=paper_image)
    else:
        user_label.configure(image=scissor_image)
    checkwin(x,computer_choice)


#buttons
rock=Button(root,width=15,height=3,text="ROCK",bg="red",
            fg="black",command=lambda:updatechoice("rock"))
paper=Button(root,width=15,height=3,text="PAPER",bg="red",
             fg="black",command=lambda:updatechoice("paper"))
scissor=Button(root,width=15,height=3,text="SCISSOR",bg="red",
               fg="black",command=lambda:updatechoice("scissor"))
rock.grid(row=2,column=1)
paper.grid(row=2,column=2)
scissor.grid(row=2,column=3)

root.mainloop()