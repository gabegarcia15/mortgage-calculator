from art import *

tprint("Mortgage Payments", font="charl")


#1
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
            exit()
        else:
            print("That's not a valid response. Try again!")
            is_buying_home = input("Are you considering buying a home? (Y/N): ")

is_buyer()     

#2
home_price = int(input("How much is the home you want to purchase?: "))
down_payment = int(input("How much is the down payment?: "))
loan_amount = home_price-down_payment
interest_rate = float(input("How much is the interest rate? (e.g. 6.09 is 6.09%): "))
monthly_interest_rate = (interest_rate*.01)/12.00
loan_term = int(input("What is the loan term? (e.g. 30 is 30 years): "))
loan_term_payments = loan_term*12

first_numerator = (1+monthly_interest_rate)**loan_term_payments
second_numerator =  monthly_interest_rate*first_numerator
#numerator = loan_amount*((1+monthly_interest_rate)**loan_term_payments)
denominator = ((1+monthly_interest_rate)**loan_term_payments)-1
mortgage_payment = loan_amount*(second_numerator/denominator)

# Print Monthly Mortgage Payment
mortgage_payment_format_float = "{:.2f}".format(mortgage_payment)
print(f"Your monthly mortgage payment is ${mortgage_payment_format_float}.")