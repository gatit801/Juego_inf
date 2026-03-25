from tkinter import *
from PIL import Image, ImageTk
import random

vent= Tk()
vent.geometry("600x400")
vent.title("Juego_infinito")
vent.config(bg="#5ABF92")

img=ImageTk.PhotoImage(Image.open('dadp.jpg'))

player1 = Label(vent, text ='jugador 1', bg ='#2DD650', fg = '#222B27')
player1.place(relx = 0.1, rely = 0.3, anchor = CENTER)

player2 = Label(vent, text ='jugador 2', bg ='#3ACFBB', fg = '#222B27')
player2.place(relx = 0.9, rely = 0.3, anchor = CENTER)

player_1_score_label = Label(vent, bg ='#2DD650', fg = 'white')
player_1_score_label.place(relx = 0.1, rely = 0.4, anchor = CENTER)

player_2_score_label = Label(vent, bg ='#3ACFBB', fg = 'white')
player_2_score_label.place(relx = 0.9, rely = 0.4, anchor = CENTER)

random_dice_label = Label(vent, bg = "#F7BE39", fg = 'white')
random_dice_label.place(relx = 0.5, rely = 0.5, anchor = CENTER)

player_score1 = 0

def player1():
    global player_score1
    random_no = random.randint(1,6)
    random_dice_label['text'] = 'Numero aleatorio del dado del jugador 1: ' + str(random_no)
    player_score1 = player_score1 + random_no
    player_1_score_label["text"] = str(player_score1)

player_score2 = 0

def player2():
    global player_score2
    random_no = random.randint(1,6)
    random_dice_label['text'] = 'Numero aleatorio del dado del jugador 2: ' + str(random_no)
    player_score2 = player_score2 + random_no
    player_2_score_label["text"] = str(player_score1)


player_1_btn = Button(vent, image=img, command=player1)
player_1_btn.image = img
player_1_btn.place(relx=0.2, rely=0.6, anchor= CENTER)


player_2_btn = Button(vent, image=img, command=player2)
player_2_btn.image = img
player_2_btn.place(relx=0.8, rely=0.6, anchor= CENTER)


vent.mainloop()