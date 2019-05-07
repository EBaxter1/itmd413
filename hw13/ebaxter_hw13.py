'''
File name: ebaxter_hw13.py
Made by: Erin Baxter
This program will make a GUI that
computes the dollar and cents value of coins input
'''

print("Hello and welcome to the Change Counter 27,000!")

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
allCoins = ("Quarters", "Dimes", "Nickels", "Pennies", "Half-Dollars", "Dollar Coins")

window = Tk()
window.title("Change Counter")
window.geometry('450x400')
window.configure(background = "tan");

def calc(coins):
    try:
        quart = (int(coins["Quarters"].get()) * .25)
        print(quart)

        dime = (int(coins["Dimes"].get()) * .10)
        print(dime)

        nick = (int(coins["Nickels"].get()) * .05)
        print(nick)
        
        pen = (int(coins["Pennies"].get()) * .01)
        print(pen)

        hDol = (int(coins["Half-Dollars"].get()) * .50)
        print(hDol)

        dol = (int(coins["Dollar Coins"].get()) * .50)
        print(dol)
        
    except ValueError:
        print("Please enter whole values only!")

def makeFields(window, coins):
    fields = {}
    for coin in coins:
        row = Frame(window)
        lab = Label(row, width=22, text=coin+":", anchor="w")
        ent = Entry(row)
        ent.insert(0,"0")
        row.pack(side=TOP, fill=X, padx=5, pady=5)
        lab.pack(side=LEFT)
        ent.pack(side=RIGHT, expand=YES,fill=X)
        fields[coin] = ent
    return fields

def ThankYou():
    messagebox.showinfo("Submited", "Thank You!")

    
ents = makeFields(window, allCoins)
window.bind("<Return>", (lambda event, e=ents: fetch(e)))

btn = ttk.Button(window, text="Compute", command=(lambda e=ents: calc(e)))
btn.pack(side=LEFT, padx=5, pady=5)

window.mainloop()
