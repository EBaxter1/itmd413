'''
File Name: ebaxter_hw10_testInheritance.py
Made by: Erin Baxter
This program will test the Employee and ProductionWorker classes by interacting with them
'''

# get class information from other file
# from ebaxter_hw10_inheritance import Employee
from ebaxter_hw10_inheritance import ProductionWorker
# global variable of new object from class

newWorker = ProductionWorker("Ana", 1198, 1, 12)

print(newWorker.getShift())
newWorker.displayData()
