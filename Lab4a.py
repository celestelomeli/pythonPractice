#--------------------------------------------------------------------------------------
# This program calculates income tax owed on gross income. 
#--------------------------------------------------------------------------------------
# Name:          Maria Lomeli
# Date:          November 13, 2021
# Reference:     A4a Lab
# Title:         Income Tax
# Inputs:        Average U.S. Income and User's Gross Income    
# Process:       Determines user's income tax rate based on user inputs and calculates
#                user's income tax owed.      
# Outputs:       The users input, income tax rate, and income tax owed.
#---------------------------------------------------------------------------------------
# Define main
def main():
    # Declare/Initialize the variables
    averageIncome = 0
    grossIncome   = 0
    incomeTaxRate = 0
    incomeTaxOwed = 0  
    

    # User inputs
    averageIncome   = input("Please enter the average U.S. income            :$")
    grossIncome     = input("Please enter your gross income                  :$")
    
    # Caculates user's tax bracket value
    taxBracket = float(grossIncome) / float(averageIncome)

    # Determines user's exact income tax rate based off of their tax bracket value 
    if (taxBracket >= 0 and taxBracket <= .75):
        incomeTaxRate = .12
    elif (taxBracket >= .76 and taxBracket <= 1.25):
        incomeTaxRate = .15
    elif (taxBracket >= 1.26 and taxBracket <= 2.00):
        incomeTaxRate = .18
    else:
        (taxBracket > 2.00)
        incomeTaxRate = .20

    # Calculates income tax owed using income tax rate value 
    incomeTaxOwed = float(grossIncome) * incomeTaxRate

# Displays user inputs and values calculated for average income, gross income, income tax 
# rate and income tax owed 
    print("----------------------------------------------------------------")
    print("The average U.S income is        :$", averageIncome)
    print("Your gross income is             :$", grossIncome)
    print("Your income tax rate is          :",incomeTaxRate * 100, "%")
    print("Your income tax owed is          :$", incomeTaxOwed)

# Call main 
main()
