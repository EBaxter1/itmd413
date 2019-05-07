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
coins = ("Quarters:", "Dimes:", "Nickels:", "Pennies:", "Half-Dollars:", "Dollar Coins")

window = Tk()
window.title("Change Counter")
window.geometry('450x155')
window.configure(background = "tan");

quart = Label(window ,text = "Quarters:").grid(row = 0,column = 0)
quart1 = Entry(window).grid(row = 0,column = 1)

dime = Label(window ,text = "Dimes:").grid(row = 1,column = 0)
dime1 = Entry(window).grid(row = 1,column = 1)

nick = Label(window ,text = "Nickels:").grid(row = 2,column = 0)
nick1 = Entry(window).grid(row = 2,column = 1)

pen = Label(window ,text = "Pennies:").grid(row = 3,column = 0)
pen1 = Entry(window).grid(row = 3,column = 1)

hDoll = Label(window ,text = "Half-Dollar:").grid(row = 4,column = 0)
hDoll1 = Entry(window).grid(row = 4,column = 1)

doll = Label(window ,text = "Dollar Coin:").grid(row = 5,column = 0)
doll1 = Entry(window).grid(row = 5,column = 1)

quartValue = Label(window ,text = "Quarter value: $").grid(row = 0,column = 2)
quartValue1 = Entry(window).grid(row = 0,column = 3)

def ThankYou():
    messagebox.showinfo("Submited", "Thank You!")
    
btn = ttk.Button(window, text="Compute", command=ThankYou).grid(row=6,column=0)
window.mainloop()
