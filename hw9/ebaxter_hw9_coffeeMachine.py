'''
File Name: ebaxter_hw9_coffeeMachine.py
Made by: Erin Baxter
This program will have the class for a coffee machine and the methods needed to interact with it
'''

# class that has methods to get information about a coffeeMachine 
class coffeeMachine:
    #constructor for number of cups, price of coffee and total amount of moeny inserted by user
    def __init__(self,quantity = 0, price = 1.30, total = 0.0):
        self.price = price
        self.quantity = quantity
        self.total = total

    # get the current quantity of coffee
    def getQuantity(self):
        return self.quantity

    # get the current price of coffee
    def getPrice(self):
        return self.price
    
    # get the total amount of user money 
    def getTotal(self):
        return self.total

    # set current quantity 
    def setQuantity(self, quantity):
        self.quantity = quantity

    #set current user total entered money
    def setTotal(self, total):
        self.total = total

        
        

