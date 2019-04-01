'''
File Name:ebaxter_hw8.py
Made by: Erin Baxter
This program save user data as dictionary and then output it to a file.
'''

print("Hello and welcome to the Email Dictionary Generator 18,000!\n")

def main():
      # vairbale to to program running
      noStop = "y"

      while noStop == "y":
          try:
              menuOption = int(input(f'''What would you like to do?\n1. Look up email address(enter 1)\n2. Add new name and email address(enter 2)\n3. Update existing email address(enter 3)\n4. Delete existing name and email address(enter 4)\n5. Exit program (enter any key other then 1-4)\nEnter option: '''))
              if choice == 1:
                lookUpValue()
              elif choice == 2:
                addValue()
              elif choice == 3:
                updateValue()
              elif choice == 4:
                delValue()
          except ValueError:
              #writeValue()
              noStop = "n"
                      
          
'''
def lookUpValue():

def addValue():

def updateValue():

def delValue():
      
def writeFile():
'''
      
#calls main
main()

print("Program ending, goodbye!")
