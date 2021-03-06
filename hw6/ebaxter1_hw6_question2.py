'''
File name: ebaxter1_hw6_question2.py
made by: Erin Baxter
This program will create either a bar chart or line graph for gas file
'''

import matplotlib.pyplot as plt

print("Hello and welcome to the Gas Averages Data Displayer 12,000!\n")

#main function that opens file, reads file and then sends data to other functions
def main():
    #open file 
    print("Opening file...")
    getFile = open("1994_Weekly_Gas_Averages.txt", "r")

    #vairbales for data
    allGas = []
    totalWeeks = []
    i = 1

    #read file
    print("Reading file...")
    for line in getFile:
        allGas.append(float(line.strip()))
        totalWeeks.append(i)
        i += 1

    #close file
    print("Closing file...")
    getFile.close()

    #pick type of graph
    graphType = input("\nWould you like the data as a bar chart or a line graph?(Enter bar or line): ")
    graphType = graphType.lower().strip()

    if graphType == "line":
        makeLine(totalWeeks, allGas)
    elif graphType == "bar":
        makeBar(totalWeeks, allGas)
    else:
        print("\nInvaild input. Please try again and enter 'line' or 'bar'.")

#this function will make a line graph based on the data from file 
def makeLine(x,y):
    #make graph 
    print("\nCreating Graph...")
    plt.plot(x,y)
    plt.title("Average Gas Prices per Week for 1994", color="purple")
    plt.xlabel("Week Number", color='red')
    plt.ylabel("Average Gas Price", color='red')
    plt.grid(True)

    #display graph
    print("Displaying Graph...")
    plt.show()

#this function will make a bar chart based on the data from file 
def makeBar(x,y):
    #make graph 
    print("\nCreating Graph...")
    plt.bar(x,y, color="green")
    plt.title("Average Gas Prices per Week for 1994", color="purple")
    plt.xlabel("Week Number", color='red')
    plt.ylabel("Average Gas Price", color='red')
    plt.grid(True)

    #display graph
    print("Displaying Graph...")
    plt.show()


#call main
main()

print("\nGoodbye for now! Program now ending")
