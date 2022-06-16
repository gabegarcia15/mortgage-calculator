from art import *

tprint("Mortgage Payments", font="charl")



def is_buyer():
    # Input
    is_buying_home = input("Are you considering buying a home? (Y/N): ")
    buyer = True

    while buyer == True:
        if(is_buying_home.upper())=="Y":
            buyer = False
            print("Good Luck!")
        elif(is_buying_home.upper())=="N":
            buyer = False
            print("Too Bad!")
        else:
            print("That's not a valid response. Try again!")
            is_buying_home = input("Are you considering buying a home? (Y/N): ")

is_buyer()        