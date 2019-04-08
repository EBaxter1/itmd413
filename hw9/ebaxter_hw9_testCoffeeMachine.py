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
    except ValueError:
        print("Error! Please enter a whole number!")

def menu():
    quantity = newMachine.getQuantity()
    price = newMachine.getPrice()
    print(quantity, price)
    return quantity, price

def insert(quarters, dimes, nickels):
    price = newMachine.getPrice()
    userTotal = (quarters * 0.25) + (dimes * 0.10) + (nickels * 0.05)
    newMachine.setTotal(userTotal)
    return userTotal

def select(): #add something to say how many cups they want
    newTotal = newMachine.getTotal()
    singlePrice = newMachine.getPrice()
    inventory = newMachine.getQuantity()

    try:
        amount = int(input("How many cups of coffee do you want?: "))

        if (newTotal / amount) == singlePrice and amount <= inventory:
            print("Coffee is now being dispensed..")
            newMachine.setQuantity(inventory - amount)
            print('''______
                  ______   |
                        |__|
                         ||
                         || 
                   ______________
                   \             /
                    \           /
                     \         /  
                     |        |
                     |        |
                     |        |
                     |________|
                  ''')
             print('''
                         |||                            
                   ______________
                   \             /
                    \ Caution   /
                     \  Hot!   /  
                     |        |
                     |        |
                     |        |
                     |________|
                  ''')
            print("Coffee done pouring. Enjoy!") 
    except ValueError:
        print("Error! Please enter a whole number!")
'''
def refund():
'''
    
# call main method
main()
