import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
import main
import players
import yahtzee

class Design(tk.Frame):

    def __init__(self):
        self.main = main.Main()
        self.top = tk.Tk()
        self.frame = tk.Frame(self.top)
        self.photo = tk.PhotoImage(file="yatzee.png")
        self.button = tk.Button(self.top, image=self.photo, command=self.start_game)
        self.button.photo = self.photo
        self.var = StringVar()
        self.label = tk.Label(self.top, textvariable=self.var, relief = tk.FLAT)
        self.entry = tk.Entry()
        self.buttonEntry = tk.Button(self.top, text = "play", command= self.amount_players)
        self.players = 0
        self.entries = []
        self.yatzee = yahtzee.Yatzee()
        self.main.yahtzee = self.yatzee
        self.variable = StringVar()
        self.label2 = tk.Label(self.top, textvariable = self.variable)

    def make_start_screen(self):
        self.frame.pack()
        self.button.pack()
        tk.mainloop()

    def amount_players(self):
        self.players = self.entry.get()
        self.buttonEntry.configure(command=self.make_players)
        self.var.set("What are the names of the players?")
        for player in range(int(self.players)):
            self.entries.append(tk.Entry())
            self.entries[player].pack()

        self.entry.destroy()

    def make_players(self):
        for index in range(int(self.players)):
            name = self.entries[index].get()
            player = players.Player()
            player.name = name
            print(player.name)
            self.yatzee.players.append(player)
            self.entries[index].destroy()
        self.label2.pack()
        self.main.startGame()

    def start_game(self):
        self.button.destroy()
        self.top.geometry("750x750")
        self.var.set("With how many players do you want to play?")
        self.label.pack(side = TOP)
        self.entry.pack(side = TOP)
        self.buttonEntry.pack()

#design = Design()
#design.make_start_screen()
