# Imports
import mouse
import os
import random

# User starts as not signed in
SignedIn = False

# Check if the input is a number
def numCheck(num):
  num_is_int = False
  #Try the input as a number
  try:
    int(num)
    #If the input is a number put num_is_int as True
    num_is_int = True
  except ValueError:
    print("\nTry again using a whole number")
    # If the input isn't a number put num_is_int as False
    num_is_int = False
  # Return num_is_int
  return num_is_int

# ----------------------Yes or no checker---------------------------
def yesNo(answer):
  yes = False
  if answer.lower() == "yes" or answer.lower() == "y":
    yes = True
  else:
    yes = False
  return yes

# Check if the responce is yes
def yesNo(answer):
    yes = False
    if answer.lower() == "yes" or answer.lower() == "y":
        yes = True
    else:
        yes = False
    return yes


# Print out the choices a user has
def menu():
    print("Select your choice:")
    if not SignedIn:
        login = print("1. Login")
        signUp = print("2. Signup")
        end = print("3. Exit")

    else:
        profile = print("1. Profile")
        checkMon = print("2. Check Balance")
        addMon = print("3. Deposit Money")
        takeMon = print("4. Withdraw Money")
        logout = print("5. Logout")
    


def createAccount():
    confirm = False
    while not confirm:
        # Start the account creation project
        userFirstName = input("\nFirst Name: ")
        # Ask user for last name
        userLastName = input("\nLast Name: ")
        # Ask user to confirm their choices if not clear screen and ask again
        answer = input("\nSay yes to confirm your choices? ")
        if not yesNo(answer):
            # If the user says no repeat the loop and clear the screen
            confirm = False

        else:
            # End the loop and continue
            confirm = True
    # Get the users pin using pin maker function
    currentpass = pinMaker()
    # Now get a pin
    newNum = False
    while not newNum:
        userNum = random.randint(3000, 9999999)
        print(userNum)
        newNum = True
        # add to the table


def pinMaker():
    passMatch = False

    # Print pins rules
    print("\nInsert a pin that is at least 4 digits long: \n")
    # while the pins don't match
    while not passMatch:
        # ask for a pin
        userInputPin = input("\nPin: ")
        # If pin is less than 4 don't accept pin
        if numCheck(userInputPin):
          if len(userInputPin) >= 4:
              # Ask user to confirm the pin
              userPinConfirm = input("Confirm pin: ")

              # Check if the pins are same
              if userInputPin == userPinConfirm:
                  print("Pins match.")
                  # Make passMatch into true to make the while statement end
                  passMatch = True
              else:
                  print("Pins do not match. \nTry Again")
                  passMatch = False
          else:
              print("Pin is too short try again")
              passMatch = False

          userPin = userInputPin
    # show the first and the last two characters of the pin
    # Remove two from the number so that you can show the pin with the right amount
    passNum = len(userPin) - 3
    passBlocked = (
        userPin.split()[0][0]
        + "*" * passNum
        + userPin.split()[0][-1]
    )
    yes_no = input(f"Confirm that you want to us this pin ('{passBlocked}')\n")
    if yesNo(yes_no):
        print("Ok, pin added to database")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        return userPin
    else:
        print("Ok, create a new pin!")
        # Run the pin maker again
        pinMaker()


""" This is used to test code (delete when finished)"""
pinMaker()

# Welcome the user to the
print("Hello, welcome to the Blank Bank Place App!")
