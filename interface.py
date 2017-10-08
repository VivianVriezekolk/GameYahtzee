import tkinter as tk

class Interface():
    def __init__(self, model):
        self.yahtzee = model

    def welcome_message(self):
        self.top = tk.Tk()
        self.frame = tk.Frame(self.top)
        self.photo = tk.PhotoImage(file="yatzee.png")

    def ask_amount_players(self):
        print('blabla')