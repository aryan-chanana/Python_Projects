import random
import time
import tkinter
from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
from tkinter import messagebox
import pygame
from pygame import mixer

window = tkinter.Tk()
window.title("GAME")
window.columnconfigure(10,minsize=100)
window.rowconfigure([0,1,2,3,4,5,6,7],minsize = 50)
window.configure(bg="#9172EC")
LARGEFONT = ("Arial",24)
lablefont = ('times',20,'bold')
label = tkinter.Label(window, text = "TIC - TAC - TOE",font = LARGEFONT,fg = "white",bg="black").grid(row=0,column=1)
pygame.init()
mixer.music.load('D:\\Temp. Folder\\Programming\\Python\\Tic tac Toe\\background.wav')
mixer.music.play(-1)

def createNewWindow():
    global newWindow
    newWindow = tkinter.Toplevel(window)
    newWindow.configure(bg="#64E986")
    newWindow.columnconfigure(0,minsize=250)
    newWindow.rowconfigure([0,1,2,3,4],minsize=50)
    label1 = tkinter.Label(newWindow, text="LET THE GAME BEGIN", font=LARGEFONT, fg="white",bg="#810541").grid(row=0, column=1)
    columns = ''' 1 | 2 | 3 
__|__|__
4 | 5 | 6
__|__|__
7 | 8 | 9'''
    positions = tkinter.Label(newWindow, text=columns, fg="#0041C2",font=(LARGEFONT,40)).grid(row=2,column=0)
    display = tkinter.Label(newWindow, text="THESE ARE THE POSITIONS",bg="black", fg="white",font=(25)).grid(row=2,column=1)
    button_play = tkinter.Button(newWindow, text="START",command=game).grid(row=3, column=1)

arr = [1,2,3,4,5,6,7,8,9]
arr2 = ["","","","","","","","",""]
chance = 0
winner = ""
pos1 = IntVar()
def game():
    newWindow.destroy()
    global newWindow1
    newWindow1 = tkinter.Toplevel(window)
    newWindow1.title("GAME")
    newWindow1.columnconfigure(10,minsize=200)
    newWindow1.rowconfigure([0,1,2,3,4,5,6,7],minsize = 100)
    newWindow1.configure(bg="#F52887")
    LARGEFONT = ("Arial",28)
    lablefont = ('times',20,'bold')
    label = tkinter.Label(newWindow1, text = "TIC - TAC - TOE",font = LARGEFONT,fg = "white",bg="#571B7E").grid(row=0,column=2)

    label1=Label(newWindow1,text='   ')
    label2=Label(newWindow1,text='   ')
    label3=Label(newWindow1,text='   ')
    label3=Label(newWindow1,text='   ')
    label4=Label(newWindow1,text='   ')
    label5=Label(newWindow1,text='   ')
    label6=Label(newWindow1,text='   ')
    label7=Label(newWindow1,text='   ')
    label8=Label(newWindow1,text='   ')
    label9=Label(newWindow1,text='   ')

    label1.grid(row=2,column=1)
    label2.grid(row=2,column=2)
    label3.grid(row=2,column=3)
    label4.grid(row=3,column=1)
    label5.grid(row=3,column=2)
    label6.grid(row=3,column=3)
    label7.grid(row=4,column=1)
    label8.grid(row=4,column=2)
    label9.grid(row=4,column=3)

    position = tkinter.Entry(newWindow1, textvariable=pos1, width=30,bg="#BDEDFF").grid(row=1, column=0)
    enter = tkinter.Button(newWindow1, text="Enter position",command=show,bg="#BDEDFF").grid(row=1, column=2)

def show():
    global chance 
    chance += 1
    label=Label(newWindow1,text='X',font=("arial",12,"bold"))

    if pos1.get() <= 3:
        label.grid(row=2,column=pos1.get(),padx=10,pady=10)
    elif pos1.get() <= 6:
        label.grid(row=3,column=pos1.get()-3,padx=10,pady=10)
    elif pos1.get() < 10:
        label.grid(row=4,column=pos1.get()-6,padx=10,pady=10)
    arr2[pos1.get()-1] = 'x'
    arr.remove(pos1.get())

    # check
    if arr2[0] == arr2[4] and arr2[0] == 'x' and arr2[0] == arr2[8]:
        win()
        #time.sleep(2)
        newWindow1.destroy()

    elif arr2[0] == arr2[1] and arr2[0] == 'x' and arr2[0] == arr2[2]:
        win()
        #time.sleep(2)
        newWindow1.destroy()

    elif arr2[3] == arr2[4] and arr2[3] == 'x' and arr2[3] == arr2[5]:
        win()
        #time.sleep(2)
        newWindow1.destroy()

    elif arr2[6] == arr2[7] and arr2[6] == 'x' and arr2[6] == arr2[8]:
        win()
        #time.sleep(2)
        newWindow1.destroy()

    elif arr2[2] == arr2[4] and arr2[2] == 'x' and arr2[2] == arr2[6]:
        win()
        #time.sleep(2)
        newWindow1.destroy()

    elif arr2[0] == arr2[3] and arr2[0] == 'x' and arr2[0] == arr2[6]:
        win()
        #time.sleep(2)
        newWindow1.destroy()

    elif arr2[1] == arr2[4] and arr2[1] == 'x' and arr2[1] == arr2[7]:
        win()
        #time.sleep(2)
        newWindow1.destroy()

    elif arr2[2] == arr2[5] and arr2[2] == 'x' and arr2[2] == arr2[8]:
        win()
        #time.sleep(2)
        newWindow1.destroy()


    elif chance == 5:
        tied()
        #time.sleep(2)
        newWindow1.destroy()

    if winner != "yes" and chance != 5:
        comp = random.choice(arr)
        arr2[comp-1] = 'o'
        arr.remove(comp)
        label2=Label(newWindow1,text='O',font=("arial",12,"bold"))
        if comp <= 3:
            label2.grid(row=2,column=comp,padx=10,pady=10)
        elif comp <= 6 and comp >3:
            label2.grid(row=3,column=comp-3,padx=10,pady=10)
        elif comp <= 9 and comp > 6:
            label2.grid(row=4,column=comp-6,padx=10,pady=10)

    # check again
    if arr2[0] == arr2[4] and arr2[0] == 'o' and arr2[0] == arr2[8]:
        loss()
        #time.sleep(2)
        newWindow1.destroy()

    elif arr2[0] == arr2[1] and arr2[0] == 'o' and arr2[0] == arr2[2]:
        loss()
        #time.sleep(2)
        newWindow1.destroy()

    elif arr2[3] == arr2[4] and arr2[3] == 'o' and arr2[3] == arr2[5]:
        loss()
        #time.sleep(2)
        newWindow1.destroy()

    elif arr2[6] == arr2[7] and arr2[6] == 'o' and arr2[6] == arr2[8]:
        loss()
        #time.sleep(2)
        newWindow1.destroy()

    elif arr2[2] == arr2[4] and arr2[2] == 'o' and arr2[2] == arr2[6]:
        loss()
        #time.sleep(2)
        newWindow1.destroy()

    elif arr2[0] == arr2[3] and arr2[0] == 'o' and arr2[0] == arr2[6]:
        loss()
        #time.sleep(2)
        newWindow1.destroy()

    elif arr2[1] == arr2[4] and arr2[1] == 'o' and arr2[1] == arr2[7]:
        loss()
        #time.sleep(2)
        newWindow1.destroy()

    elif arr2[2] == arr2[5] and arr2[2] == 'o' and arr2[2] == arr2[8]:
        loss()
        #time.sleep(2)
        newWindow1.destroy()



def win():
    global winner
    winner = "yes"
    if winner == "yes":
        messagebox.showinfo("Congrats","You won!")
def loss():
    winner = "no"
    if winner == "no":
        messagebox.showinfo("Sorry","You lost!")
def tied():
    winner = ""
    if winner == "":
        messagebox.showinfo("Oh","Game Tied!")



button_1 = tkinter.Button(window,text = "PLAY GAME", width=32, height=3, bg = "#E67451", fg="black", cursor="hand2",command=createNewWindow,font=("arial",12,"bold")).grid(row=3, column=0)
# button_2 = tkinter.Button(window,text = "CHECK WIN COUNTER", width=32, height=3, bg = "#E67451", fg="#87F717", cursor="hand2").grid(row=3, column=2)
# button_3 = tkinter.Button(window,text = "CLICK FOR DEVELOPER DETAILS", width=32, height=3, bg = "#E67451", fg="#87F717", cursor="hand2").grid(row=5, column=0)
button_4 = tkinter.Button(window,text = "EXIT", width=32, height=3, bg = "#E67451", fg="black", cursor="hand2",command=window.destroy,font=("arial",12,"bold")).grid(row=3, column=2)
mainloop()