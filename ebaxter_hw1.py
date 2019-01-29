# File Name: hw1
# Made by: Erin Baxter
# This program provides information about stocks that is provided by the user

print("Hello, welcome to the stock program!\n")
name = input("What is your name? ")
print("Hello " + name + "!\n")

# inputs
try:
    stock_amount = int(input("Please input the number of stocks you purchased:"))
    stock_cost = float(input("Please input the amount of money you paid for each stock:"))
    commission = float(input("Please input the commission percent for the stock as a desimal(i.e 'for 3% enter 0.03')"))
    sold_cost = float(input("Please input the amount you sold each stock for:"))
    sold_amount = int(input("Please input the number of stocks you sold:"))
except ValueError:
    print("\nIncorrect format entered for one of the prompts. Program ending")
    quit()
    
#calulations
stock_total = stock_amount * stock_cost
commission_total = commission * stock_total
sold_total = sold_cost * sold_amount
commission_sold_total = sold_total * commission
grand_total = stock_total + commission_sold_total + commission_total
result = sold_total - grand_total
 
# outputs
print("\nThe total amount of money you paid for the stocks is: ${0:.2f}".format(stock_total))
print("The amount of money you paid to the stockbroker for all the stocks is: ${0:.2f}".format(commission_total))
print("The total amount you got for selling the stocks is: ${0:.2f}".format(sold_total))
print("The amount of money paid to the stockbroker for the sold stocks is: ${0:.2f}".format(commission_sold_total))
print("Your total money you have left after selling the stocks and paying out to the stockbroker is: ${0:.2f}".format(result))
if result > 0:
    print("You made a profit with stocks " + name + "!")
else:
    print("You lost money with stocks " + name + " :(")


