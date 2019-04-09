'''
File Name: ebaxter_hw9_testCoffeeMachine.py
Made by: Erin Baxter
This program will have the methods to test the coffeeMachine class
'''
# get class information from other file
from ebaxter_hw9_coffeeMachine import coffeeMachine
#make a global variable for bew object
newMachine = coffeeMachine()

print("Hello and welcome to the Coffee Maaker 19,000!")

#main method gives user menu options for what they want to do
def main():
    # variable to run loop
    noStop = "y"

    # while loop for menu
    while noStop == "y":
        # try to make sure options are int
        try:
            menuOption = int(input(f'''\nWhat would you like to do?\n1. Check current inverntory and price(enter 1)\n2. Insert coins(enter 2)\n3. Select coffee(enter 3)\n4. Refund money(enter 4)\n5. Exit program (enter any key other then 1-4)\nEnter option: '''))
            # menu options 
            if menuOption == 1:
                # set varaibles from menu method 
                amount, price = menu()
                print(f"\nThe quantity of cups currently in the machine is {amount} and the price per cup is: " + "${:.2f}".format(price))
            elif menuOption == 2:
                # check to see if any inventory is even there 
                if newMachine.getQuantity() == 0:
                    print("\nCurrent inventory is 0. Coffee can not be made. please try again later")
                else:
                    # try to make sure everything is an int
                    try:
                        quart = int(input("\nPlease enter the number of quarters you would like to insert: "))
                        dime = int(input("Please enter the number of dimes you would like to insert: "))
                        nick = int(input("Please enter the number of nickeles you would like to insert: "))
                        # call insert method 
                        insert(quart, dime, nick)
                    except ValueError:
                        print("Error! Please enter a whole number!")
            elif menuOption == 3:
                select() # call select method
            elif menuOption == 4:
                refund() # call refund method
            else:
                noStop = "n" # stop while loop
        except ValueError:
            noStop = "n" # stop while loop


# this funciton returns current the quantity and price
def menu():
    # set variables using class methods 
    quantity = newMachine.getQuantity()
    price = newMachine.getPrice()
    return quantity, price

#this function sets variables based on class and calculated new user total 
def insert(quarters, dimes, nickels):
    # set variables based on current class price
    price = newMachine.getPrice()
    # calculated total amount of money inserted
    userTotal = (quarters * 0.25) + (dimes * 0.10) + (nickels * 0.05)
    # set new total for user money 
    newMachine.setTotal(userTotal)

# function to dispresene coffee based on selection 
def select():
    # variables set by class methods
    newTotal = round(newMachine.getTotal(), 2) # round so it is a money number 
    singlePrice = newMachine.getPrice()
    inventory = newMachine.getQuantity()
    # string drawing 
    createCoffee = '''Coffee is now being dispensed...
                  _________
                  ______   |
                        |__|
                         ||
                         || 
                   _______________
                   \             /
                    \           /
                     \         /  
                     |        |
                     |        |
                     |        |
                     |________|
                     --------------------------
              
                  _________
                  ______   |
                        |__|
                         
                                     |||                            
                               _______________
                               \             /
                                \  Caution  /
                                 \   Hot!  /  
                                 |        |
                                 |        |
                                 |        |
                                 |________|
                     --------------------------\n\nCoffee done pouring. Enjoy!'''
    #output current user total 
    print("\nCurrent Change Inserted: " + "${:.2f}".format(newTotal))
    #make sure inverntory or total isn't 0
    if inventory == 0:
        print("Current inventory is 0. Coffee can not be made. please try again later")
        if newTotal > 0:
            refund() # call refund method just incase 
    elif newTotal == 0:
        print("Please insert coins. Price per cup is " + "${:.2f}".format(singlePrice))
    else:
        try:
            # aask user for how many coffees they want
            amount = int(input("How many cups of coffee do you want?: "))
            if (newTotal / amount) == singlePrice and amount <= inventory:
                # re-set quantity and total 
                newMachine.setQuantity(inventory - amount)
                newMachine.setTotal(0.0)
                # output the drawing
                print(createCoffee)
            # check and make sure the total matchs cost of drinks 
            elif newTotal != (amount * singlePrice):
                print("Error! Exact change is required, price per cup is " + "${:.2f}".format(singlePrice) + ". Please try again with a total change amount of " + "${:.2f}".format(amount * singlePrice))
                refund() # call refund
            elif amount > inventory and inventory > 0:
                # check and see if they are willing to have less coffee
                ask = input(f"There is not enough inventory for {amount} cup(s) of coffee. Current quantity of cups is {inventory}. Would you like to make {inventory} cup(s) of coffee instead?(Enter y for yes or anything else for no): ")
                if ask.lower() == "y":
                    groupPrice = singlePrice * inventory
                    # set new quantity and total 
                    newMachine.setQuantity(0)
                    newMachine.setTotal(newTotal - groupPrice)
                    print(createCoffee) # print drawing 
                else:
                    print("Money will be refunded")
                    refund() # call refund
        except ValueError:
            print("Error! Please enter a whole number!")

# this funciton will return any extra money back to user
def refund():
    # set variable based on class method
    returnTotal = newMachine.getTotal()
    # string drawing 
    coin = '''______________
              \  ___
               \/   \    
                \\___/
                 \     ___      ___
                  \   /   \    /   \   |
                   \__\___/____\___/___|'''

    #make sure there is something to give back
    if returnTotal > 0:
        print("\nReturning " + "${:.2f}".format(returnTotal) + "...")
        print(coin) # print drawing
        newMachine.setTotal(0.0) # set new total
    else:
        print("\nNo change available!")

    
# call main method
main()

print("\nThank you come again!")
