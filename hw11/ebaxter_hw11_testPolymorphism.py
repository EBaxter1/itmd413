'''
File Name: ebaxter_hw11_testPolymorphism.py
Made by: Erin Baxter
This program will go through the classes created in th epolumorphism file and call the print function and test them using issinstance
'''

from ebaxter_hw11_polymorphism import Ship
from ebaxter_hw11_polymorphism import CruiseShip

'''
for a in [Ship("Blue", 1917), CruiseShip(35)]:
    a.displayData()
'''


b = Ship("Blue", 1917)
b.displayData()


a = CruiseShip(35)
a.displayOData()

