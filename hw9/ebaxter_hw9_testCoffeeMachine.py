'''
File Name: ebaxter_hw9_testCoffeeMachine.py
Made by: Erin Baxter
This program will have the constructors to test the methods in coffeeMachine
'''
from ebaxter_hw9_coffeeMachine import coffeeMachine
newMachine = coffeeMachine()

def main():
    amount, price = menu()
    print(f"The quantity of cups currently in the machine is: {amount} and the price per cup is: " + "${:.2f}".format(price))
    
    try:
        quart = int(input("Please enter the number of quarters you would like to insert: "))
        dime = int(input("Please enter the number of dimes you would like to insert: "))
        nick = int(input("Please enter the number of nickeles you would like to insert: "))

        money = insert(quart, dime, nick)
        select()
    except ValueError:
        print("Error! Please enter a whole number!")

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
        refund()
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
    coin = ''' ___
              /   \
              \___/
    print("\nReturning " + "${:.2f}".format(returnTotal) + "...")
    newMachine.setTotal(0.0)
    print("Thank you come again!")
    

    
# call main method
main()
