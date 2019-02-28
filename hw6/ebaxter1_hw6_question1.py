'''
File name: ebaxter1_hw6_question1.py
made by: Erin Baxter
This program creates a pie chart based on expenses
'''
# import matplot
import matplotlib.pyplot as plt

print("Hello and welcome to the Pie Chart Generator 11,000!\n")

# main method that opens file, reads it and outputs chart 
def main():
    #open file 
    print("Opening file...")
    getFile = open("expenses.txt", "r")

    #variables for data 
    cost_labels = []
    costs = []

    # read each line of file and put into variable lists 
    print("Reading file...")
    for line in getFile:
        #print(line)
        newLabel, newCost = line.strip().split(":")
        cost_labels.append(newLabel)
        costs.append(newCost)

    # add data to chart
    print("Creating chart...")
    plt.pie(costs, labels=cost_labels)

    #name chart
    plt.title("Last Month Expenses")

    #display chart 
    print("Displaying chart...")
    plt.show()

    #close file
    print("Closing file...")
    getFile.close()
    

#call main
main()

print("\nGoodbye and see you next time! Program ending")
