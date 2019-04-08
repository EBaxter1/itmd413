'''
File Name: ebaxter_hw9_coffeeMachine.py
Made by: Erin Baxter
This program will have the class for a coffee machine and the methods needed to interact with it
'''

class coffeeMachine:
    #stock machine with cups and set price
    def __init__(self,quantity = 10, price = 1.30, total = 0.0):
        self.price = price
        self.quantity = quantity
        self.total = total

    # display the quantity and price of coffee
    def getQuantity(self):
        return self.quantity

    def getPrice(self):
        return self.price

    def getTotal(self):
        return self.total

    def setQuantity(self, quantity):
        self.quantity = quantity

    def setTotal(self, total):
        self.total = total

        
        

