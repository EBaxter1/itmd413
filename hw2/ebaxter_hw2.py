# File Name: hw2
# Made by: Erin Baxter
# This program helps a user troubleshoot for a Diesel Engine

print("Hello and welcome to the 'What's the *beep* is wrong with my diesel engine!?!'\n")

try:
    print("What color is the status light for the engine?")
    light = int(input("Enter 1 for Green, 2 for Red, or 3 for Amber: "))
    print("\n")
except ValueError:
    print("\nInvaild choice selected, please try again with choice 1-3. Program ending")
    quit()

# variables
meter = "na"
velocity = "na"
pressure = "na"


# check first lights 
if (light == 1):
    print("Do restart procedure and you should be all set!")
    exit()
elif (light == 3):
    print("Check fuel line service routine and see what you can find.")
elif (light == 2):
    print("Shut off all input lines!")
    try:
        meter = int(input("Next, check meter #3 and enter the number, without digits, that is shown: "))
    except ValueError:
        print("\nInvaild input, please try again with an integer. Program ending")
        quit()
else:
    print("Invalid choice entered. Program now ending")
    quit()

print("\n")


# check meter
if (meter < 50):
    print("Check the main line and test for pressure")
    try:
        pressure = int(input("What did the test show? Enter 1 for Normal, 2 for High or 3 for Low: "))
    except ValueError:
        print("\nInvaild choice selected, please try again with choice 1-3. Program ending")
        quit()
elif (meter >= 50):
    print("Measure the flow velcouty at inlet 2-B")
    try:
        velocity = int(input("What was the velocity? Enter 1 for Normal, 2 for High or 3 for Low: "))
    except ValueError:
        print("\nInvaild choice selected, please try again with choice 1-3. Program ending")
        quit()
elif (meter == "na"):
        exit()

# for pressure
if (pressure == 1):
    print("Refer to motor service manual.")
elif (pressure == 2 or pressure == 3):
    print("Refer to main line manual")
else:
    print("\nInvaild choice selected, please try again with choice 1-3. Program ending")
    quit()

    
# for velocity
if (velocity == 1):
    print("Refer to inlet service manual.")
elif (velocity == 2 or velocity == 3):
    print("Refer unit for factory service")
else:
    print("\nInvaild choice selected, please try again with choice 1-3. Program ending")
    quit()

print("I hope I helped! Have a nice day, goodbye!")
