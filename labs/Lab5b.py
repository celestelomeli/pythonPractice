#-----------------------------------------------------------------------
# This program calculates cannibas sales for the month for states selling
# cannabis. Calculates total taxes to pay for pot sales. 
#-----------------------------------------------------------------------
# Name   : Maria Lomeli
# Date   : November 20, 2021
# Title  : A5b Pot Sales
# Inputs : State (CA, OR, WA) of sales, total pot sales
# Process: User enters in a valid state, user enters in a valid sales per state
#          Based on user input, calculate the tax for the respective state
# Outputs: User input, validate state code, validate pot sales amount, pot tax owed
#----------------------------------------------------------------------
# import math function to use ceil
import math

# set Global Constants for fixed values in the program
# Max total sales allowed in CA
CA_MAX = 500000.00

# Max total sales allowed in Oregon
OR_MAX = 200000.00

# Max total sales allowed in Washington
WA_MAX = 300000.00

#CA tax rate
CA_TAX = .15
# OR tax rate
OR_TAX = .12
# WA tax rate
WA_TAX = .17

# Minimum tax values for each state
CA_MIN_TAX = 37500
OR_MIN_TAX = 12000  
WA_MIN_TAX = 25500

# Main module
def main():
   
    # Initialize variable - set state to empty string
    state    = ""
    # Initialize variable - pot sales for total pot sales
    potSales = 0
    # Initialize variable - pot tax for total taxes using pot sales
    potTax   = 0
    
    # Print message header for program
    print("   Pot Sales Calculator      ")
    print("*****************************")

    # Get state from validateState() function
    initialState    = input("Please enter a state (CA,WA,OR): ")
    state    = validateState(initialState)
    # Get valid pot sales amount
    initialPotSales = float(input("Please enter a sales amount for your business: "))

    # Calculate pot sales
    potSales = int(validateMaxPotSales(state, initialPotSales))

    # Calculate pot tax
    potTax = float(minPotTax(potSales, state))

    # Format values to display 2 decimal places
    potTax   = "{:.2f}".format(potTax)

    # Print the results
    print("  Results                   ")
    print("*****************************")
    print("Initial State User Input: ", initialState)
    print("Initial Sales User Input: $", initialPotSales)
    print("\nValidated State of Sales: ", state)
    print("Validated Pot Sales     : $" , potSales)
    print("Validated Pot Taxes     : $",  potTax)

     
# validateState function prompts user for input and returns the users correct state
def validateState(state):
    # Initialize local variable
    notValidState = True

    # Get valid state code
    while(notValidState):
        try:
            # Check if the value passed triggers a false condition
            if (state != "CA" and state != "WA" and state != "OR"):
                # Reprompt user
                state = input("Please enter a valid state (CA, WA, OR): ")
            else:
                notValidState = False
        except NameError:
            print("Error")
    return state

# validateMaxPotSales - determine the correct value for pot sales per state
def validateMaxPotSales(state, potSales):
    
    # Initialize notValidSales
    notValidSales = True  
    
    # Start loop to validate sales amount
    while notValidSales:
        try: 
            # Check through each possibility for state entered and reprompt if necessary
            if state == "CA" and potSales > CA_MAX:
                potSales = float(input("Invalid sales total for CA. Please enter a Max value of $500000.00: $"))
            elif state == "WA" and potSales > WA_MAX:
                #If pot sales > :
                potSales = float(input("Invalid sales total for WA. Please enter a Max value of $300000.00: $"))
            elif state == "OR" and potSales > OR_MAX:
                potSales = float(input("Invalid sales totals for OR. Please enter a Max value of $200000.00: $"))
            else:
                # If no conditions are triggered than the value is valid, change notValidSales to exit loop
                notValidSales = False  
        except NameError:
            print("Error")    
    # Return pot sales as rounded integer
    return math.ceil(int(potSales))

# Minimum pot tax
def minPotTax(totalPotSales, state):
    
    # Initialize variable for total taxes
    totalTaxes = 0.0
    
    # Check which state and check if the taxes are less than the minimum required
    if state == "CA":
        totalTaxes = totalPotSales*CA_TAX
        while(totalTaxes < CA_MIN_TAX):
            totalTaxes = CA_MIN_TAX
    # Check which state and check if the taxes are less than the minimum required
    elif state == "OR":
        totalTaxes = totalPotSales*OR_TAX
        while(totalTaxes < OR_MIN_TAX):
            totalTaxes = OR_MIN_TAX
    # Check which state and check if the taxes are less than the minimum required
    elif state == "WA":
        totalTaxes = totalPotSales*WA_TAX
        while(totalTaxes < WA_MIN_TAX):
            totalTaxes = WA_TAX
    # Check which state and check if the taxes are less than the minimum required
    else:
       print("Error")
    # Return totalTaxes
    return totalTaxes

# Call main
main()
