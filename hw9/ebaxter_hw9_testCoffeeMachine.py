'''
File Name: ebaxter_hw9_testCoffeeMachine.py
Made by: Erin Baxter
This program will have the constructors to test the methods in coffeeMachine
'''
# get class information from other file
from ebaxter_hw9_coffeeMachine import coffeeMachine
#make a global variable for bew object
newMachine = coffeeMachine()

#main method gives user menu options for what they want to do
def main():
    noStop = "y"

    while noStop == "y":
        try:
            menuOption = int(input(f'''\nWhat would you like to do?\n1. Check current inverntory and price(enter 1)\n2. Insert coins(enter 2)\n3. Select coffee(enter 3)\n4. Refund money(enter 4)\n5. Exit program (enter any key other then 1-4)\nEnter option: '''))
            if menuOption == 1:
                amount, price = menu()
                print(f"\nThe quantity of cups currently in the machine is {amount} and the price per cup is: " + "${:.2f}".format(price))
            elif menuOption == 2:
                if newMachine.getQuantity() == 0:
                    print("\nCurrent inventory is 0. Coffee can not be made. please try again later")
                else:
                    try:
                        quart = int(input("\nPlease enter the number of quarters you would like to insert: "))
                        dime = int(input("Please enter the number of dimes you would like to insert: "))
                        nick = int(input("Please enter the number of nickeles you would like to insert: "))

                        money = insert(quart, dime, nick)
                    except ValueError:
                        print("Error! Please enter a whole number!")
            elif menuOption == 3:
                select()
            elif menuOption == 4:
                refund()
            else:
                noStop = "n"
        except ValueError:
            noStop = "n"

       
   

def menu():
    quantity = newMachine.getQuantity()
    price = newMachine.getPrice()
    return quantity, price

def insert(quarters, dimes, nickels):
    price = newMachine.getPrice()
    userTotal = (quarters * 0.25) + (dimes * 0.10) + (nickels * 0.05)
    newMachine.setTotal(userTotal)
    return userTotal

def select():
    newTotal = round(newMachine.getTotal(), 2)
    singlePrice = newMachine.getPrice()
    inventory = newMachine.getQuantity()
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
    print("\nCurrent Change Inserted: " + "${:.2f}".format(newTotal))
    if inventory == 0:
        print("Current inventory is 0. Coffee can not be made. please try again later")
        if newTotal > 0:
            refund()
    elif newTotal == 0:
        print("Please insert coins. Price per cup is " + "${:.2f}".format(singlePrice))
    else:
        try:
            amount = int(input("How many cups of coffee do you want?: "))
            if (newTotal / amount) == singlePrice and amount <= inventory:
                newMachine.setQuantity(inventory - amount)
                newMachine.setTotal(0.0)
                print(createCoffee)
            elif newTotal != (amount * singlePrice):
                print("Error! Exact change is required, price per cup is " + "${:.2f}".format(singlePrice) + ". Please try again with a total change amount of " + "${:.2f}".format(amount * singlePrice))
                refund()
            elif amount > inventory and inventory > 0:
                ask = input(f"There is not enough inventory for {amount} cup(s) of coffee. Current quantity of cups is {inventory}. Would you like to make {inventory} cup(s) of coffee instead?(Enter y for yes or anything else for no): ")
                if ask.lower() == "y":
                    groupPrice = singlePrice * inventory 
                    newMachine.setQuantity(0)
                    newMachine.setTotal(newTotal - groupPrice)
                    print(createCoffee)
                else:
                    print("Money will be refunded")
                    refund()
        except ValueError:
            print("Error! Please enter a whole number!")

def refund():
    returnTotal = newMachine.getTotal()
    coin = '''______________
              \  ___
               \/   \    
                \\___/
                 \     ___      ___
                  \   /   \    /   \   |
                   \__\___/____\___/___|'''

    if returnTotal > 0:
        print("\nReturning " + "${:.2f}".format(returnTotal) + "...")
        print(coin)
        newMachine.setTotal(0.0)
    else:
        print("\nNo change available!")
    

    
# call main method
main()

print("\nThank you come again!")
