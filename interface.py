import tkinter as tk
from tkinter import *
#from PIL import Image, ImageTk

class Interface():
    def __init__(self, model):
        self.yahtzee = model
        self.top = tk.Tk()
        self.frame = tk.Frame(self.top)
        self.photo = tk.PhotoImage(file="yatzee.png")
        self.button = tk.Button(self.top, image=self.photo, command=self.start_game)
        self.button.photo = self.photo
        self.var = StringVar()
        self.label = tk.Label(self.top, textvariable=self.var, relief=tk.FLAT)
        self.entry = tk.Entry()
        self.buttonEntry = tk.Button(self.top, text="play", command=self.amount_players)
        self.amount_players = 0

    def welcome_message(self):
        self.frame.pack()
        self.button.pack()
        tk.mainloop()

    def start_game(self):
        self.button.destroy()
        self.top.geometry("750x750")
        self.var.set("With how many players do you want to play?")
        self.label.pack(side=TOP)
        self.entry.pack(side=TOP)
        self.buttonEntry.pack()

    def amount_players(self):
        amount_of_players = input()
        self.amount_players = amount_of_players

    def ask_name_of_players(self):
        names = []
        for player in self.yahtzee.players:
            names.append(input("What is the name of the player " + str(player.player_number + 1) + "? \n"))
        return names

    def printScores(self):
        print(self.yahtzee.dice_eyes)