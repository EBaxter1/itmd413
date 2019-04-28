'''
File name: ebaxter_hw12.py
Made by: Erin Baxter
This program has a digits reverse function and a decimal to hex function
'''

print("Hello and welcome to the Recursion Fun Maker 26,000!\n")

def main():
    number = int(input("Please enter a number to test: "))

    reverseDisplay(number, 4)

def reverseDisplay(value, count):
   getLength = len(str(value))
   newList = list(str(value))
   num = newList.pop()
   newList.insert((getLength - 1), num)
   print(newList)
   value = int("".join(newList))
   print(value)
   if count > 0:
       reverseDisplay(value, (count - 1))

#def decimalToHex(value):


# call main 
main()

print("Goodbye!")
