import tkinter as tk
from tkinter import messagebox
from tkinter import *
import pygame 
from PIL import Image,ImageTk
import random

root = Tk()
root.title("Rock Paper Scissor")
root.config(bg="#8DD7BF")
root.geometry('500x560+400+100')   

computer=Label(root,text = "COMPUTER'S CHOICE",bg='#8DD7BF',font = ("Helvetica 26 bold"))
computer.grid(row=1,column=3)

player = Label(root,text = "USER'S CHOICE",bg='#8DD7BF',font = ("Helvetica 26 bold"))
player.grid(row=1,column=10)

rock_image=ImageTk.PhotoImage(Image.open("rockl.png"))
paper_image=ImageTk.PhotoImage(Image.open("paperl.png"))
scissor_image=ImageTk.PhotoImage(Image.open("scissorl.png"))

comp_rock_image=ImageTk.PhotoImage(Image.open("rockr.png"))
comp_paper_image=ImageTk.PhotoImage(Image.open("paperr.png"))
comp_scissor_image=ImageTk.PhotoImage(Image.open("scissorr.png"))

comp_label = Label(root,image=comp_scissor_image,bg="#8DD7BF")
user_label = Label(root,image=scissor_image,bg="#8DD7BF")
comp_label.grid(row=2,column=3)
user_label.grid(row=2,column=10)

user_score=Label(root,text = "USER'S SCORE",bg='#8DD7BF',font = ("Helvetica 12 bold"))
comp_score=Label(root,text = "COMPUTER'S SCORE",bg='#8DD7BF',font = ("Helvetica 12 bold"))
user_score.grid(row=3,column=10)
comp_score.grid(row=3,column=3)

user_score1=Label(root,text = 0,bg='#8DD7BF',font = ("Helvetica 12 bold"))
comp_score1=Label(root,text = 0,bg='#8DD7BF',font = ("Helvetica 12 bold"))
user_score1.grid(row=4,column=10)
comp_score1.grid(row=4,column=3)

winner_label=Label(root,text='',bg='#8DD7BF',font = ("Helvetica 20 bold"))
winner_label.grid(row=5,column=6)

def update_winner():
    if((user_score1['text'])==(comp_score1['text'])):
        winner_label["text"] = 'Its tie!!!'
    elif((user_score1['text'])>(comp_score1['text'])):
        winner_label["text"] = 'You Win..'
    elif((user_score1['text'])<(comp_score1['text'])):
        winner_label["text"] = 'You Loose..'

def update_user_score():
    score = int(user_score1["text"])
    score+=1
    user_score1["text"] = str(score)

def update_comp_score():
    score = int(comp_score1["text"])
    score+=1
    comp_score1["text"] = str(score)

def check_winner(user_choice,comp_choice):
    if(user_choice==comp_choice):
        pass
    if(user_choice=='ROCK' and comp_choice=='PAPER'):
        update_comp_score()
    if(user_choice=='ROCK' and comp_choice=='SCISSOR'):
        update_user_score()
    if(user_choice=='PAPER' and comp_choice=='ROCK'):
        update_user_score()
    if(user_choice=='PAPER' and comp_choice=='SCISSOR'):
        update_comp_score()
    if(user_choice=='SCISSOR' and comp_choice=='PAPER'):
        update_user_score()
    if(user_choice=='SCISSOR' and comp_choice=='ROCK'):
        update_comp_score()

opts=['ROCK','PAPER','SCISSOR']

def displaychoice(val):
    comp_choice=random.choice(opts)
    if(comp_choice=='ROCK'):
        comp_label.configure(image=comp_rock_image)
    elif(comp_choice=='PAPER'):
        comp_label.configure(image=comp_paper_image)
    elif(comp_choice=='SCISSOR'):
        comp_label.configure(image=comp_scissor_image)

    if(val=='ROCK'):
        user_label.configure(image=rock_image)
    elif(val=='PAPER'):
        user_label.configure(image=paper_image)
    else:
        user_label.configure(image=scissor_image)

    check_winner(val,comp_choice)
def reset():
    user_score1['text']=str(0)
    comp_score1['text']=str(0)
    winner_label["text"]=''
    
rock=Button(root,text='ROCK',bg='#FF3E4D',font='arial 10 bold',height=3,width=20,bd=2,command=lambda :displaychoice('ROCK')).grid(row=4,column=5)
paper=Button(root,text='PAPER',bg='#FAD02E',font='arial 10 bold',height=3,width=20,bd=2,command=lambda :displaychoice('PAPER')).grid(row=4,column=6)
scissor=Button(root,text='SCISSOR',bg='#0ABDE3',font='arial 10 bold',height=3,width=20,bd=2,command=lambda :displaychoice('SCISSOR')).grid(row=4,column=7)

play_again=Button(root,text='PLAY AGAIN',bg='green',fg="white",font='arial 10 bold',height=4,width=20,bd=4,command=reset).grid(row=8,column=6)
quit=Button(root,text='QUIT',bg='red',fg="white",height=4,width=20,font='arial 10 bold',bd=4,command=update_winner).grid(row=7,column=6)

root.mainloop()