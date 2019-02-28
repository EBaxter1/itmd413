'''
File name: ebaxter1_hw6_question1.py
made by: Erin Baxter
This program creates a pie chart based on expenses
'''

import matplotlib.pyplot as plt

print("Hello and welcome to the Pie Chart Generator 11,000!\n")


def main():
    print("Opening file...")
    getFile = open("expenses.txt", "r")

    cost_labels = []
    costs = []

    print("Reading file...")
    for line in getFile:
        #print(line)
        newLabel, newCost = line.strip().split(":")
        cost_labels.append(newLabel)
        costs.append(newCost)

        
    print("Creating chart...")
    plt.pie(costs, labels=cost_labels)

    plt.title("Last Month Expenses")

    print("Displaying chart...")
    plt.show()
    
    print("Closing file...")
    getFile.close()
        


#call main
main()

print("\nGoodbye and see you next time! Program ending")
