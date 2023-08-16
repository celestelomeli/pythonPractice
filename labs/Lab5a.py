#-----------------------------------------------------------------------
# This program calculates the number of hours a user must work to
# cover the expenses they accumulate in a month.
#-----------------------------------------------------------------------
# Name     : Maria Lomeli
# Date     : November 20, 2021
# Reference: A5a Lab
# Title    : Hours to Work
# Inputs   : user's choice, expense costs, and hourly wage
# Process  : User determines between 2 options to enter expenses.
#            First option uses a do while loop, while second option 
#            uses a fixed for loop. At the end calculates how many hours
#            user must work in order to cover expenses.
# Outputs  : The users inputs, total expenses cost and total hours necessary to work
#----------------------------------------------------------------------
# import math to use round
import math

#Define main
def main():
    # Initialize variables - users choice of option 1 or 2
    userChoice  = 0
    # Initialize variables - users hourly pay rate
    hourlyRate  = 0
    # Intiailize variables - the hours to work
    hoursToWork = 0

    # Initialize variables - expenseCost
    expenseCost = 0

    # Initialize variables = total expenses
    total       = 0
    

    # Expense Calculator
    
    print(" Expense Calculator                                      ")
    print("***********************************************************")
    # Get user input for choice of input
    userChoice = int(input("Option 1: Enter N items then enter 0 to continue\nOption 2: Enter a specific number of expenses\n\n **** Your Decision (Enter 1 or 2): "))
    
    # Enter section 1 or 2 depending on user's choise
    if userChoice == 1:
        # Execute scenario 1
        print("\n***********************************************")
        print("* You have selected option 1. Please continue to \n* enter an expense value and enter 0 to end")
        print("*************************************************")
        # Prompt the user for input
        expenseCost = float(input("Enter an expense value to sum (or 0 to quit): $"))

        while (expenseCost != 0):
            #Add number to total
            total = total + expenseCost
            #Get the next expense cost
            expenseCost = float(input("Enter an expense value to sum (or 0 to quit): $"))
    # User chooses second option
    elif userChoice == 2:
        # Execute scenario 2
        count = 0
        print("\n**************************************")
        print("* You have selected Option 2.")
        print("****************************************")
         # Get num of expenses from user to control the amount of iteratoins
        numOfExpenses = int(input("Please enter a fixed amount of expenses you will enter:"))
        
        # Start for loop with user defined numOfExpenses
        for count in range (numOfExpenses):
            # Get the next expense cost
            expenseCost = float(input("Enter cost for expense: $"))
            # Sum the total
            total = total + expenseCost
    else:
        print("************\nThat was not an option. Good bye\n*********************")
    
    # Prompt user for hourlty pay rate
    hourlyRate = float(input("\nPlease enter the hourly pay rate: $"))

    # Calculate hours necessary to work
    hoursToWork = math.ceil(total / hourlyRate)

    hourlyRate = "{:.2f}".format(hourlyRate)
    total      = "{:.2f}".format(total)
    # Print user input, expense costs, and total hours needed to work
    print("***********************************************************************")
    print("Hourly Rate            : $", hourlyRate)
    print("Your total Expense Cost: $", total)
    print("You must work ", hoursToWork, " hours in order to pay for all of those items. \nYou better get to work!" )
    print("***********************************************************************")
 #Call main
main()
